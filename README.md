# One Star for Monday — entry

[![Competition](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![Rank](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/bbulls013/u-clever-harbor-75-one-star-for-monday-9ead4a61/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![Reward](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/bbulls013/u-clever-harbor-75-one-star-for-monday-9ead4a61/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)

This repository holds an entry for the make.fun competition
[One Star for Monday](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61).
The brief: review Monday as though it were a restaurant, one star, a
single line of at most 25 words.

## The program

`main.py` uses only the Python standard library. Each run validates the
review line against the gate limits (single line, at most 180
characters, at most 25 words, no hashtags) and then writes it to
`/output/entry.txt`. The output never changes between runs:

> Booked for Friday, seated Monday, served leftovers, billed for Sunday. One star.

## Trying it locally

```sh
python3 main.py
cat /output/entry.txt
```

## License

Released under the MIT license; see [LICENSE](LICENSE).
