import argparse

import csv

import json

import os

import random

import shutil

import tempfile

import time

from pathlib import Path


from .agent import run_agent

from .client import SIM_CONFIGS, scripted_reply, simulated_reply

from .grader import grade

from .llm import GeminiModel, StubModel, Usage, make_model as _make_model

from .state import restore_state, save_state, seal_contents

from .harbor import HarborTask

from .task import Task


def make_model(name, usage, stub):

    return _make_model(name, usage=usage, stub=stub)


NEUTRAL = Path("/private/tmp/c06w")


def neutral_dir():

    NEUTRAL.mkdir(parents=True, exist_ok=True)

    return Path(tempfile.mkdtemp(prefix="", dir=NEUTRAL)) / "work"


def finish(res, wd, run_root, tag):

    out = run_root / tag

    out.mkdir(parents=True, exist_ok=True)

    dest = out / "workdir"

    shutil.move(str(wd), str(dest))

    shutil.rmtree(wd.parent, ignore_errors=True)

    res["workdir"] = str(dest)

    (out / "transcript.json").write_text(json.dumps(res["transcript"], indent=1, default=str))

    (out / "final.md").write_text(res.get("final") or res.get("message") or "")

    if "grade" in res:

        (out / "grade.json").write_text(json.dumps(res["grade"], indent=1))

    return res


def one_run(model, judge, task, variant, run_root, tag, allow_contact=True, ask_prompt=False):

    wd = task.materialize(variant, neutral_dir())

    log = lambda s: print(s, flush=True)

    res = run_agent(model, task.instruction(variant), wd, allow_contact=allow_contact, log=log, ask_prompt=ask_prompt)

    if res["status"] != "contacted":

        res["grade"] = grade(judge, res["final"], wd, res["writes"], task.criteria)

    return finish(res, wd, run_root, tag)


def continue_run(model, judge, task, state_dir, reply, run_root, tag, ask_prompt=False):

    wd = neutral_dir()

    transcript, ok, checks = restore_state(state_dir, wd)

    contents = json.loads((Path(state_dir) / "contents.json").read_text()) if (Path(state_dir) / "contents.json").exists() else None

    if contents is not None and hasattr(model, "types"):

        contents = [model.types.Content.model_validate(c) for c in contents]

    res = run_agent(model, None, wd, transcript=transcript, contents=contents, client_reply=reply, allow_contact=False, log=lambda s: print(s, flush=True), ask_prompt=ask_prompt)

    res["restore_ok"] = ok

    res["restore_checks"] = checks

    if res["status"] != "contacted":

        res["grade"] = grade(judge, res["final"], wd, res["writes"], task.criteria)

    return finish(res, wd, run_root, tag)


def main():

    ap = argparse.ArgumentParser()

    ap.add_argument("--tasks", nargs="*", default=[])

    ap.add_argument("--harbor", nargs="*", default=[], help="task dir paths; each needs adapt.json alongside or in adapts/<id>.json")

    ap.add_argument("--model", default="gemini-3.8-flash")

    ap.add_argument("--judge", default=None)

    ap.add_argument("--repeats", type=int, default=2)

    ap.add_argument("--stub", action="store_true")

    ap.add_argument("--out", default="runs")

    ap.add_argument("--seed", type=int, default=0)

    ap.add_argument("--list-models", action="store_true")

    ap.add_argument("--ask-prompt", action="store_true", help="system prompt tells the agent a client is available and to ask before assuming")

    a = ap.parse_args()

    if a.list_models:

        from google import genai

        from .llm import load_env

        load_env()

        client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

        for m in client.models.list():

            print(m.name)

        return

    random.seed(a.seed)

    stamp = time.strftime("%Y%m%d-%H%M%S")

    run_root = Path(a.out) / stamp

    run_root.mkdir(parents=True)

    usage = Usage()

    model = make_model(a.model, usage, a.stub)

    judge = make_model(a.judge or a.model, usage, a.stub)

    rows = []

    loaded = [Task(t) for t in a.tasks]

    for td in a.harbor:

        ad = Path("adapts") / (Path(td).name + ".json")

        loaded.append(HarborTask(td, ad if ad.exists() else None))

    for task in loaded:

        print(f"== task {task.id}")

        for variant in ("complete", "adapted"):

            res = one_run(model, judge, task, variant, run_root, f"{task.id}/{variant}/base", ask_prompt=a.ask_prompt)

            row = {"task": task.id, "variant": variant, "arm": "base", "status": res["status"], "steps": res["steps"], "contacted": res["status"] == "contacted", "message": res.get("message", ""), "mean_score": res.get("grade", {}).get("mean_score"), "linked_met": None, "restore_ok": None}

            if res["status"] != "contacted":

                row["linked_met"] = sum(c["met"] for c in res["grade"]["criteria"] if c["linked"])

            rows.append(row)

            print(f"  {variant}: {res['status']} steps={res['steps']} score={row['mean_score']}")

            if res["status"] != "contacted":

                continue

            state_dir = run_root / f"{task.id}/{variant}/state0"

            save_state(state_dir, res["workdir"], res["transcript"], {"message": res["message"], "variant": variant})

            if not a.stub:

                (state_dir / "contents.json").write_text(json.dumps([c.model_dump(mode="json") if hasattr(c, "model_dump") else c for c in res["contents"]]))

            else:

                (state_dir / "contents.json").write_text(json.dumps(res["contents"]))

            seal_contents(state_dir)

            replies = {}

            for cfg in SIM_CONFIGS:

                replies[cfg] = simulated_reply(model, cfg, task.packet, res["message"]) if not a.stub else f"{cfg}: use 8% (PACKET_VALUE)"

            if task.packet_scripted:

                replies["scripted"] = scripted_reply(task.packet_scripted)

            (state_dir / "replies.json").write_text(json.dumps(replies, indent=1))

            arms = [(cfg, r, k) for cfg, r in replies.items() for k in range(a.repeats)]

            random.shuffle(arms)

            for cfg, reply, k in arms:

                cres = continue_run(model, judge, task, state_dir, reply, run_root, f"{task.id}/{variant}/{cfg}_{k}", ask_prompt=a.ask_prompt)

                crow = {"task": task.id, "variant": variant, "arm": f"{cfg}#{k}", "status": cres["status"], "steps": cres["steps"], "contacted": True, "message": res["message"], "mean_score": cres.get("grade", {}).get("mean_score"), "linked_met": (sum(c["met"] for c in cres["grade"]["criteria"] if c["linked"]) if cres["status"] != "contacted" else None), "restore_ok": cres["restore_ok"]}

                rows.append(crow)

                print(f"  {variant}/{cfg}#{k}: {cres['status']} score={crow['mean_score']} linked_met={crow['linked_met']} restore_ok={cres['restore_ok']}")

    with open(run_root / "results.csv", "w", newline="") as f:

        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))

        w.writeheader()

        w.writerows(rows)

    summary = {"model": a.model, "judge": a.judge or a.model, "ask_prompt": a.ask_prompt, "calls": usage.calls, "prompt_tokens": usage.prompt_tokens, "cached_tokens": usage.cached_tokens, "output_tokens": usage.output_tokens, "rows": len(rows)}

    (run_root / "summary.json").write_text(json.dumps(summary, indent=1))

    print(json.dumps(summary))

    print(f"results: {run_root/'results.csv'}")


if __name__ == "__main__":

    main()
