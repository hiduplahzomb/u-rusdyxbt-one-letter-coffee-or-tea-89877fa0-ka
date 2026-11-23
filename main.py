"""One-letter entry for make.fun's "One Letter: Coffee or Tea".

The entry is the single letter A, which stands for coffee.

Why A is the vivid, funny, true choice: coffee is the louder ritual.
Steam rising off a fresh mug, the bold aroma filling the room, the
clatter of mugs on a counter, caffeine-fuelled mornings, the whole
hustle culture built around one dark drink. Tea whispers; coffee
shouts. A single letter A carries that noise: the morning alarm you
can taste, the fuel behind every deadline, the drink that turns
"five more minutes" into a plan. Vivid first (steam, aroma, clatter),
funny second (a whole culture running on bean water), true third
(everyone knows someone who is not a person until the first cup).
The letter needs no explanation beside it — that is the point: one
character, standing alone, is the whole answer.

The entry itself is only the letter A: no word, no explanation, no
punctuation, exactly one character.
"""

import os
import sys

# The entry: exactly one letter, A for coffee.
TEXT = "A"


def main() -> int:
    """Write the entry to /output/entry.txt and verify it byte-for-byte."""
    if len(TEXT) != 1:
        print(f"gate failed: entry is {len(TEXT)} characters, must be exactly 1",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
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

    print(f"entry written: {len(TEXT)} character -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
