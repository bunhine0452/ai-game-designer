# Balancing practice: spreadsheets, simulation, metrics

## The three tools

| Tool | Strength | Weakness | Use for |
|---|---|---|---|
| Spreadsheet model | Transparent, fast to change, shareable | Shows averages, not variance; no emergent behavior | Curves, cost tables, budgets, first-pass numbers |
| Simulation (Monte Carlo, agent-based) | Variance, long tails, interactions over time | Only as good as the assumptions about behavior | Economies, drop luck, matchmaking, AI vs. AI balance |
| Playtest and telemetry | Real behavior and feelings | Slow and noisy; needs enough players | Validation, discovering exploits, feel |

Schreiber and Romero recommend all three: model in spreadsheets, simulate the variance, and
playtest the parts models can't capture.

## A balancing loop

1. **Define the targets** in player terms (time, attempts, win rates).
2. **Build the spreadsheet model**, with one row per item or level and attributes in columns.
   Keep formulas visible.
3. **Find the outliers** (cost curve, DPS budget) and fix them on paper.
4. **Simulate** where luck or time matters (`economy_sim.py`, custom scripts).
5. **Playtest** with the target audience and log the matching metrics.
6. **Compare** predicted with observed values. Update the model's assumptions, not just the
   numbers.
7. **Ship small changes**: patch one variable at a time where possible, and announce why.

## Metrics to watch after launch

| System | Metric | Healthy sign |
|---|---|---|
| Progression | Time to level N by cohort; funnel by level | Matches targets; no cliffs |
| Economy | Faucet/sink totals by source; balance percentiles; prices | In/Out near 1; stable prices |
| Combat | TTK by weapon; win rate by class or loadout | Spread inside a band; no dominant option |
| Cards / heroes | Pick rate × win rate by skill tier | Many viable options at the top; nothing oppressive at the median |
| Gacha | Pulls per hit; share of players with zero hits; spend distribution | Matches disclosed odds; no extreme pressure on minors |

Slay the Spire's team used metrics early (a metrics server and win rates per card) together
with community feedback. They warned that metrics mislead without context: a card's low win
rate may mean it gets picked in losing situations.

## Patch philosophy

- Prefer **buffing the weak** over nerfing the strong when power creep is acceptable. Prefer
  **nerfs** when the overall power level is already too high.
- Change **one thing at a time** so you can attribute the effect.
- Watch for **perception**: players react to how a change looks as well as to its size.
  Halo 3's 0.2 s sniper change considered community perception explicitly.
- Keep a **changelog with reasons**. Players accept changes they understand.

## Sources
- [C2] Schreiber & Romero (2021), *Game Balance*. · [C3] Schreiber (2016), *A Course About Game Balance* (GDC).
- [B2] Giovannetti (2019), *Slay the Spire: Metrics Driven Design and Balance* (GDC).
- [B6] Griesemer (2010), Halo 3 sniper change (GDC).
- [A22] Seif El-Nasr, Drachen & Canossa (eds., 2013), *Game Analytics*.
- Full bibliography: `research/SOURCES.md` in the repository.
