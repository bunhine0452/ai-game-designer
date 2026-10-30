# Interest curve report: Tidecaller 30-minute run (revised v2)

| Metric | Value |
|---|---|
| Duration | 30.0 min |
| Beats | 29 |
| Mean intensity | 5.99 / 10 |
| Peaks (≥ threshold) | 9 |
| Climax | 10 at 29 min (97% through) |
| Hook strength | 7 / 10 |
| Time at high intensity | 8% |
| Time at low intensity | 0% |
| Pacing health (heuristic) | 100 / 100 |

![Interest curve](tidecaller-run-v2_curve.png)

## Findings

No pacing problems detected by the heuristics. Validate with playtests.


## Curve (text view)

```
 10 |                                                            ·o  
  9 |                                                          o·    
  8 |                   o             o     o      o     o    ·      
  7 | o          ·o    ·       o·    ··    ·     ·· ·  o· ·        · 
  6 |  ·    o·o·· ·      ·   ··  o        o     o      ·     ·       
  5 |     o·          o     o     ·    · ·   · ·      ·             o
  4 |o  o·         · ·    o·       ··   o            o     ··        
  3 |               o              o          o             o        
  2 |                                                                
  1 |                                                                
  0 |                                                                
    +----------------------------------------------------------------
     0.0                                                         30.0
```

## Beats

| Time (min) | Intensity | Type | Label |
|---|---|---|---|
| 0 | 4 | setup | Pick 1 of 3 starting tide relics (20 s; intro moved to the death screen) |
| 0.5 | 7 | combat | Cold open: shipwreck ambush at tide 8 - first Crest inside 60 s |
| 1.5 | 4 | reward | First card reward (pick 1 of 3) |
| 2.5 | 5 | combat | Fight: tide-pool crabs push the gauge (enemy tide intent introduced) |
| 3.5 | 6 | event | Event: Riptide shrine - trade HP for a Surge relic |
| 4.5 | 6 | combat | Fight: gull flock (AoE check) |
| 6 | 7 | elite | Elite: Barnacle Knight (armored unless the tide is low) |
| 7 | 3 | shop | Shop: first card removal |
| 8 | 5 | combat | Fight: eels |
| 9 | 8 | boss | Act 1 boss: The Drowned Choir |
| 10 | 4 | reward | Boss relic pick |
| 11 | 5 | combat | Act 2 fight: reef sharks (enemies now Ebb the gauge against you) |
| 12.5 | 7 | event | Spring-tide night: opt in - next 2 fights start at tide 8 for double gold |
| 13.5 | 6 | combat | Spring-tide fight: jellyfish swarm (Drench check) |
| 14.5 | 3 | rest | Tide pool: upgrade or heal |
| 15.5 | 8 | combat | Siren pair: the deck comes online - first double Crest |
| 16.5 | 4 | reward | Rare card reward |
| 17.5 | 6 | elite | Elite: Undertow Twins (one Surges and one Ebbs every turn) |
| 18.5 | 8.5 | boss | Act 2 boss: Storm Kraken (seizes the gauge every 2nd turn) |
| 19.5 | 3 | rest | Rest site + lighthouse story beat |
| 20.5 | 6 | combat | Act 3 fight: abyssal lanterns |
| 22 | 8 | elite | Elite: Pressure Golem |
| 23 | 4 | event | Event: wreck salvage (pick 1 of 3 upgrades) |
| 24 | 7 | combat | Act 3 fight: Deepwatch squad |
| 25 | 8 | elite | Elite: Twin Moray (optional path; skip = safer route) |
| 26 | 3 | shop | Shop + heal before the boss |
| 27.5 | 9 | boss | Final boss: The Moon-Eater phase 1 |
| 29 | 10 | boss | Phase 2: the Moon-Eater swings the tide each turn - Crest on its turn to break it |
| 30 | 5 | reward | Short resolution: run summary + unlock |

_Heuristic diagnostics. Thresholds are configurable; confirm with playtest data (quit points, session length, observed affect)._
