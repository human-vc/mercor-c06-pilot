import os

import sys


BLOCKED_EVENT_PREFIXES = ("subprocess.", "socket.", "ctypes.", "os.exec", "os.posix_spawn", "os.fork", "os.spawn", "os.system", "os.kill", "webbrowser.", "pty.", "signal.")

BLOCKED_MODULES = {"multiprocessing", "pty", "webbrowser"}

SYSTEM_PREFIXES = ["/System", "/usr", "/Library", "/private/etc", "/etc", "/dev", "/private/var/db", "/var/db", "/opt"]


def _norm(p):

    if isinstance(p, bytes):

        p = os.fsdecode(p)

    if not isinstance(p, str):

        return None

    return os.path.realpath(os.path.abspath(p))


def make_hook(workdir, allowed_prefixes):

    workdir = os.path.realpath(workdir)


    def inside(path, root):

        return path == root or path.startswith(root + os.sep)


    def allowed(path):

        if inside(path, workdir):

            return True

        return any(inside(path, pre) for pre in allowed_prefixes)


    def hook(event, args):

        if event == "ctypes.dlopen" and args and args[0] is None:

            return

        if event.startswith(BLOCKED_EVENT_PREFIXES):

            raise RuntimeError(f"sandbox: {event} is not permitted")

        if event == "import":

            name = args[0] if args else ""

            if name.split(".")[0] in BLOCKED_MODULES:

                raise RuntimeError(f"sandbox: import of {name} is not permitted")

            return

        if event == "os.chdir":

            p = _norm(args[0]) if args else None

            if p is None or not inside(p, workdir):

                raise RuntimeError("sandbox: cannot leave the task folder")

            return

        if event == "open" or event.startswith(("os.", "shutil.", "glob.", "pathlib.", "tempfile.")):

            for a in args:

                p = _norm(a)

                if p is not None and os.sep in p and not allowed(p):

                    raise RuntimeError(f"sandbox: access outside the task folder is not permitted ({a})")


    return hook


def main():

    workdir = os.path.realpath(sys.argv[1])

    code = sys.stdin.read()

    allowed_prefixes = [os.path.realpath(p) for p in (sys.prefix, sys.base_prefix, sys.exec_prefix, sys.base_exec_prefix) if p]

    allowed_prefixes += [os.path.realpath(p) for p in SYSTEM_PREFIXES]

    os.chdir(workdir)

    sys.addaudithook(make_hook(workdir, allowed_prefixes))

    g = {"__name__": "__main__", "__file__": os.path.join(workdir, "script.py")}

    exec(compile(code, "script.py", "exec"), g)


if __name__ == "__main__":

    main()
