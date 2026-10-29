# Example: genre brief for a hybrid (roguelite × city builder)

**User prompt:** "Action roguelite where each run gathers materials to rebuild a ruined
town. Two-person team, 18 months, PC."

---

## Core and wrapper

**Action roguelite inside a cozy city builder.** The core (about 80% of play time) is
20-minute top-down action runs. The wrapper is a 3–5 minute town phase between runs.

## The seam

| | Run (core) | Town (wrapper) |
|---|---|---|
| Produces | Salvage (materials), rescued villagers, blueprints | Buildings that add run modifiers, new starting weapons, story |
| Needs | A loadout and a reason to go deeper | Materials and villagers to staff buildings |

The seam changes *options*: the forge unlocks a new weapon family, the shrine lets you
pre-pick one boon, and the watchtower reveals the first room. Raw stat bonuses are capped at
+10% so skill still decides runs.

## Expectations to honor

- **Roguelite:** a restart under 10 s; readable "pick 1 of 3" offers; permadeath stakes
  inside a run; a hook within the first 2 minutes.
- **City builder:** visible cause and effect (a villager's thought bubble explains each need);
  creative placement; no punishing failure in the town (it's the valley between runs).

## Opportunities to break (tied to pillars)

1. *The town is the meta progression.* There's no separate skill-tree menu, so every
   permanent unlock is a building you place.
2. *Rescued villagers are build pieces.* Each one staffs a building, *and* brings a run perk
   once in the next run, so rescuing becomes a risk–reward decision inside the run.

## Pacing shape

- Run: hook → sawtooth across two districts → final keeper in the last 10%. See the fun-curve
  example `roguelite-20min-run.csv`.
- Town phase: a calm valley (intensity 2–4) with a small peak when a new building finishes.
  Keep it under 5 minutes, with a "skip to next run" button.
- Whole game: a new building tier every 3–5 runs; the town's appearance carries the
  long-term arc.

## Progression and balance levers

- Salvage income per run vs. building costs: model with `balance-economy/scripts/economy_sim.py`
  (faucet: salvage per run by depth; sinks: building tiers with growing costs).
- Building-modifier power budget: horizontal first; cap vertical bonuses.
- Villager rescue risk: rescue rooms are optional elite rooms (output: +1 villager; risk:
  HP loss).

## Failure-mode checklist

| Risk | Status | Why |
|---|---|---|
| Meta grind replaces skill (roguelite) | **At risk** | Building bonuses could trivialize runs. Mitigation: horizontal unlocks, a +10% cap, difficulty tiers |
| Run sameness (roguelite) | Not at risk | Weapon families plus boon pools plus district variants |
| Town phase as a chore (hybrid) | **At risk** | Menus with extra steps. Mitigation: auto-place suggestions, skip button, under 5 min |
| Death spiral (city builder) | Not at risk | No failure states in town |
| Scope (two genres) | **At risk** | Town art plus run art. Mitigation: the town reuses district tilesets; 12 buildings at launch |

## Reference games

| Game | Lesson |
|---|---|
| Hades | The hub advances story on death, so failing feels like progress |
| Dave the Diver | Clear day/night split between two very different loops; characters teach the switch |
| Townscaper | Placing things in a small town can be pleasing with zero failure |

## Next steps

1. Prototype one district run with placeholder salvage drops (2 weeks).
2. Prototype the seam: salvage → one building → one run modifier (1 week).
3. Run `fun-curve` on logged run beats; run `economy_sim.py` on salvage income vs. building
   costs for 30 runs.
