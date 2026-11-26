#!/usr/bin/env python3
"""Entrypoint for the One Star for Monday bounty (program/v1).

The harness runs this file; it must leave the entry text at
/output/entry.txt. The text is a one-star restaurant review of Monday:
the reservation was for Friday, the seating happened on Monday, the
kitchen sent out leftovers, and the bill charged for Sunday.
"""

from pathlib import Path

REVIEW = "Booked for Friday, seated Monday, served leftovers, billed for Sunday. One star."
WORD_LIMIT = 25
CHAR_LIMIT = 180
TARGET = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Raise ValueError when text breaks the bounty gate."""
    if text != text.strip() or not text:
        raise ValueError("blank or padded text")
    if "\n" in text:
        raise ValueError("more than one line")
    if len(text) > CHAR_LIMIT:
        raise ValueError("over the character limit")
    if len(text.split()) > WORD_LIMIT:
        raise ValueError("over the word limit")
    if "#" in text:
        raise ValueError("hashtags are not plain text")


def run() -> None:
    # Gate first, write second: an invalid line never reaches the file.
    validate(REVIEW)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(REVIEW + "\n", encoding="utf-8")


if __name__ == "__main__":
    run()
