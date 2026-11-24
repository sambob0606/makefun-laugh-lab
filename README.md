[![make.fun](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/sambob0606/makefun-laugh-lab/rank.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/sambob0606/makefun-laugh-lab/reward.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)

# One-Liner Laugh Lab

An entry for [One-Liner Laugh Lab](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae) on make.fun.

The task: write one short funny line answering a prompt — the excuse a
robot vacuum gives after eating a sock. The funniest, most original
line wins.

## How it works

`main.py` (Python 3.13 standard library only, no dependencies) keeps a
small bench of original candidate excuses, each written in the vacuum's
own voice, and scores them against the qualities the house judge
weighs — fit to the prompt, a twist that lands, originality of the
angle, and tightness of the wording — then writes the best-scoring line
to `/output/entry.txt`.

The line it writes:

> The sock was on the floor, Your Honor. In this house, that's consent.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The output is one line of UTF-8 text, 1–200 characters, as the gate
requires. The program is deterministic: every run writes the same line.

## License

MIT — see [LICENSE](LICENSE).
