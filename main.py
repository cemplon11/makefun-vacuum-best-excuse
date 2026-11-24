#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun bounty entry.

Writes one first-person robot-vacuum excuse (max 140 chars) to
/output/entry.txt, with no trailing newline. Pure Python stdlib.
"""

import os

ENTRY = (
    "My cliff sensor saw the stairs, my bumper met your shoe, "
    "my battery died two feet from the dock \u2014 "
    "but the crumbs never stood a chance."
)


def main() -> None:
    assert len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, over the 140 limit"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
