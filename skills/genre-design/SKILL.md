---
name: genre-design
description: Genre playbooks for designing games in any genre and combining genres. Each playbook covers core loop, signature mechanics, pacing shape, progression model, balancing levers, failure modes and reference games with why they work. Use when the user names a genre or asks how a genre works, what players expect, how to differentiate, or how to mix genres. Covers action, platformer, FPS/TPS shooter, fighting, JRPG/WRPG/ARPG, roguelike/roguelite, metroidvania, puzzle, RTS/4X/tactics, tower defense, simulation/tycoon, city builder, survival/crafting, sandbox, horror, narrative/adventure/visual novel, card game/deckbuilder, idle/incremental, casual/hypercasual/match-3, rhythm, racing, sports, MOBA, battle royale, MMO, party/social, educational/serious, and hybrids. Also triggers on 장르, 로그라이크, 메트로배니아, 덱빌딩, 방치형, 타워 디펜스, 장르 혼합; ジャンル, ローグライク, デッキ構築, 放置系, ジャンル融合; 游戏类型, 肉鸽, 卡牌构筑, 放置类, 塔防, 品类融合; género, mezcla de géneros.
---

# Genre design playbooks

Genres are bundles of player expectations. Know which expectations to honor (players feel
cheated without them) and which to break (that's where differentiation comes from). Use the
playbook for the user's genre to ground every recommendation.

**Language:** answer in the user's language. On first use, write each technical term
localized with the English term in parentheses, e.g. `로그라이트 (Roguelite)`. Terms are in
`references/glossary.md` if bundled, or `../game-design/references/glossary.md`.

## Workflow

1. **Identify the genre(s)** from the pitch or reference games. If there's more than one,
   name the *core* genre (the moment-to-moment loop) and the *wrapper* genre(s) (session or
   meta loop).
2. **Load the playbook(s)** from the index below. Read only the files you need.
3. **Write a genre brief** for the user's concept:
   - *Expectations to honor:* 3–5 conventions this audience will assume.
   - *Opportunities to break:* 1–3 conventions that, if changed, make the game distinct.
     Tie each to a pillar.
   - *Pacing shape:* the genre's typical curve at session and whole-game scale. Hand off
     to `fun-curve` for detail.
   - *Progression model* and *balancing levers* that matter most for this concept. Hand
     numbers to `balance-economy`.
   - *Failure-mode checklist:* the genre's common traps, each marked "at risk / not at risk"
     for this concept, with a reason.
   - *Reference games:* 2–4, each with the one lesson to take (not the one feature to copy).
4. **For hybrids**, follow `references/hybrid-genres.md`: pick a core loop, map how each
   loop feeds the other, find the conflicts (pacing, input, audience), and design the
   "seam".
5. **Offer next steps:** a pacing pass (`fun-curve`), a balance model (`balance-economy`), a
   one-page design (`gdd-art-direction`) or a critique (`design-review`).

## Playbook index (`references/genres/`)

| Genre family | File |
|---|---|
| Action, platformer (incl. character action) | `action-platformer.md` |
| Shooter (FPS, TPS, hero shooter, extraction) | `shooter.md` |
| Fighting (2D/3D, platform fighter) | `fighting.md` |
| RPG (JRPG, WRPG/CRPG, ARPG/looter) | `rpg.md` |
| Roguelike, roguelite (incl. bullet heaven) | `roguelike-roguelite.md` |
| Metroidvania | `metroidvania.md` |
| Puzzle (logic, physics, spatial, narrative puzzle) | `puzzle.md` |
| Strategy (RTS, 4X, grand strategy, turn-based tactics) | `strategy.md` |
| Tower defense | `tower-defense.md` |
| Simulation, management, tycoon | `simulation-management.md` |
| City builder | `city-builder.md` |
| Survival, crafting | `survival-crafting.md` |
| Sandbox | `sandbox.md` |
| Horror (survival horror, psychological, action horror) | `horror.md` |
| Narrative, adventure, visual novel | `narrative-adventure.md` |
| Card game, deckbuilder (CCG, roguelike deckbuilder, LCG) | `card-deckbuilder.md` |
| Idle, incremental | `idle-incremental.md` |
| Casual, hypercasual, match-3 | `casual-match3-hypercasual.md` |
| Rhythm | `rhythm.md` |
| Racing (arcade, sim, kart) | `racing.md` |
| Sports (sim, arcade, management) | `sports.md` |
| MOBA | `moba.md` |
| Battle royale | `battle-royale.md` |
| MMO / MMORPG | `mmo.md` |
| Party, social (incl. social deduction) | `party-social.md` |
| Educational, serious games | `educational-serious.md` |
| Hybrid genres (method) | `../hybrid-genres.md` |

Each playbook has the same sections: **Core loop · Signature mechanics · Pacing shape ·
Progression model · Balancing levers · Failure modes · Reference games (and why they work) ·
Talks and postmortems · Design questions · Sources.**

## Principles

- **Learn from reference games, don't clone them.** Pull out the principle ("telegraphed
  enemy intent makes every turn a fair puzzle") and apply it in an original way. If the user
  wants a copy of a specific game, steer toward an original design built on the principles
  they like.
- **Respect genre literacy.** Veterans read conventions fast (minimap, dodge roll, rarity
  colors). Breaking a convention costs teaching time, so break it on purpose.
- **Scope by genre.** Some genres are content-hungry (RPG, MMO, metroidvania), others are
  systems-hungry (strategy, sim, roguelike). Warn small teams when a genre's appetite
  doesn't fit their size.
- **State the evidence.** Playbooks note where guidance rests on a designer talk or
  postmortem and where it's general practice. Racing, battle royale and party games have
  thinner primary sources (flagged in their files).

## Example

`examples/hybrid-roguelite-citybuilder.md`: a full genre brief for a hybrid concept, from
loop mapping through failure modes.
