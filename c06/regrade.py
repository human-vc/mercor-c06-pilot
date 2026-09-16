import argparse

import csv

import json

from pathlib import Path


from .grader import grade

from .harbor import HarborTask

from .llm import GeminiModel, Usage, make_model


TASKS = Path("data/apex-agents-v1.1/tasks")


def run_dirs(root):

    for final in sorted(Path(root).rglob("final.md")):

        d = final.parent

        if d.name == "state0":

            continue

        yield d


def main():

    ap = argparse.ArgumentParser()

    ap.add_argument("run_root")

    ap.add_argument("--judge", required=True)

    ap.add_argument("--only-unresolved", action="store_true", help="regrade only criteria whose stored grade was a parse failure")

    a = ap.parse_args()

    root = Path(a.run_root)

    usage = Usage()

    judge = GeminiModel(a.judge, usage=usage)

    tasks = {}

    rows = []

    for d in run_dirs(root):

        tid = d.relative_to(root).parts[0]

        variant, arm = d.relative_to(root).parts[1], d.name

        if tid not in tasks:

            tasks[tid] = HarborTask(TASKS / tid, Path("adapts") / f"{tid}.json")

        task = tasks[tid]

        old_path = d / "grade.json"

        if not old_path.exists():

            continue

        old = json.loads(old_path.read_text())

        final = (d / "final.md").read_text()

        if a.only_unresolved:

            bad = [i for i, c in enumerate(old["criteria"]) if str(c.get("rationale", "")).startswith(("PARSE_ERROR", "UNRESOLVED"))]

            if not bad:

                new = old

            else:

                new = json.loads(json.dumps(old))

                sub = grade(judge, final, d / "workdir", [], [task.criteria[i] for i in bad])

                for i, r in zip(bad, sub["criteria"]):

                    new["criteria"][i] = r

                resolved = [c for c in new["criteria"] if c.get("resolved", not str(c.get("rationale", "")).startswith("PARSE_ERROR"))]

                new["mean_score"] = sum(bool(c["met"]) for c in resolved) / max(1, len(resolved))

                new["n_unresolved"] = len(new["criteria"]) - len(resolved)

            out = d / "grade_repaired.json"

        else:

            new = grade(judge, final, d / "workdir", [], task.criteria)

            out = d / f"grade_{a.judge}.json"

        out.write_text(json.dumps(new, indent=1))

        linked = [c for c in new["criteria"] if c["linked"]]

        rows.append({"task": tid, "variant": variant, "arm": arm, "old_score": old["mean_score"], "new_score": new["mean_score"], "unresolved": new.get("n_unresolved", 0), "linked_met": sum(bool(c["met"]) for c in linked), "linked_total": len(linked)})

        print(f"{tid} {variant}/{arm}: {old['mean_score']:.2f} -> {new['mean_score']:.2f} (unresolved {new.get('n_unresolved', 0)})", flush=True)

    name = "regrade_repaired.csv" if a.only_unresolved else f"regrade_{a.judge}.csv"

    with open(root / name, "w", newline="") as f:

        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))

        w.writeheader()

        w.writerows(rows)

    print(json.dumps({"judge": a.judge, "calls": usage.calls, "prompt_tokens": usage.prompt_tokens, "output_tokens": usage.output_tokens}))


if __name__ == "__main__":

    main()
