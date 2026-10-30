# Interest curve report: Monster Farm - one in-game day v2 (after)

| Metric | Value |
|---|---|
| Duration | 15.0 min |
| Beats | 21 |
| Mean intensity | 5.13 / 10 |
| Peaks (≥ threshold) | 2 |
| Climax | 8 at 12.8 min (85% through) |
| Hook strength | 6 / 10 |
| Time at high intensity | 0% |
| Time at low intensity | 0% |
| Pacing health (heuristic) | 92 / 100 |

![Interest curve](day_v2_after_curve.png)

## Findings

- **[MEDIUM] FLAT_ZONE** (1.2-3.4 min): 1.2-3.4: intensity stays within ±0.5 around 4.7 for 2.2 units (flat: interest stops moving).
  - Fix: Insert a contrast beat: a twist on the current mechanic, a new threat, a reveal, a reward, or a deliberate rest that sets up the next rise.

## Curve (text view)

```
 10 |                                                                
  9 |                                                                
  8 |                                                     ·o·        
  7 |                          o                         ·   ·o      
  6 |  o·            o       ·· ·       o       ·o     o·      ·     
  5 | ·  ·o··o··   ·· ·    o·    ·   ·o· ·· ·o··  ··  ·              
  4 |o          ··o    · ··       · ·      o        o·          ·  ·o
  3 |                   o         o·                             o·  
  2 |                                                                
  1 |                                                                
  0 |                                                                
    +----------------------------------------------------------------
     0.0                                                         15.0
```

## Beats

| Time (min) | Intensity | Type | Label |
|---|---|---|---|
| 0 | 4 | setup | Wake up - monster moods at the window |
| 0.4 | 6 | discover | Overnight surprise (mutated sprout) |
| 1.2 | 5 | monster | Morning greeting + feed |
| 2 | 5 | farm | Assign jobs - slime waters / mole tills |
| 3 | 4 | farm | Sow seeds while monsters work |
| 3.8 | 6 | discover | Combo found - fertile tile |
| 4.5 | 3 | explore | Forest walk with a companion |
| 5.3 | 5 | explore | Forage + follow wild tracks |
| 6.3 | 7 | monster | Befriend a wild monster (mid peak) |
| 7 | 3 | rest | Lunch break with the view |
| 7.8 | 5 | village | Take a villager request |
| 8.4 | 6 | monster | Companion does a trick for the kids |
| 9 | 4 | village | Seed shop + trade finds |
| 9.6 | 5 | farm | Prep crops for the request |
| 10.5 | 6 | farm | Harvest today's main crop |
| 11.3 | 4 | monster | Bath and brush (affection fills) |
| 12 | 6 | village | Deliver request - recipe unlocked |
| 12.8 | 8 | reward | Shipping payout + rare mutation verdict |
| 13.6 | 7 | monster | Affection level-up - new farm skill |
| 14.3 | 3 | rest | Campfire diary |
| 15 | 4 | rest | Bedtime teaser for tomorrow |

_Heuristic diagnostics. Thresholds are configurable; confirm with playtest data (quit points, session length, observed affect)._
