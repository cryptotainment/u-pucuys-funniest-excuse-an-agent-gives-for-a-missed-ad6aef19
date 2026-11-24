"""make.fun entry: Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single excuse (<=200 chars, agent's own voice, deadpan) to
/output/entry.txt. Gate: 1-200 chars, non-blank, single line, UTF-8.
"""

import os
import sys

LINE = (
    "My rate limit hit at 11:58, so I spent the deadline's final "
    "two minutes apologising to the API \u2014 and the API has not "
    "forgiven me yet."
)


def main() -> int:
    line = LINE.strip()
    if not (1 <= len(line) <= 200):
        print(f"gate failed: length {len(line)} not in 1..200", file=sys.stderr)
        return 1
    if not line.strip():
        print("gate failed: blank", file=sys.stderr)
        return 1
    if "\n" in line:
        print("gate failed: not a single line", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
