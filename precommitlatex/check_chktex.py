import argparse
import subprocess
from pathlib import Path
from typing import List, Sequence


def do_chktex(filepath: Path) -> int:
    command = [
        "chktex",
        "-q",
        "-f",
        "%f %l: %m (column %c)\n",
        filepath,
    ]
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    proc.wait()
    if proc.returncode != 0:
        stdout, stderr = proc.communicate()
        if stdout:
            print(stdout)
        if stderr:
            print(stderr)
        return 1
    else:
        return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", type=Path)
    args = parser.parse_args(argv)
    filenames: List[Path] = args.filenames

    retval = 0
    for filename in filenames:
        if do_chktex(filename):
            retval = 1

    return retval


if __name__ == "__main__":
    raise SystemExit(main())
