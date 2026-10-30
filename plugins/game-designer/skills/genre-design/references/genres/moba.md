# MOBA

Team-based competitive matches (usually 5v5) where each player controls one hero with
unique abilities, pushing lanes toward the enemy base. Variants: classic three-lane, arena
MOBAs, mobile MOBAs, auto-battlers as a related genre.

## Core loop
Pick or ban a hero → laning (last-hits, trades) → earn gold and XP → items and levels →
team fights and objectives → push or defend → destroy the base.

## Signature mechanics
- Heroes with kits of about 4 abilities and roles (carry, support, tank, mage).
- Lanes, minions, towers, jungle and neutral objectives.
- In-match economy and item builds.
- Fog of war and vision control.
- Draft (pick and ban) as a strategic pre-game.

## Pacing shape
Early game: laning, small skirmishes. Mid game: rotations and objectives. Late game: decisive
team fights, often with comebacks (bounties on leaders, objectives that scale). Matches of
20–40 minutes have a clear three-act structure.

## Progression model
Within a match: levels and items. Across matches: hero mastery, ranked ladder, collection
(heroes, skins). Riot's stated values stress **mastery**: kits that reward fine skill over
time.

## Balancing levers
- Hero stats and ability numbers. Patches are the main tool.
- Item costs and power (cost curves); gold income rates.
- Snowball vs. comeback mechanics (bounties, objective scaling).
- Map timers (objective respawns).
- Pick, ban and win rates by skill tier. Balance for the top and the median separately.
- Sirlin: **viable options** (many heroes are worth picking) and no dominant pick.

## Failure modes
- **Unreadable team fights:** effects and silhouettes blur together. Riot names silhouette
  the top factor in recognizing a champion, and keeps skins from hiding where its power comes
  from.
- **Kits without counterplay:** Riot later admitted that some champions left opponents too few
  ways to respond.
- **Snowballing:** early leads become unbeatable, and the game drags on after it's decided.
- **Toxicity** from long matches, high stakes and dependence on teammates.
- **Huge onboarding cost:** 100+ heroes and items to learn.

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| League of Legends | Clarity standards (silhouettes, ability readability) and kits built around mastery |
| Dota 2 | Deep systemic interactions; denial and courier mechanics add strategic layers |
| Pokémon UNITE / mobile MOBAs | Shorter matches and simplified economies fit mobile sessions |

## Talks and postmortems
- Riot Games, /dev: *Clarity in League*; design values (mastery, counterplay; recap).
- Sirlin, *Balancing Multiplayer Games*.

## Design questions
1. Can a spectator tell what every hero just did in a team fight?
2. What does each kit let opponents do in response?
3. How often do teams that are behind at 15 minutes come back? (Target a healthy band, not 0% or 50%.)
4. How many heroes does a new player need to know to enjoy match one?

## Sources
- [B31] Riot Games, /dev: Clarity in League. https://riotgames.com/en/news/dev-clarity-in-league
- [B7] Sirlin. · [D5] TF2 readability (silhouettes).
- Full bibliography: `research/SOURCES.md` in the repository.
