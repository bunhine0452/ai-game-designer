# Interest curve report: Horror chapter (revised after diagnosis)

| Metric | Value |
|---|---|
| Duration | 43.0 min |
| Beats | 18 |
| Mean intensity | 5.81 / 10 |
| Peaks (≥ threshold) | 4 |
| Climax | 9.5 at 41 min (95% through) |
| Hook strength | 6 / 10 |
| Time at high intensity | 6% |
| Time at low intensity | 0% |
| Pacing health (heuristic) | 92 / 100 |

![Interest curve](https://raw.githubusercontent.com/bunhine0452/ai-game-designer/main/docs/images/examples/horror-chapter-revised_curve.png)

## Findings

- **[MEDIUM] FLAT_ZONE** (4.7-10.2 min): 4.7-10.2: intensity stays within ±0.5 around 4.5 for 5.5 units (flat: interest stops moving).
  - Fix: Insert a contrast beat: a twist on the current mechanic, a new threat, a reveal, a reward, or a deliberate rest that sets up the next rise.

## Curve (text view)

```
 10 |                                                            o   
  9 |                                                           ··   
  8 |                    ·o               o          o        ··  ·  
  7 |                  ·· ·           ·····        ·· ·     ·o       
  6 |  o             ··o   ·       ··o     ·    ·o·    ·  ··       · 
  5 |   ··   ·o·    ·           ·o·         · ··        ··          o
  4 | ·   ·o·   ··o·        o···             o          o            
  3 |o                                                               
  2 |                                                                
  1 |                                                                
  0 |                                                                
    +----------------------------------------------------------------
     0.0                                                         43.0
```

## Beats

| Time (min) | Intensity | Type | Label |
|---|---|---|---|
| 0 | 3 | explore | Wake up to radio static |
| 1.5 | 6 | scare | Shape at the end of the hall |
| 4 | 3.5 | explore | Search reception |
| 6 | 5 | puzzle | Fuse box (stalker sounds nearby) |
| 9 | 4 | story | Nurse's notes reveal |
| 12 | 6.5 | stealth | Stalker patrol: hide |
| 14 | 8 | chase | Short chase |
| 16 | 3.5 | rest | Safe room + save |
| 19 | 5 | explore | Basement descent |
| 22 | 6.5 | puzzle | Archive puzzle under time pressure |
| 25 | 7.5 | scare | Lights out |
| 27 | 4 | rest | Generator room |
| 30 | 6 | stealth | Morgue stalk |
| 33 | 8 | chase | Chase to the elevator |
| 35 | 4.5 | story | Elevator reveal |
| 38 | 7 | stealth | Final ward |
| 41 | 9.5 | boss | Cornered confrontation |
| 43 | 5 | story | Exit door |

_Heuristic diagnostics. Thresholds are configurable; confirm with playtest data (quit points, session length, observed affect)._
