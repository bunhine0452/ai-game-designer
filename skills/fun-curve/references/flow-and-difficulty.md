# Flow and difficulty

## Flow

Csikszentmihalyi describes flow as deep absorption in an activity. The time sense changes,
self-consciousness fades, and the activity becomes rewarding in itself. Conditions that
recur across his studies:

- Challenge and skill are **both high and matched**.
- **Clear goals** at every moment.
- **Immediate feedback** on progress.
- A sense of **control** over the outcome.
- Full concentration, with no attention left for distraction.

Mismatches: challenge ≫ skill gives **anxiety** (frustration, quitting); skill ≫ challenge
gives **boredom**.

## The flow channel (Chen)

Chen draws flow as a band (channel) between anxiety and boredom on a challenge-vs-skill
chart. As the player's skill grows, the channel moves up and to the right, so challenge has
to grow too. Two implications:

1. **Players differ.** One fixed difficulty line puts novices in anxiety and experts in
   boredom. Hardcore and casual players need different paths through the same game.
2. **Prefer active, player-driven adjustment.** In *flOw*, players choose to dive deeper
   (harder) or rise (easier) as part of play. Difficulty becomes an in-world choice, not a
   menu setting and not a hidden algorithm.

## Ways to keep players in the channel (most to least transparent)

| Technique | How | Watch out for |
|---|---|---|
| Player-chosen challenge in the world | Optional harder routes, risk–reward branches, elite enemies, bonus objectives | Make the risky option attractive, not just harder |
| Difficulty and assist settings | Modes, granular assists (damage taken, timing windows, aim help) | Accessibility is orthogonal to difficulty; separate them |
| Self-imposed challenge systems | Heat / ascension / curse levels in roguelites | Unlock gradually; reward with recognition, not power |
| Teaching and scaffolding | Introduce → develop → twist (kishōtenketsu); optional practice spaces | Don't over-tutorialize experienced players |
| Forgiveness windows | Coyote time, input buffering, generous hitboxes | Keep them invisible and consistent |
| Hidden dynamic difficulty adjustment | Adjust spawns, drops or AI accuracy from performance | Never punish skill; keep it invisible; disclose in competitive games |
| Rubber banding | Catch-up for trailing players (racing, party) | Overdone, it makes winning feel random |

## Sawtooth difficulty

Ramp difficulty within a segment, peak at a test (boss, gate level), then **reset lower,
above the previous low**. Each reset gives recovery and a feeling of mastery ("this used to
be hard"). Each new peak tests a little more. Typical cadence: a new teach-test cycle every
5–15 minutes in action games, a hard level about every 5th level in match-3, and a mid-boss
every biome in roguelites.

## Difficulty spikes and walls

A **spike** is a sharp, short jump; a **wall** is a sustained jump many players can't get
past. Diagnose them from data:
- **Funnel drop-off**: the share of players who reach segment N but not N+1.
- **Attempts per segment** and **deaths per minute**: a sudden rise marks a spike.
- **Quit after failure**: the share of sessions that end within a minute of a death.

Fixes: teach the needed skill earlier (skill-atom gap), add a checkpoint before the spike,
give an alternative route or tool, or lower the variance (more predictable tells) rather than
the average difficulty.

## Failure design

Failure keeps players in flow when it's **fair** (the cause can be read), **fast** (quick
retry), and **informative** (the player learns what to change). Failure pushes players out
when it's random, slow to recover from, or costs progress they can't win back. Roguelites
turn failure into progress (meta unlocks, a story that advances on death). Competitive games
show what went wrong (death recaps, replays).

## Hard fun and frustration

Lazzaro's *Hard Fun* depends on frustration building before triumph (*fiero*). Frustration
isn't the enemy. **Unproductive** frustration is: no sense of improving, unclear cause, or no
way forward. Look for signs that players are making progress between failures (better runs,
new strategies). If attempts don't improve, the challenge has moved from hard to unfair.

## Sources

- [A2] Csikszentmihalyi (1990), *Flow: The Psychology of Optimal Experience*.
- [A3] Chen (2007), *Flow in Games (and Everything Else)*, Communications of the ACM 50(4). doi:10.1145/1232743.1232769
- [A6] Lazzaro (2004), *Four Keys to More Emotion*: hard fun and fiero.
- [A13] Thorson (2020), *Celeste & Forgiveness*. https://maddymakesgames.com/articles/celeste_and_forgiveness/
- [A16] Cook (2007), *The Chemistry of Game Design*: skill atoms.
- [D10] Schatz & Gallant (2020): accessibility vs. difficulty in The Last of Us Part II.
- [B25] King: difficulty pacing across match-3 levels.
- Full bibliography: `research/SOURCES.md` in the repository.
