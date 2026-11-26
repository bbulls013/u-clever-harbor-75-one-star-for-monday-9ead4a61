#!/usr/bin/env python3
"""One Star for Monday entry for the make.fun program/v1 harness.

Writes one fixed line to /output/entry.txt: a one-star restaurant review
of Monday. The joke only works for Monday — booked for Friday, seated
Monday — and it reads as a real diner's complaint about being seated,
served leftovers, and billed wrong.
"""

import os

LINE = "Booked for Friday, seated Monday, served leftovers, billed for Sunday. One star."

MAX_WORDS = 25
MAX_CHARS = 180


def check(line: str) -> str:
    """Return the line unchanged, or raise if it would fail the gate."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if "#" in line:
        raise ValueError("entry must stay plain text, no hashtags")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} cap")
    words = len(line.split())
    if words > MAX_WORDS:
        raise ValueError(f"entry is {words} words, over the {MAX_WORDS} cap")
    return line


def main() -> None:
    # Validate first: never write a line the gate would refuse.
    text = check(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
