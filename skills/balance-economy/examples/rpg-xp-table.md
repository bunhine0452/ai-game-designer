# Worked example: a 50-level RPG XP table

**Targets:** a story RPG with level 50 as the cap near the ending. First level in about
5 minutes, about 40–50 hours to the cap, and late levels around an hour each. No walls.

**Model:** polynomial curve with an offset (gentler early ratios), with XP income growing
5% per level as zones get richer.

```bash
python3 scripts/progression_curve.py --curve poly --levels 50 --first 300 --exponent 2.2 \
    --offset 5 --xp-per-hour 3000 --income-growth 1.05 \
    --name rpg-xp-table --title "RPG XP table: 50 levels, ~44 h to cap" --out examples/output
```

![RPG XP table](output/rpg-xp-table.png)

## Results

| Metric | Value | Read |
|---|---|---|
| Total XP to level 50 | 654,915 | — |
| Level 1→2 | 300 XP, 6 min | Meets the "first level fast" target |
| Level 49→50 | 37,710 XP, about 72 min | Late levels near an hour ✓ |
| Slowest level | 75 min | No level over 80 min ✓ |
| Time to the cap | 44.3 h | Inside the 40–50 h target ✓ |
| Half-XP level | 40 of 50 (80%) | Fairly back-loaded; the final ten levels hold half the XP |

Full table: `output/rpg-xp-table.csv` (columns `level, xp_to_next, cumulative_xp,
growth_ratio, xp_per_hour, hours_this_level, cumulative_hours`).

## Comparing families at the same first level and total

```bash
python3 scripts/progression_curve.py --curve all --levels 50 --first 300 --exponent 2.2 \
    --offset 5 --xp-per-hour 3000 --income-growth 1.05 --name curve-families --out examples/output
```

![Curve families](output/curve-families.png)

| Family (shape solved for the same total) | Time to cap | Slowest level | What it feels like |
|---|---|---|---|
| linear (step 544) | 54.0 h | 84 min | Slow middle (levels 15–30 drag), then late levels speed up as income outgrows XP |
| poly (exponent 2.2) | 44.3 h | 75 min | Gradual rise, then a plateau: steady |
| exp (growth 1.121) | 34.5 h | 136 min | Fast early, then a steep late grind: an endgame wall |
| logistic (cap ratio 320) | 45.3 h | 95 min | Slow start, a hump around level 30, then easing |

**Choice:** poly suits a story RPG whose ending is near the cap. For an MMO-style endgame,
exponential with horizontal progression after the cap is the usual pattern.

## Next checks
- Does new content (zones, abilities) arrive every 2–3 levels? Levels without content feel empty.
- Add catch-up XP for returning players, never penalties for absence.
- After a playtest, replace `--xp-per-hour` with measured income per zone and re-run.
