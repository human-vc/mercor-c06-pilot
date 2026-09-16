import argparse

import csv

import json

import time

from pathlib import Path


from .agent import run_agent

from .client import scripted_reply

from .grader import grade

from .harbor import HarborTask

from .llm import GeminiModel, StubModel, Usage, make_model

from .run import continue_run, finish, neutral_dir

from .state import save_state, seal_contents


def tool_mix(transcript, start):

    calls = [e["call"] for e in transcript[start:] if e.get("call")]

    return {"n_calls": len(calls), "n_python": calls.count("run_python"), "n_read": calls.count("read_file"), "n_write": calls.count("write_file")}


def main():

    ap = argparse.ArgumentParser()

    ap.add_argument("task_dir")

    ap.add_argument("--model", default="gemini-3.8-flash")

    ap.add_argument("--judge", default=None)

    ap.add_argument("--contacts", type=int, default=4)

    ap.add_argument("--max-attempts", type=int, default=8)

    ap.add_argument("--ask-prompt", action="store_true")

    ap.add_argument("--variant", default="adapted")

    ap.add_argument("--stub", action="store_true")

    ap.add_argument("--out", default="runs/replay")

    a = ap.parse_args()

    usage = Usage()

    model = make_model(a.model, usage=usage, stub=a.stub)

    judge = make_model(a.judge or a.model, usage=usage, stub=a.stub)

    task = HarborTask(a.task_dir, Path("adapts") / f"{Path(a.task_dir).name}.json")

    root = Path(a.out) / time.strftime("%Y%m%d-%H%M%S")

    root.mkdir(parents=True)

    reply = scripted_reply(task.packet_scripted)

    log = lambda s: print(s, flush=True)

    rows = []

    contacts = 0

    attempts_run = 0

    for attempt in range(a.max_attempts):

        if contacts >= a.contacts:

            break

        attempts_run += 1

        tag = f"attempt_{attempt}"

        wd = task.materialize(a.variant, neutral_dir())

        res = run_agent(model, task.instruction(a.variant), wd, allow_contact=True, log=log, ask_prompt=a.ask_prompt)

        if res["status"] != "contacted":

            if "final" in res:

                res["grade"] = grade(judge, res["final"], wd, res["writes"], task.criteria)

            finish(res, wd, root, f"{tag}/base")

            rows.append({"attempt": attempt, "contacted": False, "arm": "base", "score": res.get("grade", {}).get("mean_score"), "linked_met": None, "steps": res["steps"], "restore_ok": None, **tool_mix(res["transcript"], 0)})

            print(f"{tag}: no contact, status {res['status']}", flush=True)

            continue

        contacts += 1

        state_dir = root / tag / "state0"

        save_state(state_dir, wd, res["transcript"], {"message": res["message"], "variant": a.variant})

        (state_dir / "contents.json").write_text(json.dumps([c.model_dump(mode="json") if hasattr(c, "model_dump") else c for c in res["contents"]]))

        seal_contents(state_dir)

        print(f"{tag}: contacted at step {res['steps']}", flush=True)

        start = len(res["transcript"])

        live = run_agent(model, None, wd, transcript=res["transcript"], contents=res["contents"], client_reply=reply, allow_contact=False, log=log, ask_prompt=a.ask_prompt)

        if "final" in live:

            live["grade"] = grade(judge, live["final"], wd, live["writes"], task.criteria)

        finish(live, wd, root, f"{tag}/uninterrupted")

        rows.append({"attempt": attempt, "contacted": True, "arm": "uninterrupted", "score": live.get("grade", {}).get("mean_score"), "linked_met": sum(bool(c["met"]) for c in live.get("grade", {}).get("criteria", []) if c["linked"]), "steps": live["steps"], "restore_ok": None, **tool_mix(live["transcript"], start)})

        print(f"{tag}/uninterrupted: {live['status']} score={rows[-1]['score']} linked={rows[-1]['linked_met']}", flush=True)

        rest = continue_run(model, judge, task, state_dir, reply, root, f"{tag}/restored", ask_prompt=a.ask_prompt)

        rows.append({"attempt": attempt, "contacted": True, "arm": "restored", "score": rest.get("grade", {}).get("mean_score"), "linked_met": sum(bool(c["met"]) for c in rest.get("grade", {}).get("criteria", []) if c["linked"]), "steps": rest["steps"], "restore_ok": rest["restore_ok"], **tool_mix(rest["transcript"], start)})

        print(f"{tag}/restored: {rest['status']} score={rows[-1]['score']} linked={rows[-1]['linked_met']} restore_ok={rest['restore_ok']} checks={rest.get('restore_checks')}", flush=True)

    with open(root / "replay.csv", "w", newline="") as f:

        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))

        w.writeheader()

        w.writerows(rows)

    paired = [(u, r) for u in rows for r in rows if u["attempt"] == r["attempt"] and u["arm"] == "uninterrupted" and r["arm"] == "restored"]

    diffs = [(r["score"] or 0) - (u["score"] or 0) for u, r in paired]

    summary = {"task": task.id, "model": a.model, "ask_prompt": a.ask_prompt, "attempts": attempts_run, "contacts": contacts, "pairs": len(paired), "mean_score_uninterrupted": sum((u["score"] or 0) for u, _ in paired) / max(1, len(paired)), "mean_score_restored": sum((r["score"] or 0) for _, r in paired) / max(1, len(paired)), "paired_diffs_restored_minus_uninterrupted": diffs, "calls": usage.calls, "prompt_tokens": usage.prompt_tokens, "cached_tokens": usage.cached_tokens, "output_tokens": usage.output_tokens}

    (root / "summary.json").write_text(json.dumps(summary, indent=1))

    print(json.dumps(summary))

    print(f"results: {root/'replay.csv'}")


if __name__ == "__main__":

    main()
