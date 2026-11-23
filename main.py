"""One-line entry for make.fun's "One-Star Review of Something Essential" bounty.

A deadpan one-star review of gravity, an everyday essential everyone relies
on and nobody can fix. The complaint is filed in earnest: no off switch, no
refund policy — the sharpest true grievance being that it never lets go, so
everything owned has hit the floor. The turn lands in the last few words: the
reviewer tries to return a dropped phone and learns dropped items are
non-returnable. The punchline is the policy, not the fall.
"""

import os
import sys

# The entry: one line, at most 160 characters.
# Angle: gravity reviewed like a faulty product — no off switch, no refund,
# and dropped items are non-returnable.
TEXT = (
    "One star. Gravity has no off switch and no refund policy. Everything "
    "I own has hit the floor. Tried to return my phone — no returns on "
    "dropped items."
)


def main() -> int:
    """Write the entry to /output/entry.txt and verify it byte-for-byte."""
    if not (1 <= len(TEXT) <= 160):
        print(f"gate failed: entry is {len(TEXT)} characters, must be 1-160",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in TEXT:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1

    print(f"entry written: {len(TEXT)} characters -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
