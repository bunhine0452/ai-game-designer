# Sports

Covers sports simulations (licensed leagues), arcade sports, physics sports hybrids
(Rocket League), sports management, and extreme or skill sports (skateboarding, golf).

> **Sourcing note:** primary sports-design sources here are mainly physics and tuning talks.
> Mode and progression guidance is general practice; validate it against your audience.

## Core loop
Match: read the play → position and choose an action (pass, shoot, tackle) → execute
(timing, aim, physics) → outcome → reset or transition. Meta: matches → rewards → team
or player improvement → season progress.

## Signature mechanics
- Physics or animation-driven ball and player control.
- Team AI (teammates and opponents) and tactics settings.
- Real-sport rules as the shared language (fast to learn when players already know the sport).
- Modes: quick match, season or career, online ranked, ultimate-team collection modes.
- Replays and highlights.

## Pacing shape
Follows the sport: halves or periods, scoring bursts, the final minutes as climax. Comeback
potential keeps late peaks alive. Season arcs: regular season → playoffs → final.

## Progression model
Player and team ratings, career modes with storylines, collection modes (card packs, with the
loot-box issues in `balance-economy`), cosmetics, ranked divisions.

## Balancing levers
- Physics tuning (Rocket League's team spent years on it, and kept one physics model across
  modes so player instincts transfer).
- AI assist strength (auto-positioning, aim assist) vs. manual control.
- Rating spread between teams and its effect on outcomes.
- Match length and pacing settings.
- Online: matchmaking and skill rating.

## Failure modes
- **Simulation fidelity over fun:** realistic but slow or unreadable.
- **Annual-release sameness**, with mostly roster updates.
- **Pay-to-win collection modes** using randomized packs (a regulatory and ethics risk).
- **AI teammates that undermine the player.**
- **The skill floor:** nothing to do until the player has mastered complex controls.

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| Rocket League | One consistent physics model, easy to understand and very deep; mastery is visible (aerials) |
| FIFA / EA Sports FC series | The licensed fantasy of real teams; career and collection modes give long arcs |
| Tony Hawk's Pro Skater | Combos and scoring turn a sport into expressive challenge |
| Football Manager | Management depth: the sport as a strategy and simulation game |

## Talks and postmortems
- Cone, *It IS Rocket Science! The Physics of Rocket League Detailed* (GDC 2018); design
  interview with Corey Davis.

## Design questions
1. What can a non-fan understand in 30 seconds?
2. Where is the expressive skill ceiling (tricks, aerials, set plays)?
3. Do teammates help, or do they make the player feel helpless?
4. If there's a collection mode, can it be played well without random paid packs?

## Sources
- [B30] Cone (2018); Davis interview (secondary).
- [C8] Zendle & Cairns (2018): loot boxes and problem gambling. · [C13] Dutch FIFA ruling.
- Full bibliography: `research/SOURCES.md` in the repository.
