# Progression report: Curve families: same first level, same total XP

![Progression](https://raw.githubusercontent.com/bunhine0452/ai-game-designer/main/docs/images/examples/curve-families.png)

## linear (step = 544.4, solved for total)

- Total XP to level 50: 654,915
- XP for level 1→2: 300; for 49→50: 26,431
- Half of all XP is earned after level 36 of 50 (72% of the level range): balanced spread.
- Time to max level: 54.0 h. Per level: 6 min (fastest) to 84 min (slowest).
- WARNING: time-per-level jumps x2.68 at level 2; players feel a wall. Smooth the curve or add a new XP source there.
- Table: `curve-families_linear.csv`

## poly (exponent = 2.2, solved for total)

- Total XP to level 50: 654,915
- XP for level 1→2: 300; for 49→50: 37,710
- Half of all XP is earned after level 40 of 50 (80% of the level range): balanced spread.
- Time to max level: 44.3 h. Per level: 6 min (fastest) to 75 min (slowest).
- Table: `curve-families_poly.csv`

## exp (growth = 1.121, solved for total)

- Total XP to level 50: 654,915
- XP for level 1→2: 300; for 49→50: 70,716
- Half of all XP is earned after level 44 of 50 (88% of the level range): back-loaded; the late game carries most of the grind.
- Time to max level: 34.5 h. Per level: 6 min (fastest) to 136 min (slowest).
- Table: `curve-families_exp.csv`

## logistic (cap_ratio = 320.4, solved for total)

- Total XP to level 50: 654,915
- XP for level 1→2: 300; for 49→50: 26,431
- Half of all XP is earned after level 38 of 50 (76% of the level range): balanced spread.
- Time to max level: 45.3 h. Per level: 6 min (fastest) to 95 min (slowest).
- Table: `curve-families_logistic.csv`

## Sample rows (linear)

| level | xp_to_next | cumulative_xp | growth_ratio | xp_per_hour | hours_this_level | cumulative_hours |
|---|---|---|---|---|---|---|
| 1 | 300 | 0 |  | 3000.0 | 0.1 | 0.0 |
| 2 | 844 | 300 | 2.8147 | 3150.0 | 0.268 | 0.1 |
| 3 | 1389 | 1144 | 1.6447 | 3307.5 | 0.42 | 0.37 |
| 5 | 2478 | 4466 | 1.2816 | 3646.5 | 0.679 | 1.34 |
| 10 | 5200 | 22298 | 1.1169 | 4654.0 | 1.117 | 5.72 |
| 26 | 13910 | 170820 | 1.0407 | 10159.1 | 1.369 | 27.06 |
| 49 | 26431 | 628484 | 1.021 | 31203.8 | 0.847 | 53.2 |
| 50 |  | 654915 |  |  |  | 54.05 |

_Read XP together with income: players feel time per level, not XP._
