# Interest curve report: Tidecaller 30-minute run (draft v1)

| Metric | Value |
|---|---|
| Duration | 30.0 min |
| Beats | 26 |
| Mean intensity | 5.76 / 10 |
| Peaks (≥ threshold) | 5 |
| Climax | 10 at 16.5 min (55% through) |
| Hook strength | 4 / 10 |
| Time at high intensity | 20% |
| Time at low intensity | 4% |
| Pacing health (heuristic) | 43 / 100 |

![Interest curve](tidecaller-run-v1_curve.png)

## Findings

- **[HIGH] MISSING_HOOK** (0.0-3.0 min): No beat reaches 6/10 in the first 10% of the experience (best is 4). Players decide early whether to keep going.
  - Fix: Open with a short, legible high-interest moment (a promise of the core fantasy, a striking reveal, or a quick win), then dip to teach.
- **[HIGH] EARLY_CLIMAX** (at 16.5 min): The strongest moment (10, Deck comes online: first Crest chain (3 Crests in one turn)) happens at 55% of the experience; later beats never top it.
  - Fix: Move or build a climax into the last 30%, or reduce the early peak so the ending is the highest point.
- **[MEDIUM] NO_ESCALATION** (9.0-29.0 min): Peaks after the hook don't rise (trend -0.9 points across the run).
  - Fix: Make each major peak a little stronger or more complex than the last: sawtooth upward, resetting lower after each release.
- **[MEDIUM] FLAT_ZONE** (9.8-15.4 min): 9.8-15.4: intensity stays within ±0.5 around 4.9 for 5.6 units (flat: interest stops moving).
  - Fix: Insert a contrast beat: a twist on the current mechanic, a new threat, a reveal, a reward, or a deliberate rest that sets up the next rise.
- **[MEDIUM] FLAT_ZONE** (21.3-25.3 min): 21.3-25.3: intensity stays within ±0.5 around 7.9 for 4.0 units (high and flat: numbness and fatigue risk).
  - Fix: Insert a contrast beat: a twist on the current mechanic, a new threat, a reveal, a reward, or a deliberate rest that sets up the next rise.
- **[LOW] MONOTONY** (11.0-16.5 min): 5 consecutive 'combat' beats from 11.0 to 16.5.
  - Fix: Interleave a different activity or change the rules of the repeated one.

## Curve (text view)

```
 10 |                                   o                            
  9 |                   o               ·                      o··o  
  8 |                                  ·    o      o··o··o           
  7 |                  ·                    ·    ··       ·   ·      
  6 |           ··o      ·            ·  · ·    o          ·       · 
  5 |         o·  ·   o     o··o··o···o      · ·                     
  4 |    o··o·     · ·    o·              o                 ··      o
  3 |  o·           o                         o              o       
  2 |o·                                                              
  1 |                                                                
  0 |                                                                
    +----------------------------------------------------------------
     0.0                                                         30.0
```

## Beats

| Time (min) | Intensity | Type | Label |
|---|---|---|---|
| 0 | 2 | story | Lighthouse intro: the keeper hands you the tide |
| 1 | 3 | setup | Starter deck review + tide gauge tutorial popup |
| 2 | 4 | combat | Fight 1: tide-pool crabs (tutorial Surge to Crest) |
| 3.5 | 4 | reward | Card reward (pick 1 of 3) |
| 4.5 | 5 | combat | Fight 2: gull flock |
| 6 | 6 | elite | Elite: Barnacle Knight |
| 7 | 3 | shop | Shop |
| 8 | 5 | combat | Fight 3: eels |
| 9 | 9 | boss | Act 1 boss: The Drowned Choir |
| 10 | 4 | reward | Boss relic pick |
| 11 | 5 | combat | Act 2 fight: reef sharks |
| 12.5 | 5 | combat | Act 2 fight: jellyfish swarm |
| 14 | 5 | combat | Act 2 fight: sharks + eel |
| 15.5 | 5 | combat | Act 2 fight: siren pair |
| 16.5 | 10 | combat | Deck comes online: first Crest chain (3 Crests in one turn) |
| 17.5 | 4 | reward | Card reward |
| 18.5 | 8 | boss | Act 2 boss: Storm Kraken |
| 19.5 | 3 | rest | Rest site |
| 20.5 | 6 | combat | Act 3 fight: abyssal lanterns |
| 22 | 8 | elite | Elite: Pressure Golem |
| 23.5 | 8 | elite | Elite: Twin Moray |
| 25 | 8 | combat | Act 3 fight: Deepwatch squad |
| 26.5 | 3 | shop | Shop |
| 27.5 | 9 | boss | Final boss: The Moon-Eater phase 1 |
| 29 | 9 | boss | Final boss phase 2 (more HP and damage) |
| 30 | 4 | reward | Run summary + unlocks |

_Heuristic diagnostics. Thresholds are configurable; confirm with playtest data (quit points, session length, observed affect)._
