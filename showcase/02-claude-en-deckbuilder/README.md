# Tidecaller: design pass 1

A roguelike deckbuilder for PC in which every card is a tide spell. Team of three.
This folder holds three deliverables: the genre brief, a 24-card starter pool with cost-curve analysis, and the interest curve of a 30-minute run.

## Files

| File | What it is |
|---|---|
| `01-genre-brief.md` | Core system (tide gauge), pillars, 5 expectations to honor, 3 conventions to break, a 12-item failure-mode checklist, reference games |
| `02-cost-curve-analysis.md` | Targets, model, v1 → v2 → v3 results, energy exchange rates, remaining risks, validation plan |
| `03-interest-curve.md` | Target shape, v1 findings and fixes, v1 → v2 metrics, what the tool can't see, validation plan |
| **Cards** | |
| `cards/tidecaller-starter-v1.csv` | Draft pool (24 cards, flat AoE flag) |
| `cards/tidecaller-starter-v2.csv` | After the first fixes (Rogue Wave, Spring Tide, Still Water, Drowned Bell) |
| `cards/tidecaller-starter-v2-aoe-check.csv` | v2 re-encoded with AoE per point, to test whether Spindrift's flag was real |
| `cards/tidecaller-starter-v3.csv` | **Final pool** (per-point AoE schema, 0 off-curve cards) |
| `cards/output/*_fit.png` | Cost-curve charts for v1, v2 and v3 (the AoE check ran without a chart) |
| `cards/output/*_report.md` | Fitted weights and per-card verdicts for each pass |
| `cards/output/*_fit.csv` | Fair cost and residual for every card in each pass |
| **Run** | |
| `run/tidecaller-run-v1.csv` | Draft beat list of a 30-minute run |
| `run/tidecaller-run-v2.csv` | Revised beat list |
| `run/output/*_curve.png` | Interest-curve charts (v1 with problems highlighted, v2 clean) |
| `run/output/*_report.md` / `*_report.json` | Findings and metrics for each version |
| `run/output/*_resampled.csv` | The curve resampled on an even time grid |

Tools used: `balance-economy/scripts/cost_curve.py --robust` and `fun-curve/scripts/fun_curve.py --reference` from the ai-game-designer plugin.

## Key conclusions

### Genre brief
- **Keep these genre conventions:** telegraphed intent (now including **tide intent** with an exact gauge preview), pick 1 of 3 with Skip, removal and upgrades,
  a visible branching map, fast restart, and meta unlocks that widen the card pool rather than add power.
- **Three conventions to break:** (1) a **shared tide gauge** that enemies push too, (2) **direction (Surge/Ebb) instead of card types**, (3) **30-minute runs**.
- **Biggest risks:** **run sameness** (one theme, two verbs), a **solved gauge** (one tide-movement deck dominating), **tide screw** from enemy Ebbs,
  and **scope** for three people. Plan one character with about 80 cards at 1.0, and keep cards data-driven.

### Cost curve
- **v1:** two cards clearly off-curve: **Rogue Wave** (cost 1, fair 2.4) was too strong and **Still Water** (cost 2, fair 0.8) too weak.
  Still Water also had a rules bug: a condition it could never meet. The less obvious finding was that **the tide was priced at about zero**
  (weight −0.04). Spring Tide (free) and Moonpull (2 energy) did the same tide job at very different costs, so the fit couldn't price tide at all.
- **v2:** four fixes. R² went from 0.71 to 0.94, and tide now prices at +0.21 per point.
- **Model check:** Spindrift's v2 flag came from the flat AoE flag. Pricing AoE per point fits better (R² 0.95) and puts Spindrift on the curve, so
  **Spindrift was not changed.**
- **v3 (final):** Rogue Wave trimmed to 12 damage, and Crest Breaker flipped to Ebb so no card is strictly better than another. **0 flagged cards, R² 0.96, RMSE 0.16.**
- **1 energy ≈ 5.9 damage ≈ 4 AoE damage ≈ 5.3 block ≈ 2.1 draws ≈ 5.3 tide points.** Crest and Slack Water each pay back about 2× what you spend on tide,
  so neither direction wins on paper. Playtests have to confirm that.

### Interest curve
- **v1** scored 43/100 with 6 findings. **No hook** (best beat 4/10 in the first 3 min). **Early climax** (the first Crest chain at 55% beat the final boss).
  A **flat Act 2** (four identical fights). A **numbing Act 3** (8/10 held for 4 min). **Falling boss peaks** (9 → 8 → 9).
- **v2** has 0 findings: a cold-open Crest within 60 s (hook 7), bosses rising **8 → 8.5 → 9 → 10**, and a climax at 97% where the Moon-Eater swings the tide
  and you must Crest on its turn. The final boss tests the core skill instead of an HP bar.
  Act 2 gets a Spring-tide night risk event and a rest. Act 3 gets a salvage valley and an optional elite.
- The 100/100 score only means no structural red flags. **The deck-comes-online peak is emergent.** Check with telemetry that the first double Crest lands
  at 45–60% of the run.

## Next steps
1. Prototype the tide gauge with the 24 v3 cards and 3 enemies that have tide intent. Test "do players hold cards because of the tide?"
2. Log per-card pick and win rate, Crest vs Slack triggers, quit points by node, and run length. Re-fit the cost curve every time the pool grows.
3. Add 2 Surge defensive cards to fix the direction skew. Run an art direction pass on card readability by direction.
