# Interest curve report: Horror chapter (first draft, deliberately flawed)

| Metric | Value |
|---|---|
| Duration | 43.0 min |
| Beats | 16 |
| Mean intensity | 5.19 / 10 |
| Peaks (≥ threshold) | 2 |
| Climax | 9.5 at 25 min (58% through) |
| Hook strength | 2.5 / 10 |
| Time at high intensity | 25% |
| Time at low intensity | 28% |
| Pacing health (heuristic) | 23 / 100 |

![Interest curve](https://raw.githubusercontent.com/bunhine0452/ai-game-designer/main/docs/images/examples/horror-chapter-flawed_curve.png)

## Findings

- **[HIGH] MISSING_HOOK** (0.0-4.3 min): No beat reaches 6/10 in the first 10% of the experience (best is 2.5). Players decide early whether to keep going.
  - Fix: Open with a short, legible high-interest moment (a promise of the core fantasy, a striking reveal, or a quick win), then dip to teach.
- **[HIGH] FLAT_ZONE** (0.0-11.9 min): 0.0-11.9: intensity stays within ±0.5 around 2.6 for 11.9 units (low and flat: boredom and quit risk).
  - Fix: Insert a contrast beat: a twist on the current mechanic, a new threat, a reveal, a reward, or a deliberate rest that sets up the next rise.
- **[HIGH] EARLY_CLIMAX** (at 25.0 min): The strongest moment (9.5, Cornered fight) happens at 58% of the experience; later beats never top it.
  - Fix: Move or build a climax into the last 30%, or reduce the early peak so the ending is the highest point.
- **[MEDIUM] FLAT_ZONE** (14.7-23.0 min): 14.7-23.0: intensity stays within ±0.5 around 8.3 for 8.3 units (high and flat: numbness and fatigue risk).
  - Fix: Insert a contrast beat: a twist on the current mechanic, a new threat, a reveal, a reward, or a deliberate rest that sets up the next rise.
- **[MEDIUM] SUSTAINED_PEAK** (15.1-25.8 min): 15.1-25.8: intensity stays at or above 8 for 10.8 units (25% of the run).
  - Fix: Break the plateau into two peaks with a short release between them, or vary the kind of intensity (spatial, cognitive, emotional).
- **[MEDIUM] NO_RELIEF** (19.0-24.2 min): Peak at 19.0 (8.5, Chase continues) is not followed by a drop of 2.5+ within 5.2 units.
  - Fix: After a peak, give a release beat (safe room, loot, story, shop, short traversal) so the next peak lands harder.
- **[MEDIUM] FLAT_ZONE** (27.5-37.9 min): 27.5-37.9: intensity stays within ±0.5 around 4.3 for 10.4 units (flat: interest stops moving).
  - Fix: Insert a contrast beat: a twist on the current mechanic, a new threat, a reveal, a reward, or a deliberate rest that sets up the next rise.

## Curve (text view)

```
 10 |                                     o                          
  9 |                                  ····                          
  8 |                      oo····o···o·    ·                         
  7 |                     ·                                          
  6 |                    ·                  ·                  ·o·   
  5 |                   ·                    ·              ···   ··o
  4 |                                         o···o····o···o         
  3 |     ····o········o                                             
  2 |o···o        o                                                  
  1 |                                                                
  0 |                                                                
    +----------------------------------------------------------------
     0.0                                                         43.0
```

## Beats

| Time (min) | Intensity | Type | Label |
|---|---|---|---|
| 0 | 2 | explore | Wake up in the ward |
| 3 | 2.5 | explore | Search reception |
| 6 | 3 | explore | Nurse's notes |
| 9 | 2.5 | puzzle | Fuse box |
| 12 | 3 | explore | Corridor |
| 15 | 8 | scare | Stalker sighting |
| 16 | 8.5 | chase | Chase through wards |
| 19 | 8.5 | chase | Chase continues |
| 22 | 8 | chase | Vent escape |
| 25 | 9.5 | boss | Cornered fight |
| 28 | 4 | explore | Basement |
| 31 | 4.5 | explore | Archives |
| 34 | 4 | explore | Morgue |
| 37 | 4.5 | puzzle | Drawer puzzle |
| 40 | 6 | scare | Lights out |
| 43 | 5 | story | Exit door |

_Heuristic diagnostics. Thresholds are configurable; confirm with playtest data (quit points, session length, observed affect)._
