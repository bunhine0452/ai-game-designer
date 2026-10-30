# Player motivation models

Use motivation models to describe **why** people play and **what** a design offers them.
Don't use them to put players in boxes. Each model has a scope. Respect it.

## Self-Determination Theory (SDT) and PENS

Ryan, Rigby and Przybylski (2006) found that perceived **autonomy**, **competence** and
**relatedness** in a game each predict enjoyment and the wish to keep playing. They hold
across genres, and they explain *why* a mechanic feels good or bad.

| Need | Satisfied by | Thwarted by |
|---|---|---|
| Autonomy | Meaningful choice, multiple viable strategies, freedom of order, expressive tools | Forced paths, one solved build, obligation loops (dailies that punish absence) |
| Competence | Clear goals, readable feedback, a fair difficulty ramp, visible mastery | Opaque failure, random punishment, difficulty spikes, pay-to-win gaps |
| Relatedness | Co-op, gifting, guilds, characters who react to the player | Toxic matchmaking, social pressure to pay, isolation |

PENS (Player Experience of Need Satisfaction) measures these needs. It is free for academic
use; commercial use needs permission from the Center for Self-Determination Theory.

**Apply it:** for each core feature, mark which need it serves and which it might thwart.
A feature that thwarts a need for many players is a design risk even if it lifts a metric.

## Quantic Foundry Gamer Motivation Model

Built from factor analysis of survey data from hundreds of thousands of gamers. It has 12
motivations in six pairs, which cluster into three higher groups.

| Pair | Motivations | Design hooks |
|---|---|---|
| Action | Destruction, Excitement | Spectacle, pace, surprise, explosive feedback |
| Social | Competition, Community | Ranked play, leaderboards, guilds, co-op |
| Mastery | Challenge, Strategy | Hard content, deep systems, planning, optimization |
| Achievement | Completion, Power | Collections, 100% goals, power growth, gear |
| Immersion | Fantasy, Story | Role, world, characters, narrative choice |
| Creativity | Design, Discovery | Building, customization, exploration, experimentation |

The higher clusters are Action–Social, Mastery–Achievement and Immersion–Creativity.
*Discovery* bridges Immersion–Creativity and Mastery–Achievement, and *Power* bridges
Action–Social and Mastery–Achievement.

**Apply it:** describe the target audience as the 3–4 strongest motivations (e.g.
"Strategy, Completion, Discovery"). Check that the core loop serves the top two and that no
pillar works against them. The full item set is proprietary, so don't reproduce the survey.
Refer people to Quantic Foundry's profile instead.

## Bartle's player types (with context)

Bartle (1996) described four play styles **in MUDs** on two axes: acting on vs.
interacting with, and the world vs. other players.

- **Achievers** act on the world (points, levels, treasure).
- **Explorers** interact with the world (mechanics, secrets, maps).
- **Socialisers** interact with players (conversation, relationships).
- **Killers** act on players (competition, domination, sometimes griefing).

Bartle's main point was about *balance in a shared world*: the populations affect each other
(too many killers drive off socialisers, and so on). Treat it as an ecosystem lens for
multiplayer spaces, not a personality test or a market segmentation. For single-player
games, prefer the Quantic Foundry or SDT lenses.

## Audience sketch template

```
Primary audience: <who, in one line>
Top motivations (QF): 1) ___ 2) ___ 3) ___
SDT needs served: autonomy ___ / competence ___ / relatedness ___
Session context: where, when, for how long, on what device
What they will NOT tolerate: ___ (e.g. losing progress, reading long text, PvP)
Reference games they already love: ___ (and the reason for each)
```

## Common mistakes

- **Designing for "everyone".** Pick a core audience. Breadth comes from accessible
  onboarding, not a diluted core loop.
- **Equating motivation with monetization.** Power-motivated players aren't "whales". Don't
  build spending pressure on a motivation profile.
- **Treating extrinsic rewards as the motivation.** Points and badges help only when they
  signal competence or progress the player cares about. Otherwise they crowd out the
  intrinsic reasons to play.

## Sources

- [A9] Ryan, Rigby & Przybylski (2006), *The Motivational Pull of Video Games: A Self-Determination Theory Approach*, Motivation and Emotion 30(4). doi:10.1007/s11031-006-9051-8
- [A8] Quantic Foundry, Gamer Motivation Model. https://quanticfoundry.com/2015/12/21/map-of-gaming-motivations/
- [A7] Bartle (1996), *Hearts, Clubs, Diamonds, Spades: Players Who Suit MUDs*. https://mud.co.uk/richard/hcds.htm
- Full bibliography: `research/SOURCES.md` in the repository.
