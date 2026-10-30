# Fighting

Covers 2D and 3D versus fighters, tag fighters, platform fighters and anime fighters.

## Core loop
Read the opponent → choose an option (attack, block, throw, move, wait) → the interaction
resolves (frame advantage, hit or block) → adapt (condition the opponent, then counter their
adaptation) → round or match result.

## Signature mechanics
- **Frame data:** startup, active and recovery frames; advantage on hit and on block.
- The rock-paper-scissors core: strike beats throw, throw beats block, block beats strike.
  Plus spacing (footsies), anti-airs and mix-ups.
- Meter and resources: super meter, burst or breaker, guard gauge.
- Combos, links and cancels; execution barriers vs. simplified inputs.
- **Rollback netcode**: predict remote inputs and correct by rolling back. It's now the
  expected online standard.

## Pacing shape
Within a round: neutral → an opening → punish or combo → reset to neutral, with momentum
swings. Matches are best-of-N, with comebacks from meter or burst mechanics. Long-term pacing
comes from the community metagame: tier shifts after patches and discoveries.

## Progression model
Skill and knowledge progression: matchups, frame data, combos. Supporting systems include
ranked ladders, character mastery, and single-player modes (story, arcade, trials) that teach
fundamentals. Cosmetic unlocks.

## Balancing levers
- Frame data (startup and recovery), damage, hitbox and hurtbox sizes.
- Meter gain and cost; comeback mechanics and their strength.
- Character archetypes (rushdown, zoner, grappler) and their matchup spread.
- Execution difficulty vs. reward.
- Sirlin's goals: **viable options** (many characters and moves are worth using) and
  **fairness** (players of equal skill have about equal chances despite asymmetric picks).
  Avoid a **dominant** move or character above everything else.

## Failure modes
- **New-player wall:** fundamentals and execution come before any fun. Several GDC talks
  survey a decade of approachability attempts.
- **Degenerate loops:** infinite combos, unblockable setups, safe-on-block moves with no
  counter.
- **Bad netcode:** delay-based online play kills the competitive scene.
- **Weak single-player and onboarding**, so players leave before they're ready for ranked.
- **Patch whiplash:** large swings that wipe out player investment.

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| Street Fighter II | A clean rock-paper-scissors core with distinct archetypes; the template for the genre |
| Super Smash Bros. | Percent-based knockback and ring-outs read instantly to non-fighting-game players |
| Skullgirls | Anti-infinite and anti-unblockable systems address degenerate loops directly |
| Games with rollback netcode (e.g. GGPO-based) | Online play feels close to offline, which keeps communities alive |

## Talks and postmortems
- Sirlin, *Balancing Multiplayer Games* and *Playing to Win*.
- Cannon, *Fight the Lag!* (Game Developer Magazine, 2012); GGPO.
- GDC sessions on fighting-game approachability ('09 to '19 survey; Skullgirls Mobile).

## Design questions
1. What does a new player do in the first 10 minutes that feels like *fighting*, not
   button-mashing?
2. Is there a counter for every option, and can it be read in real time?
3. Which character archetypes exist, and does each have a viable plan against the others?
4. What is the netcode plan, and is it in scope from day one?

## Sources
- [B7] Sirlin, *Balancing Multiplayer Games*. https://www.sirlin.net/articles/balancing-multiplayer-games-part-1-definitions
- [B8] Sirlin (2006), *Playing to Win*. https://www.sirlin.net/ptw
- [B9] Cannon (2012), *Fight the Lag!*; GGPO. https://www.ggpo.net/
- [B10] GDC approachability sessions.
- Full bibliography: `research/SOURCES.md` in the repository.
