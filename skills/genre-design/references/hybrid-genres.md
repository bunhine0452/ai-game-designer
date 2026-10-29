# Hybrid genres: combining playbooks

Many standout games are hybrids: a roguelite city builder, a diving game with a restaurant,
a deckbuilder with tactics. Hybrids are attractive (fresh, marketable) and risky (two sets of
expectations, two content budgets, pacing conflicts).

## Step 1: name the core and the wrapper

- **Core genre:** owns the moment-to-moment loop, where players spend most of their
  minutes.
- **Wrapper genre(s):** own the session or meta loop (management between runs, story between
  missions, collection between matches).

Write it as `<core> inside <wrapper>`, e.g. "action roguelite inside a city builder". If you
can't tell which is core, players won't either. Prototype the core first.

## Step 2: map the loops (the seam)

For each loop, write what it **produces** and what it **needs**:

| | Core loop | Wrapper loop |
|---|---|---|
| Produces | e.g. salvage, XP, story fragments | e.g. upgrades, new options, narrative context |
| Needs | e.g. loadout, buffs, a reason to go | e.g. resources, unlock triggers |

The **seam** is where output from one becomes input for the other. A good seam:
- runs in **both directions** (the core feeds the wrapper, and the wrapper changes the next
  core session);
- changes **options**, not just numbers (a new building unlocks a new run modifier);
- is **visible** (the player sees their run's loot become a building).

Dave the Diver used humor and characters to teach a mix of separate systems (diving by day,
running a restaurant by night). Its director said side activities were added so the day-night
rhythm wouldn't get monotonous.

## Step 3: find the conflicts

| Conflict | Example | Resolution patterns |
|---|---|---|
| **Pacing** | Twitch action vs. slow planning | Separate the phases clearly (day/night, run/hub); let players choose when to switch |
| **Session length** | A 40-min run vs. a 5-min management check-in | Allow a short wrapper session; save mid-run |
| **Input and UI** | Real-time controls vs. menu-heavy management | One input scheme for both; keep wrapper UIs light |
| **Audience** | Action players who dislike menus; sim players who dislike reflex tests | Accessibility and assist options in the weaker genre; let the stronger genre carry identity |
| **Economy** | Wrapper upgrades trivialize the core challenge | Cap wrapper power and favor horizontal unlocks; difficulty tiers |
| **Content budget** | Two genres' worth of assets | Shrink each genre to its essential loop; reuse assets across both |

## Step 4: decide which conventions to keep

Keep each genre's **load-bearing conventions** (the ones without which the genre doesn't work)
and drop the decorative ones:
- From a roguelite, keep fast restarts, readable build offers and permadeath stakes. Drop
  long meta grinds.
- From a city builder, keep visible cause and effect and creative placement. Drop deep
  traffic simulation, unless it is the point.

## Step 5: prototype the seam early

After the core loop is fun by itself, prototype the **seam**: one run's output entering the
wrapper and changing the next run. If the wrapper feels like a menu with extra steps, the
hybrid isn't working yet.

## Hybrid patterns that recur

| Pattern | Examples | What makes it work |
|---|---|---|
| Action core + management meta | Dave the Diver, roguelite hubs | Clear day/night or run/hub split; meta unlocks change runs |
| Card core + tactics or roguelite wrapper | Slay the Spire, Monster Train | Cards give input randomness; the map gives strategic routing |
| Auto-battler / "bullet heaven" | Vampire Survivors | Removing input complexity makes the build the whole game |
| Puzzle core + narrative wrapper | Portal, The Witness | The narrative frames progression without interrupting puzzles |
| Survival core + base-building wrapper | Valheim, Subnautica | The base is safety, sink and expression; the frontier creates risk |
| Social deduction + task game | Among Us | Simple tasks give cover for deception |

## Checklist

- [ ] Core and wrapper named, and the core prototyped first.
- [ ] The seam works both ways and changes options.
- [ ] Each conflict listed, with a resolution.
- [ ] Load-bearing conventions kept for each genre.
- [ ] Content budget fits the team (one genre's worth of work, not two).
- [ ] A one-sentence pitch makes the hybrid obvious ("Hades, but every run rebuilds your town").

## Sources
- [B39] Hwang (2024), *Characters and Humor: Problem-Solving Aid in Dave the Diver* (GDC; recap secondary).
- [B40] Vampire Survivors genre coverage (secondary).
- [A17] Cook (2012), *Loops and Arcs*: loops feeding loops.
- [B2] Giovannetti (2019); [B16] Cleveland (2019).
- Full bibliography: `research/SOURCES.md` in the repository.
