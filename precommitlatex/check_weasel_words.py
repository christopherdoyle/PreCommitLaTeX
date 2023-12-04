import argparse
from pathlib import Path
from typing import Dict, List, Sequence

from . import DIRECTORY


def count_occurences(text: str, substrings: List[str]) -> Dict[str, int]:
    result = {}
    for substring in substrings:
        result[substring] = text.count(substring)
    return result


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", type=Path)
    args = parser.parse_args(argv)
    filenames: List[Path] = args.filenames

    weasel_words = (DIRECTORY / "weasel-words.txt").read_text().splitlines()

    retval = 0
    for filename in filenames:
        data = filename.read_text()
        counts = count_occurences(data, weasel_words)
        max_val = max(counts.values())
        if max_val > 0:
            summary = "; ".join(
                f"{word}={count}" for word, count in counts.items() if count > 0
            )
            print(f"{filename}: Weasel words founds {summary}")
            retval = 1
    return retval


if __name__ == "__main__":
    raise SystemExit(main())
