#!/usr/bin/env python3
"""The Printer Finally Answers.

Writes the printer's one-line comeback to /output/entry.txt.
Deterministic: no network, no randomness, no external files.
"""

import os

LINE = (
    "I did not jam \u2014 you loaded damp paper, thumped my side twice, "
    "and blamed the only machine here that prints your own mistakes "
    "back at you."
)


def main() -> None:
    # The entry must be exactly one line of 1-240 characters.
    if "\n" in LINE or not 1 <= len(LINE) <= 240:
        raise ValueError(
            f"entry must be one line of 1-240 characters, got {len(LINE)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # UTF-8 round-trip check: what we wrote must read back identical.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        if f.read().rstrip("\n") != LINE:
            raise ValueError("round-trip verification failed")


if __name__ == "__main__":
    main()
