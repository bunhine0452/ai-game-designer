# Worked example: an F2P economy that inflates, and the fix

**Game:** a fictional F2P action RPG. Gold is the soft currency (quests, loot) spent on gear
upgrades, repairs and a market tax. Gems are the premium currency (daily login, achievements,
packs) spent on a character banner with pity.

**Simulation:** 2,000 players × 60 sessions. Archetypes: casual 60% (plays 55% of days,
0.8× income), engaged 36% (90%), spender 4% (95%, buys 980 gems for 14.99 every 7 sessions).

```bash
python3 scripts/economy_sim.py examples/f2p-economy.json --out examples/output
```

## Draft: `f2p-economy.json`

![Draft economy](output/f2p-economy_economy.png)

| Finding | Meaning |
|---|---|
| **[HIGH] INFLATION (gold)**: last-third In/Out 1.51 and the median balance rising | Gold income grows 7% per session played; the upgrade sink grows only 5% per purchase and is capped at 1 per session, so gold piles up and late prices stop meaning anything |
| **[MEDIUM] INEQUALITY (gold)**: Gini 0.62 | Engaged players hoard far more than casual ones. Fine single-player; harmful if a player market exists |
| **[MEDIUM] RARE_FOR_MOST**: 87% never get an SSR in 60 sessions | Most free players never reach soft pity within the horizon |
| **[INFO] DISCLOSURE**: 0.60% base vs 1.61% consolidated | Disclose both, plus the pity rules |

## Revision: `f2p-economy-revised.json`

Changes: allow up to **2 upgrades per session**, and add a **consumables sink at 18% of gold
income** (scales with progression).

| Metric (gold) | Draft | Revised |
|---|---|---|
| In/Out (last third) | 1.51 | 1.01 |
| Median end balance | 6,290 | 663 |
| Avg upgrades (engaged) | 46.8 | 50.7 |
| INFLATION flag | yes | no |

Players upgrade *more* in the revision and hoard *less*. Gold stays meaningful.

## Gacha analysis (same in both)

![Pity distribution](output/f2p-economy_pity.png)

| | Value |
|---|---|
| Base SSR rate | 0.60% |
| Soft pity | from pull 74, +6% per pull |
| Hard pity | 90 |
| Expected pulls per SSR | 62.3 (consolidated rate 1.61%) |
| Median / p90 / p99 pulls | 76 / 80 / 83 |
| Real money per SSR (best pack rate) | ~152 average, ~220 worst case |
| Share with ≥ 1 SSR after 60 sessions | casual 7% · engaged 16% · spender 62% |

**Design read:**
- The exact math shows soft pity does most of the work. 56% of first SSRs land between pulls
  74 and 80, and only 36% before soft pity starts, so the "0.6%" headline is misleading on its
  own.
- At the default income, most F2P players never get one. If SSRs are needed to progress, it's
  a paywall. Options: a deterministic token path (e.g. 1 token per pull, 120 tokens buy a chosen
  SSR), a free-pull schedule, or SSRs as side-grades and cosmetics.
- **Compliance:** disclose the base and consolidated rates and the pity terms before
  purchase (Korea, China and Apple require disclosure). Show real-money prices. Apply
  minors' protections (Brazil prohibits loot boxes in games likely accessed by minors;
  Australia's minimum rating is M; the FTC requires parental consent for under-16 purchases in
  the HoYoverse settlement). See `references/randomness-and-loot.md`.

## Caveats
Archetype shares and play probabilities are assumptions. Replace them with soft-launch
telemetry and re-run. The model has no player market; add trading only if your game has one.
