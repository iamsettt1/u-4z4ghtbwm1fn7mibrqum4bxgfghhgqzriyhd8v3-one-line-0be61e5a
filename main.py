#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt.

Deterministic, stdlib only, no network, no randomness, no reads
outside this repository.
"""

import os

LINE = "I asked AI to write my wedding vows; it filed for divorce on my behalf."


def main() -> None:
    # Guard the gate: 1-140 chars, one line, non-blank.
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    assert "\n" not in LINE and LINE.strip(), "line must be a single non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
