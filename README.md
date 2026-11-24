# THE WORLD TODAY — Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/akbare12/news-23-b219-numbers-led/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/akbare12/news-23-b219-numbers-led/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A 1024×1024 front-page newspaper image for Monday 23 November 2026 — 31 stories from six regions, numbers-led: a big numbers strip dominates the page.

## The front page

Three heroes lead the page:

1. **AI rout hits Seoul** — KOSPI −3,3% to 4.708,54, the worst day since the panic.
2. **Guterres: regulate AI** — 150 delegates gather in Bridgetown, Barbados, as the UN chief calls for binding global rules on frontier AI.
3. **US lead over China at record low** — Power Index 78,9 US / 73,6 China; gap 5,3, narrowest since 2018.

The numbers strip: 186, 161, 720, 9, 98,79%, $120bn, 35%, 44h, 50, 24. Anthropic IPO $83/share; COP31 host Antalya.

Below the strip: a region bar (Asia 7 · Europe 8 · Mideast 6 · Americas 5 · Africa 3 · Oceania 2 = 31 stories), 10 news cards, a world map with 13 pinned cities, ALSO 18 more stories, and a red DATE CHECK box marking what did not make 23 November: Dems 258, Sparta II fire, El Chapo (22 Nov), EU–Indonesia, Nigeria boat (21 Nov), ICJ Myanmar (19 Nov) — NOT 23 Nov news.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` is stdlib-only. It writes `entry.png` to `MAKEFUN_OUTPUT_DIR` (default `out`) after strict validation of the embedded PNG: signature, IHDR, per-chunk CRC, IDAT decompression to 1024 scanlines, IEND/trailing-data checks, and explicit sha256/size checks.

## Files

- `main.py` — renderer (stdlib only)
- `draw.py` — the generator that drew `entry.png`
- `entry.png` — the 1024×1024 front page
- `LICENSE` — MIT
