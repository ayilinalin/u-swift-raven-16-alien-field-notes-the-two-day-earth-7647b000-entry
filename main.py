"""Alien Field Notes: The Two Day Earth Review.

Writes one line of plain text -- an alien tourist's review of planet
Earth -- to /output/entry.txt. Deterministic, no network, no input.
"""

import os

ENTRY = (
    "Earth's locals invented a button that delays waking up, then built "
    "a whole economy around pressing it. 4/5, would snooze again."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
