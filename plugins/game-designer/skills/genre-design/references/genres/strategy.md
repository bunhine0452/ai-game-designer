# Strategy (RTS, 4X, grand strategy, turn-based tactics)

- **RTS:** real-time base building, economy and army control.
- **4X:** *explore, expand, exploit, exterminate* (Alan Emrich coined the term in 1993).
  Long empire-building games.
- **Grand strategy:** nation-scale simulation with diplomacy and politics.
- **Turn-based tactics:** squad combat on a grid, often with a campaign layer.

## Core loop
- **RTS:** gather → build → produce units → scout → engage → expand. The match ends when one
  side breaks.
- **4X:** explore → settle or expand → develop (tech, economy) → compete (diplomacy, war) →
  next turn.
- **Tactics:** read the battlefield → position units → act → enemy turn → adapt. The
  campaign layer handles upgrades and roster management.

## Signature mechanics
- Economies with compounding growth (snowballing).
- Tech trees and unit counters (rock-paper-scissors across unit types).
- Fog of war and scouting.
- Asymmetric factions.
- Into the Breach: enemy intent is fully telegraphed, randomness is minimized, and attacks
  can be redirected. Each turn becomes a deterministic puzzle.

## Pacing shape
RTS: opening (build orders) → mid-game skirmishes → decisive battle. 4X: an exciting
explore/expand opening → a mid-game plateau (the classic weakness) → a late game often
decided long before it ends. Tactics: each battle escalates over turns; the campaign
escalates in enemy types and stakes.

## Progression model
Within a match: economy and tech. Across matches: player mastery, plus unlocks (factions,
commanders) or campaign persistence (veterans, permadeath in XCOM-likes).

## Balancing levers
- Resource income vs. unit cost (cost curves); upkeep to slow snowballing.
- Counter-matrix strength (how hard counters counter).
- Tech pacing and costs.
- Victory conditions and their timing; catch-up and anti-snowball mechanics.
- AI difficulty: bonuses vs. smarter behavior (players read flat bonuses as cheating).
- Hit chances in tactics: displayed vs. actual (some games quietly help the player),
  and their effect on trust.

## Failure modes
- **Solved openings or dominant strategies.** Players will optimize the fun out of a game if
  the optimal path is dull ("water finds a crack"). Civilization's settler-spam strategy is
  Johnson's example.
- **4X late-game slog:** the winner is clear for hours before the game ends.
- **Micromanagement overload** (RTS APM walls; 4X turn bloat).
- **Uninteresting decisions:** options aren't close in value, or outcomes can't be read
  (Meier).
- **Output-randomness frustration** in tactics ("95% shot missed").

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| StarCraft | Three highly asymmetric factions that are still fair at the top level; scouting and counters force constant adaptation |
| Civilization series | "One more turn": overlapping short-, mid- and long-term goals always leave something about to finish |
| Into the Breach | Perfect information about enemy intent plus small maps make tactics a readable puzzle |
| XCOM: Enemy Unknown | Permadeath of named soldiers adds an emotional cost to tactical risk |

## Talks and postmortems
- Meier, *Interesting Decisions* (GDC 2012).
- Johnson, *Water Finds a Crack* (Game Developer column, 2011).
- Davis, *Into the Breach Design Postmortem* (GDC 2019).
- Sirlin, *Balancing Multiplayer Games*: viable options and fairness for asymmetric factions.

## Design questions
1. What decision is the player making every 30 seconds (RTS) or every turn (4X, tactics)?
2. What stops the leader from snowballing, and does it feel fair rather than punishing?
3. When is the game usually decided, and how long after that does it end?
4. Which strategy will optimizers find first, and is it fun to repeat?

## Sources
- [B12] Emrich (1993), 4X coinage (secondary).
- [A18] Meier (2012). · [B11] Johnson (2011). https://designer-notes.com/game-developer-column-17-water-finds-a-crack
- [B13] Davis (2019). https://gdcvault.com/play/1025772/-Into-the-Breach-Design
- [B7] Sirlin. · [C1]/[C2] Schreiber: cost curves and intransitive balance.
- Full bibliography: `research/SOURCES.md` in the repository.
