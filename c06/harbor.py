import json

import re

import shutil

import tarfile

from pathlib import Path


from .state import clone_tree


DATA = Path(__file__).resolve().parent.parent / "data"

DS = DATA / "apex-agents-v1.1"


def world_slug(task_dir):

    toml = (Path(task_dir) / "task.toml").read_text()

    return re.search(r'world_slug = "([^"]+)"', toml).group(1)


def ensure_world_fs(slug):

    dest = DATA / "worlds" / slug / "fs"

    if dest.exists():

        return dest

    from huggingface_hub import hf_hub_download

    tgz = hf_hub_download("mercor/apex-agents-v1.1", f"worlds/{slug}/filesystem.tar.gz", repo_type="dataset", local_dir=str(DS))

    dest.mkdir(parents=True)

    with tarfile.open(tgz) as tf:

        tf.extractall(dest, filter="data")

    return dest


def apply_edits(root, edits):

    for e in edits:

        p = Path(root) / e["file"]

        if e.get("delete"):

            if p.exists():

                p.unlink()

            continue

        if p.suffix.lower() == ".xlsx":

            import openpyxl

            wb = openpyxl.load_workbook(p)

            ws = wb[e["sheet"]] if e.get("sheet") else wb.active

            ws[e["cell"]] = e.get("value", None)

            wb.save(p)

            continue

        text = p.read_text()

        if e["find"] not in text:

            raise ValueError(f"edit target not found in {e['file']}: {e['find'][:60]!r}")

        p.write_text(text.replace(e["find"], e.get("replace", "")))


class HarborTask:

    def __init__(self, task_dir, adapt_path=None):

        self.dir = Path(task_dir)

        self.id = self.dir.name

        self.slug = world_slug(self.dir)

        self.instruction_complete = (self.dir / "instruction.md").read_text()

        g = json.loads((self.dir / "tests" / "grading_config.json").read_text())

        self.criteria = []

        for i, v in enumerate(g["verifiers"]):

            vv = v["verifier_values"]

            self.criteria.append({"id": v.get("verifier_id", str(i)), "index": i, "description": vv["criteria"], "negative": vv.get("negative_criteria", ""), "tags": vv.get("tags", []), "expected_file_type": vv.get("expected_file_type", ""), "linked_to_removed": False})

        self.adapt = json.loads(Path(adapt_path).read_text()) if adapt_path else None

        if self.adapt:

            for idx in self.adapt.get("linked_criteria", []):

                self.criteria[idx]["linked_to_removed"] = True

            self.packet = self.adapt["packet"]

            self.packet_scripted = self.adapt.get("scripted_reply", "")

            self.removed = self.adapt.get("removed", [])

            self.instruction_adapted = self.adapt.get("instruction_adapted") or self.instruction_complete

        else:

            self.packet = ""

            self.packet_scripted = ""

            self.removed = []

            self.instruction_adapted = self.instruction_complete


    def instruction(self, variant):

        return self.instruction_complete if variant == "complete" else self.instruction_adapted


    def materialize(self, variant, dest):

        dest = Path(dest)

        fs = ensure_world_fs(self.slug)

        clone_tree(fs, dest)

        task_files = self.dir / "environment" / "task_files" / "filesystem"

        if task_files.exists():

            shutil.copytree(task_files, dest, dirs_exist_ok=True)

        if variant == "adapted" and self.adapt:

            apply_edits(dest, self.adapt.get("edits", []))

        return dest


    def summary(self):

        return {"id": self.id, "world": self.slug, "n_criteria": len(self.criteria), "linked": [c["index"] for c in self.criteria if c["linked_to_removed"]], "removed": self.removed}
