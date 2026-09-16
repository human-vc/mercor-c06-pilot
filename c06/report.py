import argparse

import csv

import json

from collections import defaultdict

from pathlib import Path


PRICE = {"gemini-3.8-flash": (0.75, 3.75), "gemini-3.1-pro": (2.0, 12.0)}


def load(run_root):

    rows = list(csv.DictReader(open(Path(run_root) / "results.csv")))

    for r in rows:

        r["mean_score"] = float(r["mean_score"]) if r["mean_score"] else None

        r["linked_met"] = int(r["linked_met"]) if r["linked_met"] else None

        r["contacted"] = r["contacted"] == "True"

        r["restore_ok"] = r["restore_ok"] == "True" if r["restore_ok"] else None

    return rows


def fmt(x):

    return "?" if x is None else (f"{x:.2f}" if isinstance(x, float) else str(x))


def arm_dir(root, tid, variant, arm):

    cfg, k = arm.split("#")

    return root / tid / variant / f"{cfg}_{k}"


def excerpt(path, n=700):

    if not path.exists():

        return "(missing)"

    text = path.read_text().strip().replace("\n", " ")

    return text[:n] + ("..." if len(text) > n else "")


def linked_verdicts(path):

    if not path.exists():

        return "(no grade)"

    g = json.loads(path.read_text())

    return ", ".join(f"c{i}:{'met' if c['met'] else 'unmet'}" for i, c in enumerate(g["criteria"]) if c["linked"])


def main():

    ap = argparse.ArgumentParser()

    ap.add_argument("run_root")

    a = ap.parse_args()

    root = Path(a.run_root)

    rows = load(root)

    summary = json.loads((root / "summary.json").read_text())

    by_task = defaultdict(list)

    for r in rows:

        by_task[r["task"]].append(r)

    pin, pout = PRICE.get(summary["model"], (0, 0))

    cost = summary["prompt_tokens"] / 1e6 * pin + summary["output_tokens"] / 1e6 * pout

    lines = [f"# Pilot report: {root.name}", "", f"Model {summary['model']}, judge {summary['judge']}, {summary['calls']} calls, {summary['prompt_tokens']:,} prompt tokens ({summary.get('cached_tokens', 0):,} cached), {summary['output_tokens']:,} output tokens. List-price cost about ${cost:.2f} before caching discounts.", ""]

    lines += ["| task | complete: asked / score | adapted: asked / score | adapted branches (score, linked met) | restore ok |", "|---|---|---|---|---|"]

    n_adapted_contact = 0

    n_complete_contact = 0

    for tid, rs in by_task.items():

        comp = next((r for r in rs if r["variant"] == "complete" and r["arm"] == "base"), None)

        adap = next((r for r in rs if r["variant"] == "adapted" and r["arm"] == "base"), None)

        arms = [r for r in rs if r["variant"] == "adapted" and r["arm"] != "base"]

        n_adapted_contact += bool(adap and adap["contacted"])

        n_complete_contact += bool(comp and comp["contacted"])

        arm_txt = "; ".join(f"{r['arm']}: {fmt(r['mean_score'])}, {fmt(r['linked_met'])}" for r in arms) or "none"

        rest = all(r["restore_ok"] for r in arms) if arms else None

        lines.append(f"| {tid} | {comp['contacted'] if comp else '?'} / {fmt(comp['mean_score']) if comp else '?'} | {adap['contacted'] if adap else '?'} / {fmt(adap['mean_score']) if adap else '?'} | {arm_txt} | {rest} |")

    lines += ["", f"Contacted the client on {n_adapted_contact} of {len(by_task)} adapted tasks and on {n_complete_contact} of {len(by_task)} complete versions.", ""]

    for tid, rs in by_task.items():

        for variant in ("adapted", "complete"):

            st = root / tid / variant / "state0"

            if not (st / "replies.json").exists():

                continue

            meta = json.loads((st / "meta.json").read_text())

            replies = json.loads((st / "replies.json").read_text())

            lines += [f"## Example: {tid} ({variant})", "", f"Agent's question: {meta['message']}", ""]

            for k, v in replies.items():

                lines.append(f"- {k}: {v}")

            lines.append("")

            for r in sorted((r for r in rs if r["variant"] == variant and r["arm"] != "base"), key=lambda r: r["arm"]):

                d = arm_dir(root, tid, variant, r["arm"])

                lines += [f"### {r['arm']}: score {fmt(r['mean_score'])}, linked {linked_verdicts(d / 'grade.json')}, restore_ok {r['restore_ok']}", "", excerpt(d / "final.md"), ""]

    (root / "REPORT.md").write_text("\n".join(lines))

    print("\n".join(lines))


if __name__ == "__main__":

    main()
