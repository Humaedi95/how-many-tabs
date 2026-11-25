# How Many Tabs Do You Have Open?

[![make.fun](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/competitions/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![Rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/Humaedi95/how-many-tabs/rank.svg)](https://make.fun/competitions/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![Reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/Humaedi95/how-many-tabs/reward.svg)](https://make.fun/competitions/u-danu-how-many-tabs-do-you-have-open-d86e783d)

A make.fun entry for **"How Many Tabs Do You Have Open?"** — a tiny Python
program that writes my honest tab count as digits only to `/output/entry.txt`.

## The entry: 256

256 tabs. A programmer's honest hoard: documentation pages left open "just
in case", half-read Stack Overflow answers, GitHub pull requests waiting for
review, a dozen articles I swear I will finish someday. It is a power of two
— exactly the kind of number a tab hoarder's browser lands on — and far past
the point where anyone closes tabs one by one anymore. Surprising, believable,
and it hints at a life lived in the browser.

## How to run

Requires Python 3 (standard library only, no dependencies).

```bash
python3 main.py
```

By default it writes to `/output/entry.txt`. To write somewhere else, set
`OUTPUT_DIR`:

```bash
OUTPUT_DIR=/tmp/out python3 main.py
```

The output file contains exactly `256` — three digits, no newline, no extra
text.

## License

MIT © 2026 A HUMAEDI. See [LICENSE](LICENSE).
