# RPG (JRPG, WRPG/CRPG, ARPG)

Covers JRPGs (party-based, often turn-based, authored story), WRPGs and CRPGs (player choice,
builds, reactive worlds) and ARPGs and looters (real-time combat, randomized loot).

## Core loop
- **JRPG:** explore → encounter → tactical battle → XP, loot, story → upgrade party → next area.
- **WRPG/CRPG:** quest → choose an approach (combat, stealth, dialogue) → consequences →
  build choices → new quests.
- **ARPG/looter:** kill → loot drop → evaluate → equip or salvage → stronger build → harder
  content.

## Signature mechanics
- Stats, classes, skill trees, leveling.
- Party composition and turn order (JRPG), action economy (CRPG).
- Itemization: rarity tiers, affixes, set items, crafting (ARPG).
- Dialogue and choice systems, reputation, companions.
- Random level and item generation (Diablo's design combined random levels, enemies and items
  to keep replays fresh).

## Pacing shape
Story arcs per chapter with dungeon climaxes; towns and camps as valleys. The whole game ramps
in power, with new mechanics every few hours. ARPGs add an endgame loop (repeatable, scaling
difficulty tiers) in place of a final climax.

## Progression model
- **Character power** (levels, gear) plus **player knowledge** (systems mastery).
- XP curves are usually polynomial or exponential and paired with growing XP income. Players
  feel *time per level*, not XP. Use `balance-economy`.
- Horizontal progression (new options) vs. vertical (bigger numbers). Healthy RPGs mix both.

## Balancing levers
- XP and level tables; enemy scaling (level-locked vs. level-scaled zones).
- Damage formulas (attack vs. defense), crit and evasion caps, stat soft caps.
- Loot tables: drop rates, rarity distribution, bad-luck protection.
- Build diversity: no single dominant build; respec cost.
- Resource attrition (JRPG MP and items between saves).

## Failure modes
- **Stat bloat:** numbers grow but decisions don't. "+3% damage" upgrades nobody notices.
- **Grind walls:** a level or gear requirement that outpaces natural progression.
- **Level scaling that erases progress** (the world scales so the player never feels stronger).
- **Loot fatigue:** too many drops, mostly junk, with no meaningful comparison.
- **Choices without consequence**, or with consequences too late to notice.
- **Scope:** RPGs are content-hungry. Indie teams should limit the world size, not the
  depth of reactivity.

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| Diablo | Random levels plus random items make "one more run" compulsive, and every drop a small lottery with build implications |
| Persona series | A calendar structure links dungeon progress to social links, so two loops reinforce each other |
| Baldur's Gate 3 / Divinity: Original Sin 2 | Systemic interactions (surfaces, elements) turn turn-based fights into puzzles with many solutions |
| Disco Elysium | Skills as voices make the stat system part of the narrative itself |

## Talks and postmortems
- Brevik, *Classic Game Postmortem: Diablo* (GDC 2016).
- Schreiber & Romero, *Game Balance*: progression and stat formulas.
- Ryan, Rigby & Przybylski (2006): autonomy and competence needs in RPG players.

## Design questions
1. What does the player decide in a typical fight, and does it change by level 20?
2. Is the progression mainly vertical, horizontal, or both? Where does each kick in?
3. How many builds are viable at endgame, and how expensive is it to try another?
4. What is the content budget per hour of play, and does it fit the team?

## Sources
- [B41] Brevik (2016). https://gdcvault.com/play/1023469/Classic-Game-Postmortem
- [C1] Schreiber (2010), *Game Balance Concepts*. · [C2] Schreiber & Romero (2021), *Game Balance*.
- [A9] Ryan, Rigby & Przybylski (2006).
- Full bibliography: `research/SOURCES.md` in the repository.
