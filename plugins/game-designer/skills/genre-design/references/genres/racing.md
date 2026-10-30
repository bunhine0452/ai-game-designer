# Racing

Covers arcade racing, simulation racing, kart racing with items, open-world racing, and
time-trial or skill racers.

> **Sourcing note:** few primary designer talks on racing design turned up in this research
> pass. This playbook rests on general principles (flow, catch-up mechanics, game feel) and
> fan-datamined item data marked as low-trust. Treat specifics as hypotheses to playtest.

## Core loop
Race → take a racing line, brake, drift or boost → overtake or defend → finish → reward
(position, time, currency) → upgrade or unlock a car or track → next event.

## Signature mechanics
- Vehicle handling model: grip, drift, weight transfer, boost.
- Track design: corners, straights, shortcuts, hazards, elevation.
- Opponent AI and **catch-up**. *Rubber banding* adjusts AI speed relative to the player.
  Kart racers also weight item odds by race position (trailing players get stronger items,
  according to fan-datamined tables).
- Time trials and ghosts; drift scoring; nitrous management.
- Car progression: tuning, upgrades, collections.

## Pacing shape
Race: start (pack chaos, a peak) → mid-race spread (a valley, or rhythm through corners) →
final lap tension (climax), helped by catch-up keeping the pack close. Season or campaign:
cups and championships with a final event.

## Progression model
Vehicle and track unlocks, upgrade trees, career or championship structure, cosmetic
collection. Sims focus on mastery (lap times); arcade on unlocks.

## Balancing levers
- Handling forgiveness (assists: steering, braking, rewind).
- Catch-up strength: AI rubber banding, position-weighted items, slipstream.
- Vehicle class balance (speed vs. acceleration vs. handling).
- Track difficulty (corner density, hazard placement).
- Reward per position.

## Failure modes
- **Invisible rubber banding:** the leader feels robbed and the AI feels like it cheats.
- **Random late-race reversals** (a leader-targeting item at the last moment). Exciting for
  the pack, but bitter for the leader, which makes it a classic party-vs-skill tension.
- **Lonely races:** the pack spreads out and there's nobody to race.
- **Handling that's either floaty or punishing**, without assists.
- **Grindy car progression** that holds back the fun of racing.

## Reference games (and why they work)
| Game | Why it works |
|---|---|
| Mario Kart series | Position-weighted items keep skill gaps close, which suits parties and families |
| Forza Horizon series | Festival framing, constant events, and assists that scale from casual to sim |
| Burnout series | Rewards aggression (takedowns) and turns crashes into spectacle |
| Trackmania | Pure time-trial mastery plus a level editor and a huge community |

## Design questions
1. Is the game for skill ranking or for close, chaotic fun? Pick the catch-up strength to match.
2. Does the player know why they lost a position?
3. What happens in the middle of a race when the pack spreads?
4. How do assists let a novice and an expert enjoy the same car?

## Sources
- [B29] Mario Kart item distribution (fan-datamined, low trust).
- [A3] Chen: flow channel. · [A11] Swink: handling feel.
- [B30] Cone (2018), Rocket League physics (vehicle physics tuning).
- Full bibliography: `research/SOURCES.md` in the repository.
