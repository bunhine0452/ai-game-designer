# Narrative, adventure and visual novel

Covers point-and-click adventures, narrative exploration games ("walking sims"),
choice-driven narrative games, interactive fiction and visual novels (including
dating-sim structures).

## Core loop
Explore or read → find information (an object, a dialogue, a memory) → make a choice or
solve a puzzle → the story responds (new scene, a relationship change) → new questions.

## Signature mechanics
- Dialogue systems: choices, timed responses, tone selection.
- State tracking: flags, relationship values, qualities, inventory.
- Branching structures. Ashwell's catalog names common patterns:
  - *Time cave*: heavy branching, many endings, little state.
  - *Gauntlet*: mostly linear, with side branches that end early or return.
  - *Branch and bottleneck*: paths split and rejoin at key events; state carries the
    differences.
  - *Quest*: modular, geographic, many paths to a fixed goal.
  - *Open map*: free movement, with stories tied to places.
  - *Sorting hat*: early branching that sorts players into long linear routes.
  - *Floating modules*: storylets unlocked by state, not by position.
  - *Loop and grow*: a repeating cycle whose content changes as state accumulates.
- Environmental storytelling (objects, documents, spaces).
- Vignettes with distinct mechanics. What Remains of Edith Finch built each story from its
  own small prototype that taught itself without a tutorial.

## Pacing shape
Revelations and choices are the peaks, quiet scenes the valleys. Classic three-act shapes
work at chapter scale. Choice density matters: too many trivial choices dilute the big ones.
Visual novels pace through route structures and common-route length.

## Progression model
Story progression and relationship progression. Replay progression in branching games (new
routes, new information). Puzzles gate progress in adventure games.

## Balancing levers
- Branch budget: unique content per branch vs. shared content.
- Choice feedback: when and how consequences show (immediate acknowledgment, delayed payoff).
- Puzzle difficulty and hint systems (adventure).
- Reading load per scene, voiced vs. text.
- How visible state is: hidden values vs. displayed relationship meters.

## Failure modes
- **Illusion of choice exposed:** choices with no acknowledgment.
- **Combinatorial explosion:** branches multiply beyond the writing budget.
- **Moon logic puzzles** that block the story.
- **Ludonarrative dissonance:** mechanics contradict the story's themes.
- **Pacing drag:** long expository scenes without player agency.

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| What Remains of Edith Finch | Each family member's story is a self-contained, mechanically unique vignette |
| 80 Days / Inkle games | Storylets and state tracking give branching that feels huge with a controlled writing budget |
| Disco Elysium | Skills speak as characters, so the stat system *is* the narrative voice |
| Hades (as narrative design) | Dialogue reacts to run state and progresses on death; over 20,000 lines made it feel alive |
| Doki Doki Literature Club | Subverts visual-novel conventions; the expected structure itself becomes the twist |

## Talks and postmortems
- Ashwell, *Standard Patterns in Choice-Based Games* (2015).
- Short, *Small-Scale Structures in CYOA* (2016).
- Dallas, *Weaving 13 Prototypes into 1 Game: Lessons from Edith Finch* (GDC 2018).
- Kasavin & Korb, *The Dialogue of Hades* (GDC 2021).

## Design questions
1. Which structure pattern fits the writing budget and the replay goal?
2. For each major choice: how and when does the game acknowledge it?
3. Where is the player *doing* rather than reading or watching, and is it meaningful?
4. What will players retell to a friend?

## Sources
- [B19] Ashwell (2015). https://heterogenoustasks.wordpress.com/2015/01/26/standard-patterns-in-choice-based-games/
- [B20] Short (2016). https://emshort.blog/2016/11/05/small-scale-structures-in-cyoa/
- [B21] Dallas (2018). · [B3] Kasavin & Korb (2021).
- Full bibliography: `research/SOURCES.md` in the repository.
