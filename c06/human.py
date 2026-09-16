import argparse

import csv

import json

from pathlib import Path


from .harbor import HarborTask

from .llm import GeminiModel, Usage, make_model

from .run import continue_run


TASKS = Path("data/apex-agents-v1.1/tasks")


def main():

    ap = argparse.ArgumentParser(description="Continue a saved state with a reply written by a person, several times, and grade each continuation.")

    ap.add_argument("state_dir", help="path to a state0 folder, e.g. runs/pilot_ask/<stamp>/<task>/adapted/state0")

    ap.add_argument("--reply-file", required=True, help="text file holding the person's reply, verbatim")

    ap.add_argument("--label", required=True, help="who answered, e.g. author, adapter, expert_finance; used as the arm name")

    ap.add_argument("--repeats", type=int, default=2)

    ap.add_argument("--model", default="gemini-3.8-flash")

    ap.add_argument("--judge", default=None)

    ap.add_argument("--ask-prompt", action="store_true", help="must match the prompt condition the state was produced under")

    a = ap.parse_args()

    state = Path(a.state_dir)

    variant_dir = state.parent

    tid = variant_dir.parent.name

    run_root = variant_dir.parent.parent

    task = HarborTask(TASKS / tid, Path("adapts") / f"{tid}.json")

    reply = Path(a.reply_file).read_text().strip()

    usage = Usage()

    model = make_model(a.model, usage=usage)

    judge = make_model(a.judge or a.model, usage=usage)

    meta = json.loads((state / "meta.json").read_text())

    print("QUESTION:", meta["message"][:600], "\nREPLY:", reply[:600], flush=True)

    rows = []

    for k in range(a.repeats):

        tag = f"{tid}/{variant_dir.name}/{a.label}_{k}"

        res = continue_run(model, judge, task, state, reply, run_root, tag, ask_prompt=a.ask_prompt)

        linked = [c for c in res.get("grade", {}).get("criteria", []) if c["linked"]]

        rows.append({"task": tid, "variant": variant_dir.name, "arm": f"{a.label}#{k}", "status": res["status"], "steps": res["steps"], "mean_score": res.get("grade", {}).get("mean_score"), "linked_met": sum(bool(c["met"]) for c in linked), "linked_total": len(linked), "restore_ok": res["restore_ok"]})

        print(f"{tag}: {res['status']} score={rows[-1]['mean_score']} linked={rows[-1]['linked_met']}/{rows[-1]['linked_total']} restore_ok={res['restore_ok']}", flush=True)

    out = variant_dir / f"human_{a.label}.csv"

    with open(out, "w", newline="") as f:

        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))

        w.writeheader()

        w.writerows(rows)

    replies = json.loads((state / "replies.json").read_text()) if (state / "replies.json").exists() else {}

    replies[a.label] = reply

    (state / "replies.json").write_text(json.dumps(replies, indent=1))

    print(json.dumps({"label": a.label, "calls": usage.calls, "prompt_tokens": usage.prompt_tokens, "cached_tokens": usage.cached_tokens, "output_tokens": usage.output_tokens}))

    print(f"results: {out}")


if __name__ == "__main__":

    main()
