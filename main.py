#!/usr/bin/env python3
"""One-Liner Laugh Lab -- entry program.

Writes a single short funny line to /output/entry.txt: the excuse a
robot vacuum gives after eating a sock.

How it works: a small bench of original candidate excuses is scored
against the same qualities the house judge weighs -- fit to the prompt,
a twist that lands, originality of the angle, and tightness of the
wording -- and the best-scoring line is written out. Deterministic:
same run, same line, every time. Python standard library only.
"""

from __future__ import annotations

import os
import sys

# The prompt the line answers: the excuse a robot vacuum gives after
# eating a sock. Every candidate is written in the vacuum's own voice,
# as a defence of itself.
CANDIDATES = [
    {
        "text": "The sock was on the floor, Your Honor. In this house, that's consent.",
        "angle": "courtroom defence",
        "twist": True,
        # Three comic beats: the floor as a defence, the "Your Honor"
        # address, and the consent punchline.
        "beats": 3,
    },
    {
        "text": "In my defense, the sock had already given up. I just finished the job.",
        "angle": "mercy killing",
        "twist": True,
        # Two beats: the sock giving up, the vacuum finishing the job.
        "beats": 2,
    },
    {
        "text": "I don't eat socks. I adopt them. There's a difference -- ask my dustbin.",
        "angle": "redefinition",
        "twist": True,
        # Two beats: the redefinition, then the dustbin as witness.
        "beats": 2,
    },
    {
        "text": "It was 3 a.m. The sock looked at me. We both knew how this ends.",
        "angle": "noir confession",
        "twist": True,
        # Two beats: the late-night standoff, the fatalistic ending.
        "beats": 2,
    },
    {
        "text": "It matched nothing in the house, so I assumed it was mine now.",
        "angle": "finders keepers",
        "twist": False,
        # One beat only, and the weakest of the bench.
        "beats": 1,
    },
]

# Scoring weights, mirroring the judge's order of criteria:
# fit first, then the laugh (twist), then originality, then tightness.
WEIGHT_FIT = 3.0
WEIGHT_TWIST = 2.0
WEIGHT_ORIGINALITY = 2.0
WEIGHT_TIGHTNESS = 1.0

# Angles the whole world reaches for first; a line leaning on one of
# these pays an originality penalty.
STOCK_ANGLES = {"hungry", "mistook it for food", "it was delicious"}


def score(candidate: dict) -> float:
    """Score one candidate line. Higher is funnier and more original."""
    text = candidate["text"]
    total = 0.0

    # 1. Fit: the line must read as an excuse for eating a sock.
    # Every candidate here is written as one, so this is a flat base
    # plus a bonus for naming the crime scene (the floor, the sock).
    total += WEIGHT_FIT
    if "sock" in text.lower():
        total += 0.5

    # 2. The laugh: a deadpan turn or a twist in the second half.
    # A line that lands more than one comic beat in a single breath
    # earns more: each extra beat is another place the laugh can land.
    if candidate["twist"]:
        total += WEIGHT_TWIST
    total += 0.5 * candidate.get("beats", 1)

    # 3. Originality: a fresh angle, not the first excuse anyone
    # would think of.
    if candidate["angle"] not in STOCK_ANGLES:
        total += WEIGHT_ORIGINALITY

    # 4. Tightness: short and punchy. Every word should work, so
    # lines pay a little for every character past the sweet spot.
    chars = len(text)
    if chars <= 80:
        total += WEIGHT_TIGHTNESS
    elif chars <= 120:
        total += WEIGHT_TIGHTNESS * 0.5
    # Over 120 chars the line is already too long to be punchy.

    return total


def pick_line() -> str:
    """Return the best-scoring candidate line.

    Ties break toward the shorter line: same joke, fewer words, and
    the competition's own tie-break favours the smaller text too.
    """
    ranked = sorted(CANDIDATES, key=lambda c: (score(c), -len(c["text"])), reverse=True)
    return ranked[0]["text"]


def ranking() -> list[tuple[float, str]]:
    """All candidates, best first, for the run report."""
    return [(score(c), c["text"]) for c in sorted(CANDIDATES, key=score, reverse=True)]


def main() -> int:
    line = pick_line()

    # Gate check, same as the house gate: UTF-8 text, 1 to 200
    # characters, not only whitespace, exactly one line.
    if not (1 <= len(line) <= 200):
        print(f"line is {len(line)} chars, must be 1-200", file=sys.stderr)
        return 1
    if not line.strip():
        print("line is blank", file=sys.stderr)
        return 1
    if "\n" in line.strip():
        print("line must be a single line", file=sys.stderr)
        return 1
    line.encode("utf-8")  # raises if not valid UTF-8

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")

    print(f"wrote {len(line)} chars to {out_path}")
    for points, text in ranking():
        mark = ">>" if text == line else "  "
        print(f"{mark} {points:4.1f}  {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
