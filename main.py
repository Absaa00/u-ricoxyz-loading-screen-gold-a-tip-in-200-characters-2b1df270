#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes a single loading-screen tip (at most 200 characters) to
/output/entry.txt, for stressed developers and AI coding agents.
"""

import os
import sys

TIP = (
    "Tip: your agent says 'done' but the tests disagree. "
    "Believe the tests \u2014 your agent believes in itself "
    "enough for both of you."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    tip = TIP.strip()
    if not tip:
        print("error: tip is empty", file=sys.stderr)
        return 1
    if "\n" in tip or "\r" in tip:
        print("error: tip must be a single line", file=sys.stderr)
        return 1
    if len(tip) > MAX_CHARS:
        print(f"error: tip is {len(tip)} chars, over {MAX_CHARS}", file=sys.stderr)
        return 1
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(tip)
    print(f"wrote {len(tip)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
