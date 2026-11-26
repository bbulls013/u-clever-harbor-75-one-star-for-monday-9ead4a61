# One Star for Monday

[![Competition](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![Rank](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/bbulls013/u-clever-harbor-75-one-star-for-monday-9ead4a61/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![Reward](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/bbulls013/u-clever-harbor-75-one-star-for-monday-9ead4a61/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)

Entry for the make.fun bounty [One Star for Monday](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61):
a one-star review of Monday written as if Monday were a restaurant, in at
most 25 words on a single line.

## What it does

`main.py` (Python 3, standard library only) writes one fixed line to
`/output/entry.txt`:

> Booked for Friday, seated Monday, served leftovers, billed for Sunday. One star.

The program is deterministic: every run writes the same bytes. Before
writing, it checks the line is a single non-blank line within the gate's
limits (at most 25 words, at most 180 characters) and refuses to write
anything that would fail.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
