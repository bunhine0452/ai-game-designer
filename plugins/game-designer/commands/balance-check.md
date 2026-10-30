---
description: Run the right balance simulator on a config or table file and report what to change
argument-hint: "[path to an economy JSON, items CSV, beats CSV, or XP settings]"
---

Run a balance check on: $ARGUMENTS

Use the `balance-economy` skill (and `fun-curve` for pacing beats). Pick the tool from the file:

| Input | Tool |
|---|---|
| Economy JSON (currencies, faucets, sinks, gacha) | `economy_sim.py` |
| Items or cards CSV (`name,cost,attributes…`) | `cost_curve.py` |
| Beats CSV/JSON (`time,intensity,…`) | `fun_curve.py` from the `fun-curve` skill |
| XP or level settings, or no file | `progression_curve.py` with the user's numbers |

1. Read the file, tell the user which tool you chose and why, and run it with an output folder
   next to the input file (`<name>-balance/`). Use the exact numbers; never estimate what a
   script can compute.
2. Report the findings: outliers, inflation or deflation, walls in progression, and pity or
   ceiling problems. Quote the numbers.
3. Propose the smallest change that fixes each finding, re-run the tool with the change, and
   show the before and after side by side.
4. If anything touches monetization, finish with the `design-review` dark-pattern check.

If no path was given, ask which file to check and stop.
