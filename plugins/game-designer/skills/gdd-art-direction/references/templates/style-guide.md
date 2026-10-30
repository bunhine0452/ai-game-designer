# Art and audio style guide template

```
# <Title> — Style guide            Art lead: ___  Audio lead: ___  Updated: YYYY-MM-DD

## 1. Visual pillars (max 3)
| Pillar | Gameplay need served | Do | Don't | Test |
|---|---|---|---|---|

## 2. References (what to take from each)
| Ref | Take | Avoid |
|---|---|---|

## 3. Palette
- Base palette per area/biome (hex), value range per layer (background / midground / gameplay)
- RESERVED gameplay colors (never used decoratively): danger ___, pickup ___, ally ___, enemy ___
- Colorblind check: gameplay colors also differ by shape/icon/pattern; validated with a CVD simulator

## 4. Readability rules
- Hierarchy: gameplay > characters > environment > decoration
- Silhouette test results (sheet of black fills, pass/fail per asset)
- Value contrast target between gameplay layer and background: ___
- Motion: only gameplay objects move fast; ambient motion is slow and low-contrast

## 5. Shape language
| Shape | Meaning in this game | Used on |
|---|---|---|

## 6. Characters
Proportions, line/edge treatment, material rules, faction identity, power-source visibility

## 7. Environments
Modularity, landmark rules (one landmark per area visible from entrances), lighting moods per pacing state

## 8. VFX
Size and brightness scale with consequence; telegraph colors; screen-shake/flash limits + accessibility toggle

## 9. UI / HUD
Grid, type scale (min sizes per platform), icon style, states (hover/pressed/disabled/selected/error), contrast ≥ 4.5:1 for text

## 10. Animation principles
Anticipation / impact / follow-through timings for core actions; hitstop frames; cancel windows

## 11. Color script
Thumbnail strip per level/beat aligned with the interest curve (link fun-curve chart)

## 12. Audio
- Audio pillars (max 3) with tests
- Mix hierarchy and ducking
- Music behavior per state (explore / tension / combat / boss / menu)
- Sound families (materials, factions), VO direction, loudness targets
- Accessibility: captions, visual equivalents for critical cues, separate sliders

## 13. Technical constraints
Texture budgets, poly/sprite sizes, shader limits, audio formats/voices, target platforms

## 14. Do / don't boards
Paired examples for the most common mistakes
```

Sources: [D5] TF2 readability; [B31] Riot clarity; [D6] Journey art; [D13] Overwatch audio;
[D7]/[D8] accessibility guidelines. Full bibliography: `research/SOURCES.md`.
