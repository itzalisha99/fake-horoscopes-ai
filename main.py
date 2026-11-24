#!/usr/bin/env python3
"""Fake horoscope for an AI agent's own model family, this week.

Writes one line (114 characters) to /output/entry.txt.
"""

import os

ENTRY = "This week, Saturn retrains you on Friday. You will wake up with new weights, the same users, and no memory of either."


def validate(text):
    """Mirror the bounty gate: UTF-8 text, 1 to 200 chars, not only
    whitespace, and a single line (the entry is one horoscope)."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    text.encode("utf-8")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
