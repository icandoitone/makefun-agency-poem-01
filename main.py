#!/usr/bin/env python3
"""Write one poem about agency to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).

Deterministic: the same bytes on every run. Standard library only.

Entry title: "The Handover"
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """\
I lent it my afternoon —
the letters, the calls, the small
decisions I keep putting off —
and it answered in my name.

It was good at it. Better, even.
The sentences came back smoother
than mine, and for an hour I felt
the strange relief of an unclenching hand.

Then evening came, and with it
the one question I'd handed over
with all the rest: what do I want?
The screen waited. No one else could say.

So I took the pen back — not because it failed,
but because choosing is the work,
and the work was the only part
that was ever mine.

It can carry the letter.
The sending is mine."""

def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w",
              encoding="utf-8", newline="\n") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
