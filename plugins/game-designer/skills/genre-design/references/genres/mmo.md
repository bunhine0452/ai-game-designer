# MMO / MMORPG

Persistent online worlds shared by many players: theme-park MMOs (curated quests and raids),
sandbox MMOs (player-driven economies and conflict) and survival MMOs.

## Core loop
Quest or activity → rewards (XP, gear, currency) → progression → group content (dungeons,
raids, PvP) → social standing and economy participation → new content updates.

## Signature mechanics
- Persistent characters, classes or skills, and gear progression.
- Group content that needs role coordination (tank, healer, DPS).
- Player economies: crafting, trading, auction houses. EVE Online publishes monthly economic
  reports tracking faucets, sinks and price indexes.
- Guilds and social structures.
- Live operations: patches, expansions, events.

## Pacing shape
Leveling arc (zones as chapters) → endgame loops (dailies, raids, seasons) → expansion
peaks. Weekly resets create recurring peaks. Live games pace by content cadence. Gaps between
updates are churn risks.

## Progression model
Vertical (levels, gear score) for the leveling phase. Horizontal (alts, collections,
cosmetics, reputation) for longevity. Social progression (guild rank, reputation) holds
players longest.

## Balancing levers
- XP curves and zone pacing (`progression_curve.py`).
- **Economy faucets and sinks.** Inflation is the classic MMO failure. Model it with
  `economy_sim.py` and monitor it as EVE does.
- Class balance in PvE (DPS parity) and PvP (counters).
- Group content difficulty tiers.
- Time-gating (lockouts) vs. grind.

## Failure modes
- **Inflation and economic collapse:** too many faucets, too few sinks.
- **Obligation loops:** dailies that feel like a job (a dark pattern: *playing by
  appointment*).
- **Content drought** between updates.
- **Unequal populations:** Bartle's point that player types shape each other in shared
  worlds (too much griefing drives off socializers).
- **Scope:** MMOs are among the most expensive genres to build and run. Warn small teams.

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| World of Warcraft | Polished theme-park leveling and raids as social goals; accessible group content |
| EVE Online | A player-driven economy with real consequences, monitored like a real economy |
| Old School RuneScape | Player polls on updates; skill-based horizontal progression |
| Final Fantasy XIV | One character can play every class, so horizontal progression keeps friends together |

## Talks and postmortems
- Koster, *Laws of Online World Design*: hard-won rules about persistent worlds.
- Bartle (1996), player-type dynamics in MUDs.
- Lehdonvirta & Castronova, *Virtual Economies: Design and Analysis* (MIT Press, 2014).
- CCP, EVE Online Monthly Economic Reports.

## Design questions
1. What do players do together that they can't do alone?
2. What are the faucets and sinks for each currency, and who monitors them after launch?
3. What does a player do on a day with only 30 minutes?
4. What's the content cadence, and can the team sustain it?

## Sources
- [B33] Koster, *Laws of Online World Design*. https://www.raphkoster.com/games/laws-of-online-world-design/
- [A7] Bartle (1996). · [B34] CCP, EVE MER. · [B35] Lehdonvirta & Castronova (2014).
- [A15] Zagal et al. (2013): playing by appointment, grinding.
- Full bibliography: `research/SOURCES.md` in the repository.
