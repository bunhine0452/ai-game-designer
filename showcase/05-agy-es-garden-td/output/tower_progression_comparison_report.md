# Progression report: Comparativa de Familias de Curvas (30 Niveles)

## linear (step = 164.5, solved for total)

- Total XP to level 30: 70,253
- XP for level 1→2: 120; for 29→30: 4,725
- Half of all XP is earned after level 22 of 30 (73% of the level range): balanced spread.
- Time to max level: 26.9 h. Per level: 6 min (fastest) to 71 min (slowest).
- Table: `tower_progression_comparison_linear.csv`

## poly (exponent = 2.1, solved for total)

- Total XP to level 30: 70,253
- XP for level 1→2: 120; for 29→30: 6,313
- Half of all XP is earned after level 24 of 30 (80% of the level range): balanced spread.
- Time to max level: 24.9 h. Per level: 6 min (fastest) to 92 min (slowest).
- Table: `tower_progression_comparison_poly.csv`

## exp (growth = 1.173, solved for total)

- Total XP to level 30: 70,253
- XP for level 1→2: 120; for 29→30: 10,465
- Half of all XP is earned after level 26 of 30 (87% of the level range): back-loaded; the late game carries most of the grind.
- Time to max level: 22.5 h. Per level: 6 min (fastest) to 153 min (slowest).
- Table: `tower_progression_comparison_exp.csv`

## logistic (cap_ratio = 62.51, solved for total)

- Total XP to level 30: 70,253
- XP for level 1→2: 120; for 29→30: 4,725
- Half of all XP is earned after level 23 of 30 (77% of the level range): balanced spread.
- Time to max level: 25.0 h. Per level: 6 min (fastest) to 87 min (slowest).
- Table: `tower_progression_comparison_logistic.csv`

## Sample rows (linear)

| level | xp_to_next | cumulative_xp | growth_ratio | xp_per_hour | hours_this_level | cumulative_hours |
|---|---|---|---|---|---|---|
| 1 | 120 | 0 |  | 1200.0 | 0.1 | 0.0 |
| 2 | 284 | 120 | 2.3705 | 1254.0 | 0.227 | 0.1 |
| 3 | 449 | 404 | 1.5782 | 1310.4 | 0.343 | 0.33 |
| 5 | 778 | 1467 | 1.2681 | 1431.0 | 0.544 | 1.12 |
| 10 | 1600 | 7001 | 1.1146 | 1783.3 | 0.897 | 4.62 |
| 16 | 2587 | 19069 | 1.0679 | 2322.3 | 1.114 | 10.63 |
| 29 | 4725 | 65528 | 1.0361 | 4115.6 | 1.148 | 25.77 |
| 30 |  | 70253 |  |  |  | 26.91 |

_Read XP together with income: players feel time per level, not XP._
