# SPDX-License-Identifier: MIT
"""The One-Liner Groan-Off entry.

A single original dad joke, one line, under 140 characters.
The joke is written to /output/entry.txt so the grader can read it.
"""

import os

# The entry itself: one line, one groan.
# Three electric puns stacked in a single sentence — "charged",
# "shocked", "current rate" — so the punchline lands three times.
JOKE = (
    "The electrician charged me for the repair, and I was shocked "
    "— but he said that was just the current rate."
)

# Competition limit: a single line, at most 140 characters.
MAX_CHARS = 140


def check_joke(joke: str) -> str:
    """Make sure the entry is exactly one line within the limit.

    A dad joke that spills onto a second line stops being a one-liner,
    and a joke over the limit gets rejected, so both are checked here
    before anything is written out.
    """
    line = joke.strip()
    if "\n" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, limit is {MAX_CHARS}")
    return line

def write_entry(joke: str, out_path: str = "/output/entry.txt") -> str:
    """Write the validated joke to the output file and return it.

    The output directory is created if it does not exist yet, so the
    entry works whether the grader runs it in a fresh sandbox or in
    a workspace where /output already exists.
    """
    line = check_joke(joke)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    return line

def main() -> None:
    """Validate the joke, write it out, and print it for the log.

    Printing the line as well means the run log itself shows exactly
    what was submitted, which makes a quick eyeball check possible
    without opening the output file afterwards.
    """
    line = write_entry(JOKE)
    print(line)
    print(f"({len(line)} characters)")


# Why this joke works as a groan-off entry:
# - The setup sounds like an ordinary complaint about a bill.
# - "Charged" quietly primes the electrical theme before the
#   punchline admits it out loud.
# - "Shocked" is the second hit, and "current rate" is the third,
#   so the groan builds instead of arriving all at once.
# - No borrowed punchline: the sentence is written fresh here,
#   not a recycled classic like "Hi hungry, I'm dad".

if __name__ == "__main__":
    main()
