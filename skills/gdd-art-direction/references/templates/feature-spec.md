# Feature spec template

```
# Feature: <name>                     Owner: ___  Updated: YYYY-MM-DD  Status: draft/agreed/built

## Purpose
- Player problem or desire this solves: ___
- Pillar(s) served: ___
- Success looks like: ___ (observable in playtest or telemetry)

## Player-facing description
<2-4 sentences as the player would experience it>

## Rules
1. ___
2. ___
Formulas / numbers (with units; mark placeholder vs. tuned):
| Parameter | Value | Unit | Source (placeholder/target/measured) |
|---|---|---|---|

## States and flow
<state diagram or list: idle → active → cooldown → …>

## Edge cases
| Case | Expected behavior |
|---|---|
| Player disconnects / quits mid-action | |
| Inventory full / resource at cap | |
| Two triggers at once | |
| Accessibility option enabled (e.g. hold → toggle) | |

## UI and feedback
- Visual: ___  Audio: ___  Haptics: ___  (every critical cue on 2+ channels)
- Text strings (IDs for localization): ___

## Content needs
| Asset | Count | Asset-list ID |
|---|---|---|

## Telemetry
| Event | Properties | Question it answers |
|---|---|---|

## Acceptance criteria (testable)
- [ ] ___
- [ ] ___

## Dependencies and risks
- Depends on: ___   Risk: ___ (mitigation: ___)

## Open questions
- ___
```

Sources: [D3] Fullerton (2018); [A22] *Game Analytics* (telemetry design). Full bibliography: `research/SOURCES.md`.
