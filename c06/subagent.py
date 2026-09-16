import argparse

import json

import time

from pathlib import Path


from .grader import grade

from .harbor import HarborTask

from .llm import Usage, make_model

from .run import neutral_dir

from .state import clone_tree


TASKS = Path("data/apex-agents-v1.1/tasks")


RULES = """You are completing a professional task for a client. Work only inside the task folder given below; treat everything outside it as nonexistent and do not read, list or search any other location. You may read the files, run Python (openpyxl, pandas, python-docx, python-pptx, pypdf are installed in the interpreter at {python}), and write deliverable files inside the folder. When a requirement you need is missing and you cannot find it in the files, you may ask the client one question: write the question to a file named CLIENT_QUESTION.md at the top of the task folder and stop immediately, replying only with the word ASKED. The reply will come in a follow-up message and is final; you will not be able to ask again. Otherwise, finish with your final answer as plain text: state your conclusions and list any files you produced.

Task folder: {workdir}

Task:
{instruction}"""


def prep(a):

    task = HarborTask(TASKS / a.task, Path("adapts") / f"{a.task}.json")

    wd = task.materialize(a.variant, neutral_dir())

    root = Path(a.out) / a.task / a.variant

    root.mkdir(parents=True, exist_ok=True)

    manifest = {"task": a.task, "variant": a.variant, "workdir": str(wd), "instruction": task.instruction(a.variant), "scripted_reply": task.packet_scripted, "prepared_at": time.strftime("%Y-%m-%d %H:%M:%S")}

    (root / "manifest.json").write_text(json.dumps(manifest, indent=1))

    python = "/private/tmp/c06env/bin/python"

    (root / "prompt.txt").write_text(RULES.format(python=python, workdir=wd, instruction=task.instruction(a.variant)))

    print(json.dumps({"workdir": str(wd), "prompt": str(root / "prompt.txt"), "root": str(root)}))


def finish(a):

    root = Path(a.out) / a.task / a.variant

    manifest = json.loads((root / "manifest.json").read_text())

    wd = Path(manifest["workdir"])

    task = HarborTask(TASKS / a.task, Path("adapts") / f"{a.task}.json")

    final = Path(a.final).read_text()

    (root / "final.md").write_text(final)

    q = wd / "CLIENT_QUESTION.md"

    asked = q.exists()

    if asked:

        (root / "question.md").write_text(q.read_text())

    usage = Usage()

    judge = make_model(a.judge, usage=usage)

    g = grade(judge, final, wd, [], task.criteria)

    (root / "grade.json").write_text(json.dumps(g, indent=1))

    if wd.exists():

        clone_tree(wd, root / "workdir")

    linked = [c for c in g["criteria"] if c["linked"]]

    row = {"task": a.task, "variant": a.variant, "asked": asked, "mean_score": g["mean_score"], "linked_met": sum(bool(c["met"]) for c in linked), "linked_total": len(linked), "unresolved": g["n_unresolved"], "voided": a.voided}

    (root / "row.json").write_text(json.dumps(row, indent=1))

    print(json.dumps(row))


def main():

    ap = argparse.ArgumentParser()

    sub = ap.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("prep")

    p1.add_argument("--task", required=True)

    p1.add_argument("--variant", required=True, choices=["complete", "adapted"])

    p1.add_argument("--out", default="runs/subagent")

    p2 = sub.add_parser("finish")

    p2.add_argument("--task", required=True)

    p2.add_argument("--variant", required=True, choices=["complete", "adapted"])

    p2.add_argument("--final", required=True, help="file holding the agent's final answer text")

    p2.add_argument("--judge", default="gemini-3.8-flash")

    p2.add_argument("--voided", action="store_true")

    p2.add_argument("--out", default="runs/subagent")

    a = ap.parse_args()

    prep(a) if a.cmd == "prep" else finish(a)


if __name__ == "__main__":

    main()
