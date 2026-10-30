# Interest curve report: Low Tide — original draft

| Metric | Value |
|---|---|
| Duration | 40.0 min |
| Beats | 21 |
| Mean intensity | 5.69 / 10 |
| Peaks (≥ threshold) | 3 |
| Climax | 10 at 12 min (30% through) |
| Hook strength | 3 / 10 |
| Time at high intensity | 22% |
| Time at low intensity | 25% |
| Pacing health (heuristic) | 0 / 100 |

## Findings

- **[HIGH] MISSING_HOOK** (0.0-4.0 min): No beat reaches 6/10 in the first 10% of the experience (best is 3). Players decide early whether to keep going.
  - Fix: Open with a short, legible high-interest moment (a promise of the core fantasy, a striking reveal, or a quick win), then dip to teach.
- **[HIGH] FLAT_ZONE** (0.0-8.0 min): 0.0-8.0: intensity stays within ±0.5 around 2.9 for 8.0 units (low and flat: boredom and quit risk).
  - Fix: Insert a contrast beat: a twist on the current mechanic, a new threat, a reveal, a reward, or a deliberate rest that sets up the next rise.
- **[HIGH] EARLY_CLIMAX** (at 12.0 min): The strongest moment (10, The drowned keeper tears through the pump hall; flee upstairs) happens at 30% of the experience; later beats never top it.
  - Fix: Move or build a climax into the last 30%, or reduce the early peak so the ending is the highest point.
- **[MEDIUM] SUSTAINED_PEAK** (11.3-20.0 min): 11.3-20.0: intensity stays at or above 8 for 8.7 units (22% of the run).
  - Fix: Break the plateau into two peaks with a short release between them, or vary the kind of intensity (spatial, cognitive, emotional).
- **[MEDIUM] NO_ESCALATION** (12.0-30.0 min): Peaks after the hook don't rise (trend -6.6 points across the run).
  - Fix: Make each major peak a little stronger or more complex than the last: sawtooth upward, resetting lower after each release.
- **[MEDIUM] FLAT_ZONE** (13.0-20.0 min): 13.0-20.0: intensity stays within ±0.5 around 8.1 for 7.0 units (high and flat: numbness and fatigue risk).
  - Fix: Insert a contrast beat: a twist on the current mechanic, a new threat, a reveal, a reward, or a deliberate rest that sets up the next rise.
- **[MEDIUM] NO_RELIEF** (20.0-24.8 min): Peak at 20.0 (8, Return through the same pursuit corridor) is not followed by a drop of 2.5+ within 4.8 units.
  - Fix: After a peak, give a release beat (safe room, loot, story, shop, short traversal) so the next peak lands harder.
- **[MEDIUM] FLAT_ZONE** (20.1-30.1 min): 20.1-30.1: intensity stays within ±0.5 around 7.1 for 10.0 units (high and flat: numbness and fatigue risk).
  - Fix: Insert a contrast beat: a twist on the current mechanic, a new threat, a reveal, a reward, or a deliberate rest that sets up the next rise.
- **[MEDIUM] NO_RELIEF** (30.0-34.8 min): Peak at 30.0 (7, Climb the service stair ahead of the keeper) is not followed by a drop of 2.5+ within 4.8 units.
  - Fix: After a peak, give a release beat (safe room, loot, story, shop, short traversal) so the next peak lands harder.
- **[LOW] MONOTONY** (0.0-8.0 min): 5 consecutive 'explore' beats from 0.0 to 8.0.
  - Fix: Interleave a different activity or change the rules of the repeated one.
- **[LOW] MONOTONY** (12.0-20.0 min): 5 consecutive 'chase' beats from 12.0 to 20.0.
  - Fix: Interleave a different activity or change the rules of the repeated one.
- **[LOW] MONOTONY** (22.0-28.0 min): 4 consecutive 'puzzle' beats from 22.0 to 28.0.
  - Fix: Interleave a different activity or change the rules of the repeated one.

## Curve (text view)

```
 10 |                   o                                            
  9 |                    ··                                          
  8 |                  ·   o··o··o···o·                              
  7 |                 ·                ·o··o··o··o··o·               
  6 |                                                 ·o··           
  5 |                o                                    ·o·        
  4 |              ··                                        ·o·     
  3 |  ·o··o··o···o                                             ·o·  
  2 |o·                                                            ·o
  1 |                                                                
  0 |                                                                
    +----------------------------------------------------------------
     0.0                                                         40.0
```

## Beats

| Time (min) | Intensity | Type | Label |
|---|---|---|---|
| 0 | 2 | explore | Land at the flooded service quay; inspect abandoned supplies |
| 2 | 3 | explore | Wade through the intake passage |
| 4 | 3 | explore | Search the keeper office for a key |
| 6 | 3 | explore | Read the maintenance log and find the pump diagram |
| 8 | 3 | explore | Return along the intake passage |
| 10 | 5 | puzzle | Restore the first pump with a valve sequence |
| 12 | 10 | chase | The drowned keeper tears through the pump hall; flee upstairs |
| 14 | 8 | chase | Cross the flooded gallery with the keeper behind |
| 16 | 8 | chase | Evade the keeper along a second gallery |
| 18 | 8 | chase | Repeat the gallery route to retrieve a fuse |
| 20 | 8 | chase | Return through the same pursuit corridor |
| 22 | 7 | puzzle | Fit the fuse while the keeper pounds on the door |
| 24 | 7 | puzzle | Turn the second bank of valves |
| 26 | 7 | puzzle | Repeat the valve pattern on the upper manifold |
| 28 | 7 | puzzle | Open the lens-room drain with another valve bank |
| 30 | 7 | chase | Climb the service stair ahead of the keeper |
| 32 | 6 | story | Listen to a radio recording about the lost rescue crew |
| 34 | 5 | puzzle | Align the lighthouse lens |
| 36 | 4 | explore | Walk to the roof beacon |
| 38 | 3 | story | Wait for the rescue boat |
| 40 | 2 | rest | Board the boat; chapter ends |

_Heuristic diagnostics. Thresholds are configurable; confirm with playtest data (quit points, session length, observed affect)._
