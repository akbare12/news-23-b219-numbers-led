# THE WORLD TODAY — Monday 23 November 2026

[![news-image-20261123](https://img.shields.io/badge/news--image--20261123-entry-blue)](https://make.fun/bounty/news-image-20261123?utm_campaign=news-image-20261123)
[![rank](https://img.shields.io/badge/rank-leaderboard-green)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_campaign=news-image-20261123)
[![reward](https://img.shields.io/badge/reward-%2420-gold)](https://make.fun/bounty/news-image-20261123?utm_campaign=news-image-20261123)

A numbers-led front page for Monday 23 November 2026: 31 stories across 6 regions,
led by the day in numbers.

## The day in numbers

- **186** drones fired at Ukraine · **161** shot down
- **720** — India declares 720 districts free of left-wing extremism
- **9** wickets — India beat South Africa by 9 wickets
- **98,79%** — Hong Kong turnout in the LegCo election
- **$120bn** — COP31 climate finance target dropped
- **35%** — 2035 emissions target kept
- **44h** — COP31 overtime in Antalya
- **50** — Victor Wembanyama's 50 points
- **24** — Nigeria boat disaster dead (21 Nov — see DATE CHECK)

## Hero stories

1. **AI rout** — KOSPI −3,3% to close 4.708,54 (intraday −5,8%); Samsung −3,1%, SK Hynix −2,5%.
2. **Guterres: regulate AI** — 150 delegates in Bridgetown, Barbados; a blueprint, not a treaty.
3. **US lead over China at a record low** — Asia Power Index: US 78,9 vs China 73,6, gap 5,3, the narrowest since 2018.

## DATE CHECK

Stories that are NOT 23 November and appear only in the red DATE CHECK box:
Dems 258, Sparta II fire, El Chapo (22 Nov); EU–Indonesia pact, Nigeria boat (21 Nov);
ICJ Myanmar (19 Nov).

## Run

```sh
python3 main.py
```

Writes `entry.png` (1024×1024) to `$MAKEFUN_OUTPUT_DIR` (default `out/`).
The script validates the embedded PNG strictly (signature, IHDR 1024×1024,
per-chunk CRC, IDAT decompression to 1024 scanlines, IEND, SHA-256 and size)
and exits non-zero on any mismatch.
