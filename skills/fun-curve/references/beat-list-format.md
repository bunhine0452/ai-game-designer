# Beat list format

## CSV

```csv
# title: My level
# unit: min
time,intensity,type,label
0.0,4,setup,Choose loadout
0.5,7,combat,Ambush hook
```

- `time` (required): a number in the chosen unit, or `mm:ss` / `hh:mm:ss`. Rows are sorted
  by time. Repeated times are allowed.
- `intensity` (required): 0–10. Out-of-range values are clamped with a warning.
- `type` (optional): a lowercase category. Up to 8 types get their own color and marker;
  any more are folded into "other".
- `label` (optional): a short description. By default only peaks, the first beat and the
  climax are labeled on the chart; `--label-all` labels every beat.
- Comment lines start with `#`. `# title:` and `# unit:` are read as metadata.
- Accepted column aliases: `t`/`minute` for time; `interest`/`tension`/`value` for
  intensity; `kind` for type; `name`/`note` for label.

## JSON

```json
{"title": "My level", "unit": "min",
 "beats": [{"time": 0, "intensity": 4, "type": "setup", "label": "Choose loadout"}]}
```

A bare list of beat objects also works.

## Intensity rubric (felt engagement or tension)

Score what the player **feels**, not how much is happening on screen.

| Score | Feels like | Examples |
|---|---|---|
| 0–1 | Nothing to do or think about | Unskippable loading, menu with no decisions |
| 2–3 | Calm, low stakes | Walking through a cleared area, reading a short note |
| 4–5 | Engaged, comfortable | Routine fight, shop with real choices, light exploration |
| 6–7 | Focused, some risk | New enemy type, puzzle with an "aha", elite fight |
| 8 | High stakes, full attention | Mid-boss, chase, risky gamble, major reveal |
| 9 | Peak | Final boss phase, climactic set piece, decisive battle |
| 10 | The best moment of the experience | Use it once, at the climax |

Calibrate with the team. Score the same 10 beats independently, compare, and agree on
anchors.

## Common beat types

`setup`, `tutorial`, `explore`, `traversal`, `combat`, `elite`, `boss`, `puzzle`, `story`,
`reveal`, `reward`, `shop`, `rest`, `event`, `scare`, `chase`, `stealth`, `social`,
`build`, `menu`. Use whichever set fits the game, but keep it to about 8 per chart.

## Sources

- [A1] Schell: interest curves and scoring experiences over time.
- [A4] Booth (2009): modelling intensity from player state.
- Full bibliography: `research/SOURCES.md` in the repository.
