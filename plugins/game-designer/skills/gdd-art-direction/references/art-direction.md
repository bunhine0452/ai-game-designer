# Art direction

## Visual pillars

Up to three, each tied to a gameplay need, with do and don't examples.

```
Visual pillar: "Light tells you everything"
Serves: gameplay pillar "Light is the only resource"
Do: light sources are the brightest values on screen; enemies are dark until lit
Don't: decorative glowing props that compete with light pickups
Test: in a grayscale screenshot, can you find every light pickup in 2 s?
```

## Readability hierarchy

Rank what must read first, then spend contrast in that order:

1. **Gameplay-critical:** threats, projectiles, interactables, the player character.
2. **Characters and units:** role and team identity.
3. **Environment:** navigable space and boundaries.
4. **Decoration:** atmosphere, which must never compete with 1–3.

Tools: **value contrast** (the strongest), **saturation** (keep it for gameplay), **hue**
(team or element identity), **edge and rim lighting**, **motion**. TF2's rendering was designed
around readability. Characters got rim highlights along their silhouettes and value contrast
against environments, so players could read class and team quickly in varied lighting.

## Silhouette test

Fill every character, enemy and key prop in solid black on white:
- Can you name each one?
- Can you tell its **role** (heavy, fast, ranged, support)?
- Is the **source of its power** visible (the weapon, the glowing hand)?

Riot calls silhouette the most important factor in recognizing a champion in League of Legends,
and requires that skins never remove or significantly alter the champion's primary feature.

## Shape language

Assign consistent meaning to primitive shapes:

| Shape | Common read | Typical use |
|---|---|---|
| Circle / round | Friendly, safe, soft | Allies, pickups, safe zones |
| Square / block | Stable, sturdy, reliable | Tanks, structures, defenses |
| Triangle / sharp | Danger, speed, aggression | Enemies, hazards, attack telegraphs |

These are conventions, not laws. Their power comes from **consistency** inside your game.

## Color script

A color script is a strip of thumbnails (one per level, scene or beat) planning palette, value
and saturation across the emotional arc. Align it with the interest curve from `fun-curve`:
quieter, desaturated palettes in valleys; contrast and saturation rising toward peaks; a
distinct palette for the climax. Journey's art process covered character, architecture and
color as a sequence of emotional beats.

Checks:
- Is each area recognizable from a single thumbnail?
- Does the palette shift with the story or pacing beats?
- Are gameplay colors (danger, pickup) **reserved**, never used for decoration?

## UI and HUD clarity

- **Diegetic vs. non-diegetic:** choose per element. Diegetic UI suits immersion; HUD overlays
  suit clarity.
- **Minimal persistent HUD:** show only what the player needs constantly; reveal the rest
  in context.
- **Hierarchy:** size, position and contrast follow importance. Health and threat warnings
  rank above currency counters.
- **Iconography:** one visual language for icons; never color alone for meaning (add shape,
  icon or text).
- **Text:** readable at the target distance (TV vs. handheld). Contrast at least 4.5:1 for
  body text (the WCAG floor) and scalable font size.
- **Feedback states:** hover, pressed, disabled, selected, error, all distinct without color.

## Style guide contents

See `templates/style-guide.md`: pillars, references (what to take from each), palette with
reserved gameplay colors, value ranges per layer, shape language, character rules, environment
rules, VFX rules, UI rules, animation principles, technical constraints, and do/don't boards.

## Sources
- [D5] Mitchell, Francke & Eng (2007), *Illustrative Rendering in Team Fortress 2*, NPAR. https://www.cs.princeton.edu/courses/archive/fall07/cos597B/papers/mitchell-team-fortress.pdf
- [B31] Riot Games, /dev: *Clarity in League*. https://riotgames.com/en/news/dev-clarity-in-league
- [D6] Nava (2013), *The Art of Journey* (GDC).
- [D12] W3C (2023), WCAG 2.2: contrast minimum.
- [D7] Game Accessibility Guidelines; [D8] Xbox Accessibility Guidelines.
- Full bibliography: `research/SOURCES.md` in the repository.
