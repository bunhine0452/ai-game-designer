# Puzzle

Covers logic and grid puzzles, physics puzzles, spatial and perspective puzzles,
programming and automation puzzles, and narrative puzzle games. Match-3 is in
`casual-match3-hypercasual.md`.

## Core loop
Observe the setup → form a hypothesis → try it → see the result → revise → "aha" (insight)
→ solve → a new rule or combination is introduced.

## Signature mechanics
- A small set of rules with deep combinatorics.
- Clear, deterministic feedback. Ambiguity belongs in the puzzle, never in the rules.
- Undo and reset; often a level select.
- Hints (optional, layered) and skip options.
- Each puzzle teaches or tests one idea, or one combination of ideas.

## Pacing shape
Per chapter: **introduce** a rule with a trivial puzzle → **develop** it → **twist** it
(combine it with an earlier rule, or invert it) → a **capstone** puzzle. After hard puzzles,
add breather puzzles. Across the game, new mechanics arrive steadily. When there are no new
mechanics left, puzzles become arbitrary and players stop.

## Progression model
Knowledge progression: players learn the rules' implications. Gates: completing puzzles opens
new ones, usually with some choice of order so a stuck player can work elsewhere.
Collectibles and optional "expert" puzzles extend the game for enthusiasts.

## Balancing levers
- The number of interacting rules in a puzzle (complexity).
- Red herrings and the size of the search space (how many possible moves).
- Order and parallelism: how many puzzles are open at once.
- Hint timing and strength.
- Puzzle length: insight puzzles should be short to execute once understood.

## Failure modes
- **Trial and error instead of insight:** a search space too big to reason about.
- **Unclear rules or feedback**, so the player can't tell why a solution failed.
- **Pixel hunting and moon logic** (in adventure-game puzzles).
- **Execution difficulty** hiding a known solution (unless dexterity is intended).
- **Hard linear gates** with no alternative puzzles, so stuck players quit.
- **Introducing too many rules at once.**

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| Portal | Each chamber teaches one portal idea, then combines ideas; the narrative frames the testing |
| Baba Is You | The rules themselves are objects to push, so the core insight is changing the rules |
| The Witness | A wordless line-drawing language taught entirely through the order of panels |
| Opus Magnum / Zachtronics games | Open-ended solutions and histograms of other players' results turn a solved puzzle into optimization |

## Talks and postmortems
- Koster, *A Theory of Fun*: fun as learning patterns. Puzzles are learning in its purest form.
- Kishōtenketsu as a structure for teaching a mechanic (3D Mario analysis).
- *Note:* primary puzzle-design talks weren't retrieved in this research pass. Guidance here
  combines established principles with analysis of well-known games.

## Design questions
1. What is the one idea each puzzle wants the player to realize?
2. Can a stuck player do something else useful?
3. After solving, would the player say "of course!" rather than "how was I supposed to know?"
4. Which rule combinations are still unused, and is there game left in them?

## Sources
- [A10] Koster (2004/2013), *A Theory of Fun*.
- [A29] Kishōtenketsu / 3D Mario analysis (secondary).
- [A16] Cook (2007): skill atoms for teaching sequences.
- Full bibliography: `research/SOURCES.md` in the repository.
