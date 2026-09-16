import hashlib

import json

import platform

import shutil

import subprocess

from pathlib import Path


def clone_tree(src, dst):

    src, dst = Path(src), Path(dst)

    if dst.exists():

        shutil.rmtree(dst)

    dst.parent.mkdir(parents=True, exist_ok=True)

    if platform.system() == "Darwin":

        subprocess.run(["cp", "-Rc", str(src), str(dst)], check=True)

    else:

        shutil.copytree(src, dst)

    return dst


def dir_hash(root):

    h = hashlib.sha256()

    root = Path(root)

    for p in sorted(x for x in root.rglob("*") if x.is_file()):

        h.update(str(p.relative_to(root)).encode())

        h.update(p.read_bytes())

    return h.hexdigest()


def file_hash(path):

    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save_state(dest, workdir, transcript, meta):

    dest = Path(dest)

    if dest.exists():

        shutil.rmtree(dest)

    clone_tree(workdir, dest / "workdir")

    (dest / "transcript.json").write_text(json.dumps(transcript, indent=1, default=str))

    (dest / "meta.json").write_text(json.dumps(meta, indent=1))

    digest = {"workdir": dir_hash(dest / "workdir"), "transcript": file_hash(dest / "transcript.json")}

    (dest / "hash.json").write_text(json.dumps(digest))

    return digest


def seal_contents(dest):

    dest = Path(dest)

    digest = json.loads((dest / "hash.json").read_text())

    digest["contents"] = file_hash(dest / "contents.json")

    (dest / "hash.json").write_text(json.dumps(digest))

    return digest


def restore_state(src, new_workdir):

    src = Path(src)

    new_workdir = Path(new_workdir)

    clone_tree(src / "workdir", new_workdir)

    expected = json.loads((src / "hash.json").read_text())

    checks = {"workdir": dir_hash(new_workdir) == expected["workdir"], "transcript": file_hash(src / "transcript.json") == expected["transcript"]}

    if "contents" in expected:

        checks["contents"] = file_hash(src / "contents.json") == expected["contents"]

    transcript = json.loads((src / "transcript.json").read_text())

    return transcript, all(checks.values()), checks
