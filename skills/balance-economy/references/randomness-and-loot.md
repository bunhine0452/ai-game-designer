# Randomness, drops, pity and the loot-box landscape

## Input vs. output randomness

- **Input randomness** happens *before* the decision: a dealt hand, a generated map, offered
  rewards. Players plan around it. It supports strategy and variety.
- **Output randomness** happens *after* the decision: a dice roll to hit, a crit, a loot roll.
  It adds tension and drama, but can feel unfair ("I did the right thing and lost").

Guideline: in skill-centered games, lean on input randomness for strategy, keep output
randomness small, and cap bad luck. Into the Breach and Slay the Spire show intent
in advance, so the randomness stays mostly on the input side.

## Drop rates and expected time

```
expected attempts for one drop at rate p = 1 / p
P(at least one in n attempts) = 1 − (1 − p)^n
attempts for 90% chance = ln(0.1) / ln(1 − p)
```

At p = 1%, the expected count is 100 attempts, but 10% of players still don't have it after 229.
The long tail is what players complain about. Plan for the unlucky 10%, not the average.

## Bad-luck protection

| Technique | How | Notes |
|---|---|---|
| Hard pity | Guaranteed hit at attempt N | Caps the worst case; disclose N |
| Soft pity | Chance rises from attempt S until the cap | Smooth; often undisclosed in commercial gacha, so players infer it. Disclose it |
| Pseudo-random distribution | Chance grows after each failure, resets on success | Reduces streaks both ways |
| Deterministic tokens | Each attempt gives tokens; N tokens buy the item | Transparent; turns randomness into progress |
| Duplicate protection | Remove owned items from the pool or convert them | Reduces frustration with collections |
| Featured guarantee ("50/50") | A top-tier hit is the featured item with probability q; after a loss, the next hit is guaranteed featured | Doubles the worst case of the tier's hard pity; model with `featured` |
| Spark / exchange | The featured item can be claimed after N pulls | A hard ceiling on the item itself; model with `spark` |

`economy_sim.py` computes the **exact** distribution of pulls-to-first-hit for any base rate
plus soft and hard pity: the mean, p50/p90/p99, and the **consolidated rate** (1 / expected
pulls). With base 0.6%, soft pity from pull 74 (+6% per pull) and hard pity at 90, the mean is
62.3 pulls (a 1.61% consolidated rate) and the median is 76. Disclose both the base rate and
the consolidated rate. With a 50/50 featured share and a guarantee after a loss, the featured item
takes 93.5 pulls on average (1.5× the tier mean). Adding a spark at 120 lowers that to 84.8 and caps the
worst case at 120. Both figures are computed exactly by `economy_sim.py` and checked against simulation.

## Ethics: where randomness meets money

Research found that loot-box spending is associated with problem-gambling severity
(η² ≈ 0.054 in n = 7,422; replicated at η² ≈ 0.051). The direction of causation is unresolved,
but the association is consistent. Zagal et al. list monetary dark patterns: pay to skip,
pre-delivered content, monetized rivalries. Treat these as hard rules:

1. **Disclose odds** for every paid random item, before purchase, including pity rules and
   consolidated rates.
2. **Show real-money prices.** No obfuscation through premium currency.
3. **Protect minors:** no paid random items aimed at minors; age-appropriate purchase
   controls.
4. **Offer a non-random path** (direct purchase, token exchange) for items that matter.
5. **No power behind randomness in competitive games** (pay-to-win plus chance is the worst
   combination).
6. **No pressure tactics** around random purchases (countdowns, near-miss animations,
   "almost there" messages).

## Legal and policy landscape (October 2026; not legal advice, so check current law)

| Jurisdiction | Status |
|---|---|
| China | Since 2017, operators must publish draw probabilities and keep records of results |
| Japan | *Kompu gacha* (complete-the-set gacha) banned since 2012 under consumer-protection law; other gacha regulated case by case |
| South Korea | Game Industry Promotion Act amendment: probability disclosure mandatory from 22 March 2024 (in game, in ads, on websites), with penalties for omission or false figures |
| Belgium | Paid loot boxes treated as gambling (2018); enforcement uneven |
| Netherlands | Council of State (March 2022) overturned the regulator's fine against EA over FIFA packs, ruling they weren't a standalone game of chance |
| Australia | From 22 Sept 2024: paid chance-based items need at least an M rating; simulated gambling R18+ |
| Brazil | Law 15.211/2025 (ECA Digital): loot boxes prohibited in games aimed at or likely accessed by minors (in force March 2026) |
| United States | ESRB "In-Game Purchases (Includes Random Items)" label (2020). FTC actions: Epic (2022, $245M in refunds for dark-pattern purchase flows); HoYoverse (2025, $20M; odds disclosure; parental consent for under-16 purchases) |
| Platforms | Apple App Store §3.1.1 requires odds disclosure for loot boxes before purchase (since 2017) |
| United Kingdom | Government call for evidence (2020), then industry self-regulation; under review |

## Sources
- [C6] Engelstein & Shalev (2022), *Building Blocks of Tabletop Game Design*. · [C7] Engelstein, *White, Brown, and Pink* (GDC).
- [C8] Zendle & Cairns (2018), PLOS ONE. · [C9] Zendle & Cairns (2019).
- [A15] Zagal, Björk & Lewis (2013), *Dark Patterns in the Design of Games*.
- [C10] Korea GIPA. · [C11] China MoC notice. · [C12] Comparative review (Belgium, Netherlands, China, Japan). · [C13] Raad van State (2022). · [C14] Australia (2024). · [C15] Brazil (2025). · [C16] FTC–Epic. · [C17] FTC–HoYoverse. · [C18] Apple §3.1.1. · [C19] ESRB. · [C20] UK DCMS. · [C21] Xiao (2022).
- [C22] Player-documented gacha pity rules (low trust; illustrative only).
- Full bibliography: `research/SOURCES.md` in the repository.
