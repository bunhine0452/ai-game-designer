# Interest curve report: Roguelite run (20 minutes, two biomes + final boss)

| Metric | Value |
|---|---|
| Duration | 20.0 min |
| Beats | 22 |
| Mean intensity | 5.72 / 10 |
| Peaks (≥ threshold) | 6 |
| Climax | 10 at 19.5 min (98% through) |
| Hook strength | 7 / 10 |
| Time at high intensity | 8% |
| Time at low intensity | 1% |
| Pacing health (heuristic) | 92 / 100 |

![Interest curve](https://raw.githubusercontent.com/bunhine0452/ai-game-designer/main/docs/images/examples/roguelite-20min-run_curve.png)

## Findings

- **[MEDIUM] NO_RELIEF** (13.5-15.9 min): Peak at 13.5 (7, Trap gauntlet) is not followed by a drop of 2.5+ within 2.4 units.
  - Fix: After a peak, give a release beat (safe room, loot, story, shop, short traversal) so the next peak lands harder.

## Curve (text view)

```
 10 |                                                          o··o  
  9 |                                                          ·     
  8 |                          ·o                             ·    · 
  7 |  o          ·o          ·                ·o     o      ·       
  6 | · ··      o·  ·      ··o   ·      ·o·   ·  ·  ·· ·    o        
  5 |     o·  ··     ·   o·       ·   o·   · ·    ·o       ·        o
  4 |o      ·o          ·           ··      o           · ·          
  3 |                 o·           o                     o           
  2 |                                                                
  1 |                                                                
  0 |                                                                
    +----------------------------------------------------------------
     0.0                                                         20.0
```

## Beats

| Time (min) | Intensity | Type | Label |
|---|---|---|---|
| 0 | 4 | setup | Choose loadout |
| 0.5 | 7 | combat | Ambush hook |
| 1.5 | 5 | combat | First room |
| 2.5 | 4 | reward | First boon pick |
| 3.5 | 6 | combat | Elite room |
| 4.5 | 7 | combat | Mini-gauntlet |
| 5.5 | 3 | shop | Shop |
| 6.5 | 5 | explore | Branching path choice |
| 7.5 | 6 | combat | Combat room |
| 8.5 | 8 | boss | Mid-boss |
| 9.5 | 3 | rest | Fountain + story beat |
| 10.5 | 5 | combat | Biome 2 new enemy |
| 11.5 | 6 | combat | Combo enemy room |
| 12.5 | 4 | reward | Rare boon |
| 13.5 | 7 | combat | Trap gauntlet |
| 14.5 | 5 | event | Risky event |
| 15.5 | 7 | combat | Elite pair |
| 16.5 | 3 | shop | Shop + heal |
| 17.5 | 6 | combat | Pre-boss room |
| 18.5 | 9.5 | boss | Final boss phase 1-2 |
| 19.5 | 10 | boss | Final boss phase 3 |
| 20 | 5 | reward | Run summary + unlock |

_Heuristic diagnostics. Thresholds are configurable; confirm with playtest data (quit points, session length, observed affect)._
