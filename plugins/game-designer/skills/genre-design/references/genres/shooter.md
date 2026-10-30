# Shooter (FPS / TPS)

Covers campaign shooters, arena and boomer shooters, tactical shooters, hero shooters,
looter shooters and extraction shooters. Battle royale has its own file.

## Core loop
Move to a position → acquire a target → shoot (aim, recoil, timing) → hit confirmation
(audio, hit marker, enemy reaction) → reposition or reload → next engagement. The "30 seconds
of fun" framing often credited to the Halo team (repeat a short, satisfying combat cycle in
varied contexts) is a useful heuristic. No primary source was retrieved for it, so don't
quote it as a fact.

## Signature mechanics
- Weapon roles: range bands, rate of fire, magazine size, reload, recoil patterns.
- Movement: sprint, slide, mantle, jump, dash, and how movement interacts with accuracy.
- Health models: regenerating, fixed with pickups, armor layers.
- Enemy archetypes (campaign) or abilities and roles (hero shooter).
- Map flow: lanes, sightlines, cover, verticality, choke points.

## Pacing shape
Campaign: combat arenas separated by traversal and story valleys, escalating enemy mixes,
set pieces as peaks. Multiplayer: engagement → reset (respawn, or round end) → engagement.
Objective modes add a match-level arc that climbs toward the final objective.

## Progression model
Campaign: weapon unlocks and upgrades, new enemy types as challenge progression.
Multiplayer: account level, cosmetics, unlockable side-grades. Keep power gains
small in PvP. Looter: gear score and build-defining exotics or legendaries.

## Balancing levers
- **Time to kill (TTK)** and its spread across weapons. Short TTK rewards positioning and
  first shot; long TTK rewards tracking and lets players respond.
- Damage falloff by range, headshot multipliers, spread and recoil.
- Ammo economy (campaign): how much ammo forces weapon variety.
- Movement speed vs. aim penalty.
- Tiny numbers matter. Halo 3's sniper time between shots went from 0.5 s to 0.7 s in a
  deliberate change, with community perception as part of the design reasoning.

## Failure modes
- **One dominant weapon** or loadout (no viable options).
- **Cover-camping stalemates.** DOOM (2016) deliberately removed regenerating health,
  reloading and cover reliance so players push forward to take resources from enemies.
- **Unreadable deaths** (no killcam or damage direction, unclear hit registration).
- **Netcode and hit-registration disputes**, which players read as design flaws.
- **Map sightlines that favor one side.**

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| DOOM (2016) | "Push-forward" combat: health and ammo come from aggression, so the optimal play is also the most exciting |
| Halo: Combat Evolved / Halo 3 | A small, readable sandbox of weapons and enemies with distinct counters |
| Counter-Strike | Economy rounds and short TTK make each round a high-stakes decision |
| Overwatch | Hero roles and audio cues ("play by sound") carry gameplay information |

## Talks and postmortems
- Loudy & Campbell, *Embracing Push Forward Combat in DOOM* (GDC 2018).
- Griesemer, *Changing the Time Between Shots for the Sniper Rifle from 0.5 to 0.7 Seconds for Halo 3* (GDC 2010).
- Lawlor & Neumann, *Overwatch: The Elusive Goal: Play by Sound* (GDC 2016).
- Ambinder, *Valve's Approach to Playtesting* (GDC 2009).

## Design questions
1. What is the TTK target, and what skill does it reward (positioning, tracking, decisions)?
2. Which behavior does the health model encourage? Is that the behavior you want?
3. For each weapon: what situation is it the best choice for, and what counters it?
4. Can a player say why they died within 2 seconds?

## Sources
- [B5] Loudy & Campbell (2018). https://gdcvault.com/play/1024940/Embracing-Push-Forward-Combat-in
- [B6] Griesemer (2010). https://gdcvault.com/play/1012211/Design-in-Detail-Changing-the
- [D13] Lawlor & Neumann (2016). · [A20] Ambinder (2009).
- [C2] Schreiber & Romero (2021): TTK and damage math.
- Full bibliography: `research/SOURCES.md` in the repository.
