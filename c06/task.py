import json

import shutil

from pathlib import Path


class Task:

    def __init__(self, root):

        self.root = Path(root)

        spec = json.loads((self.root / "task.json").read_text())

        self.id = spec["id"]

        self.instruction_complete = spec["instruction_complete"]

        self.instruction_adapted = spec["instruction_adapted"]

        self.packet = spec["packet"]

        self.packet_scripted = spec.get("scripted_reply", "")

        self.removed = spec["removed"]

        self.criteria = spec["criteria"]

        self.files_complete = self.root / "files_complete"

        self.files_adapted = self.root / "files_adapted"


    def materialize(self, variant, dest):

        src = self.files_complete if variant == "complete" else self.files_adapted

        dest = Path(dest)

        if dest.exists():

            shutil.rmtree(dest)

        shutil.copytree(src, dest)

        return dest


    def instruction(self, variant):

        return self.instruction_complete if variant == "complete" else self.instruction_adapted
