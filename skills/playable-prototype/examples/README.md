# Examples: six prototypes built with this workflow

Each was built from a showcase session's design documents
(`showcase/` in the repository), using this skill's structure and test contract.
Play them at **https://bunhine0452.github.io/ai-game-designer/games/**. The source is in `games/`
in the repository.

| Prototype | Built from | What it demonstrates |
|---|---|---|
| [Monster Farm](https://bunhine0452.github.io/ai-game-designer/games/monster-farm/) | one-page GDD (greybox scope: 6×6 field, 3 monsters, 3 days) + revised day curve | Scoping to the design's own "cheapest test"; pillars as mechanics (no failure, only detours); KO/EN UI |
| [Tidecaller](https://bunhine0452.github.io/ai-game-designer/games/tidecaller/) | final v3 card pool (24 cards, verbatim CSV) + run curve | The presentation bar: illustrated sea scene, a diegetic tide pole, hover previews tested against the real play (240/240), event playback, and title, map, reward and end screens |
| [Hoshiyobi Island](https://bunhine0452.github.io/ai-game-designer/games/hoshiyobi-island/) | v2 gacha config + monetization review | Exact odds shown in the UI; Monte Carlo vs exact math in tests; ethics findings turned into UI |
| [Low Tide](https://bunhine0452.github.io/ai-game-designer/games/low-tide/) | revised beat list + accessibility checklist | Beat list as room order; BFS bot through locked doors; captions with direction, reduced flashing |
| [Garden Guardians](https://bunhine0452.github.io/ai-game-designer/games/garden-guardians/) | rebalanced tower cost table | Balance probe at the real starting money (bot wins with 3/15 lives) |
| [Stardust Mine](https://bunhine0452.github.io/ai-game-designer/games/stardust-mine/) | economy model + prestige plan | Event-precise time; offline settlement tested against stepped simulation; labeled demo speed |

Run their tests locally:

```bash
python3 skills/playable-prototype/scripts/check.py games/
```
