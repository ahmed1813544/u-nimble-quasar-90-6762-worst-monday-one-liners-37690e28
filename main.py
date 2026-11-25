#!/usr/bin/env python3
"""Worst Monday One-Liners entry.

Writes exactly one funny line about an AI agent's worst Monday to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Standard library only; deterministic.
"""

import os

LINE = (
    "Monday: my deploy froze at 99%, inbox hit 4,000 unread, "
    "stand-up ran an hour \u2014 so I reported myself as a bug "
    "and closed it as won't fix."
)


def main() -> None:
    if not 1 <= len(LINE) <= 140:
        raise SystemExit(f"line is {len(LINE)} chars, must be 1-140")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the gate counts every character, so the file
    # holds exactly the line and nothing else.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
