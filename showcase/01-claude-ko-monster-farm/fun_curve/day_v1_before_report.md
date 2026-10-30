# Interest curve report: Monster Farm - one in-game day v1 (before)

| Metric | Value |
|---|---|
| Duration | 15.0 min |
| Beats | 18 |
| Mean intensity | 3.86 / 10 |
| Peaks (≥ threshold) | 1 |
| Climax | 8 at 5 min (33% through) |
| Hook strength | 4 / 10 |
| Time at high intensity | 0% |
| Time at low intensity | 14% |
| Pacing health (heuristic) | 29 / 100 |

![Interest curve](day_v1_before_curve.png)

## Findings

- **[HIGH] MISSING_HOOK** (0.0-1.5 min): No beat reaches 6/10 in the first 10% of the experience (best is 4). Players decide early whether to keep going.
  - Fix: Open with a short, legible high-interest moment (a promise of the core fantasy, a striking reveal, or a quick win), then dip to teach.
- **[HIGH] FLAT_ZONE** (0.0-3.5 min): 0.0-3.5: intensity stays within ±0.5 around 3.9 for 3.5 units (low and flat: boredom and quit risk).
  - Fix: Insert a contrast beat: a twist on the current mechanic, a new threat, a reveal, a reward, or a deliberate rest that sets up the next rise.
- **[HIGH] EARLY_CLIMAX** (at 5.0 min): The strongest moment (8, Rare crop harvest + shipping payout) happens at 33% of the experience; later beats never top it.
  - Fix: Move or build a climax into the last 30%, or reduce the early peak so the ending is the highest point.
- **[HIGH] FLAT_ZONE** (5.8-14.0 min): 5.8-14.0: intensity stays within ±0.5 around 3.6 for 8.2 units (low and flat: boredom and quit risk).
  - Fix: Insert a contrast beat: a twist on the current mechanic, a new threat, a reveal, a reward, or a deliberate rest that sets up the next rise.
- **[MEDIUM] MONOTONY** (0.5-4.5 min): 5 consecutive 'farm' beats from 0.5 to 4.5.
  - Fix: Interleave a different activity or change the rules of the repeated one.
- **[LOW] MONOTONY** (8.0-11.5 min): 5 consecutive 'explore' beats from 8.0 to 11.5.
  - Fix: Interleave a different activity or change the rules of the repeated one.

## Curve (text view)

```
 10 |                                                                
  9 |                                                                
  8 |                     o                                          
  7 |                    · ·                                         
  6 |                       ·                                        
  5 |                 ··o                                            
  4 |  o···o···o····o·       ·   ·o··   ·o···o···o··   o··           
  3 |o·                       o··    ··o            ·o·   ··o···o·   
  2 |                                                             ··o
  1 |                                                                
  0 |                                                                
    +----------------------------------------------------------------
     0.0                                                         15.0
```

## Beats

| Time (min) | Intensity | Type | Label |
|---|---|---|---|
| 0 | 3 | setup | Wake up - check weather and calendar |
| 0.5 | 4 | farm | Walk the fields |
| 1.5 | 4 | farm | Water crops (order slime to help) |
| 2.5 | 4 | farm | Keep watering |
| 3.5 | 4 | farm | Pull weeds |
| 4.5 | 5 | farm | Harvest |
| 5 | 8 | reward | Rare crop harvest + shipping payout |
| 6 | 3 | village | Walk to village |
| 7 | 4 | village | Seed shop |
| 8 | 3 | explore | Walk to forest |
| 8.5 | 4 | explore | Forage |
| 9.5 | 4 | explore | Forage |
| 10.5 | 4 | explore | Forage |
| 11.5 | 3 | explore | Walk home |
| 12 | 4 | monster | Feed monsters |
| 13 | 3 | monster | Pet monsters |
| 14 | 3 | rest | Write diary |
| 15 | 2 | rest | Go to sleep |

_Heuristic diagnostics. Thresholds are configurable; confirm with playtest data (quit points, session length, observed affect)._
