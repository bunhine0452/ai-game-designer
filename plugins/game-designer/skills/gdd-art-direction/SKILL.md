---
name: gdd-art-direction
description: Writes game design documents and art and audio direction for any genre, from one-page designs and pitch summaries to full living GDDs, feature specs, asset lists with scope estimates, and art or audio style guides with visual pillars, shape language, color scripts, silhouette and readability tests, UI/HUD clarity and accessibility checklists (Game Accessibility Guidelines, Xbox Accessibility Guidelines). Use when the user asks for a GDD, design doc, one-pager, feature spec, asset list, content inventory, scope estimate, art bible, style guide, art direction, audio direction or accessibility review. Covers pixel art and 3D (low poly, toon, PBR) art direction, metrics and cameras. Also triggers on 기획서, 게임 기획서, 원페이지, 기능 명세서, 에셋 리스트, 아트 디렉션, 스타일 가이드, 접근성; 企画書, 仕様書, ワンページ, アセットリスト, アートディレクション, アクセシビリティ; 策划案, 设计文档, 功能文档, 美术风格, 资源清单, 无障碍; documento de diseño, guía de estilo, accesibilidad.
argument-hint: "[one-pager | gdd | spec | style guide | accessibility] [topic]"
license: MIT
compatibility: Any agent that reads SKILL.md folders (Claude Code, Claude apps, Codex, Antigravity, Cursor, Copilot). Scripts need Python 3; matplotlib optional.
metadata:
  author: bunhine0452
  version: "1.9.0"
  repository: https://github.com/bunhine0452/ai-game-designer
---

# Design documents and art direction

Documents exist to help a team decide and build, not to be complete. Write the smallest
document that gets the decision made, keep it alive, and make it visual where possible.

**Language (required):**
- Answer in the language of the user's latest message.
- In a non-English answer, write **every** technical term the first time it appears (headings
  and table headers included) as the localized term plus the English term in parentheses, e.g.
  `원페이지 기획서 (One-Page Design)`, `실루엣 테스트 (Silhouette Test)`, `視認性 (Readability)`, `accesibilidad (Accessibility)`. After that, use the localized term alone.
- Standard terms are in `references/glossary.md` if bundled, or
  `../game-design/references/glossary.md`.
- Keep code, file names and CLI flags in English. Script output is English; translate it when
  summarizing.

## Choose the document

| Need | Document | Template |
|---|---|---|
| Pitch an idea; align a small team | One-page design (system or game) | `references/templates/one-page-design.md` |
| A shared, evolving source of truth | Living GDD (hub plus linked pages) | `references/templates/gdd-full.md` |
| Specify one feature for building | Feature spec | `references/templates/feature-spec.md` |
| Plan content and estimate scope | Asset list / content inventory | `references/templates/asset-list.csv` + `references/scope-and-assets.md` |
| Define the look and sound | Art and audio style guide | `references/templates/style-guide.md` |
| Pixel art game: canvas, palette, animation rules | Pixel art style block | `references/pixel-art-direction.md` |
| 3D game: style, budgets, metrics, camera | 3D style, metrics and camera block | `references/3d-art-direction.md` |

Default to the **one-page design** at concept stage, the **living GDD hub plus feature specs**
in production, and the **style guide** once a visual target exists.

## Workflow

1. **Collect the inputs:** pillars and target aesthetics (from `game-design`), stage, team size
   and timeline, platform, reference games or images. If anything is missing, list your
   assumptions in one line and draft anyway. Never reply with questions only.
2. **Draft from the template.** Fill every field with *decisions*, not placeholders. Where a
   decision isn't made, write `OPEN QUESTION:` with options and a recommendation.
3. **Make it visual where it matters:** loop diagrams, a map sketch, a flow chart in Mermaid or
   ASCII, tables. For art direction, describe reference boards precisely (what to take from
   each image).
4. **Tie everything to the pillars.** Each feature, art rule and audio rule should name the
   pillar it serves. If it serves none, question it.
5. **Scope check:** for GDDs and asset lists, estimate the content counts and the effort, and
   compare them with the team's capacity (`references/scope-and-assets.md`). Flag overruns and
   propose cuts.
6. **Accessibility pass:** for every GDD, style guide and UI spec, include the basic-tier
   checks from `references/accessibility.md`.
7. **Make it maintainable:** add an owner, last-updated date, status per section
   (draft/agreed/built), and a change log.

## Art direction essentials (detail in `references/art-direction.md`)

- **Visual pillars:** 3 at most, each with "do" and "don't" examples and the gameplay need it
  serves.
- **Readability first:** gameplay-relevant things (threats, interactables, players) must read
  at gameplay distance and speed. Use value contrast, silhouette and saturation, held to a
  hierarchy (gameplay > characters > environment > decoration).
- **Silhouette test:** fill characters and enemies in solid black. Each must be identifiable
  and its role readable. TF2 made class silhouettes distinct, and Riot treats silhouette as the
  top factor in recognizing a champion.
- **Shape language:** assign meaning to shapes (round = friendly or safe, square = sturdy, sharp
  = danger) and apply it consistently.
- **Color script:** plan palette and value across the game's emotional arc, level by level.
- **UI/HUD:** a clear hierarchy, minimal persistent HUD, consistent iconography, readable
  type sizes, and colorblind-safe status with redundant shape or icon.

## Audio direction essentials (detail in `references/audio-direction.md`)

Audio pillars mirror the visual pillars. Define the mix priorities (gameplay-critical cues
first), the music behavior (adaptive layers, stingers), and the information carried by sound.
Overwatch's goal was "play by sound", with distinct ally and enemy footsteps. Pair every
critical audio cue with a visual one (accessibility).

## Output standards

- Headings and tables over prose; no section longer than a screen without a visual.
- Every number has a unit and a source (target, measured, or placeholder).
- Mark assumptions clearly. Never invent market data or sales figures.
- Originality: reference games are for *what to learn*. Don't copy another game's assets,
  names or distinctive designs into the user's documents.

## References

- `references/design-docs.md`: modern GDD practice (one-page designs, living docs, pillars,
  feature specs) and why heavy legacy GDDs go unread.
- `references/scope-and-assets.md`: content inventories, estimation, and indie scope rules.
- `references/art-direction.md`: visual pillars, readability, silhouettes, shape language,
  color scripts, UI/HUD.
- `references/audio-direction.md`: audio pillars, mix hierarchy, adaptive music, sound as
  information.
- `references/accessibility.md`: Game Accessibility Guidelines tiers, XAG areas, APX patterns,
  checklist.
- `references/pixel-art-direction.md`: integer-scaled canvas, palette ramps, clean lines, outlines, animation frames and timing, tiles and bitmap fonts, scope math.
- `references/3d-art-direction.md`: choosing a finishable 3D style, polygon/texel/draw-call budgets, player metrics, camera rules, landmarks and wayfinding, color scripts.
- `references/templates/`: one-page design, full GDD, feature spec, asset list (CSV), style guide.
- `examples/one-page-gdd-example.md`: a complete one-pager for an original concept.
- `examples/asset-list-example.csv`: an inventory with estimates for the same concept.
