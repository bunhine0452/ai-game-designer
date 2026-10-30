# Placeholder art, sound and feel

Prototype art should serve the art direction's **readability rules**, not try to be final art.

## Procedural art that follows the style guide

- **Shape language first.** Use the style guide's meanings: round = friendly, angular =
  threat. Monster Farm's design said "round things are friends", so every monster is a circle
  with a silhouette cue (droplet = water, big paws = tilling, antennae = glow).
- **Silhouette test in code.** Each unit gets one unique outline element (horn, fin, spikes,
  ears) so it reads even in grayscale.
- **Reserved colors.** Gameplay colors (danger, pickup, rarity) never appear as decoration.
  Keep one accent color for the most important element.
- **SVG for portraits and cards, canvas for worlds.** A small `art(spec)` function returning
  SVG strings gives you dozens of consistent creatures. Remember `xmlns` when drawing SVG onto a
  canvas.

## Sound (WebAudio, no files)

```js
let audio = null;                          // create on the first user gesture
function tone(freq, dur, type = "sine", gain = 0.2) {
  if (!audio) return;
  const t0 = audio.currentTime, g = audio.createGain(), o = audio.createOscillator();
  g.gain.setValueAtTime(gain, t0); g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
  o.type = type; o.frequency.value = freq; o.connect(g); g.connect(audio.destination); o.start(); o.stop(t0 + dur);
}
```

- Distinct sounds for: action confirmed, reward, danger approaching, failure.
- **Every audio cue gets a caption** (with direction if position matters): "[Wet footsteps —
  right]". Low Tide shows captions by default and offers a volume slider.

## Feel (juice) in proportion

- Feedback scaled to consequence: small hit → small flash; climax → screen pulse.
- Plain result reveals for anything involving chance and money: no near-miss theatrics.
- Offer "reduce flashing" whenever anything strobes.

## When to hand off

When the prototype has proven the loop and the team needs production assets, hand off:
- Static key art, posters, banners: an image or canvas-design skill.
- Sprites, animation, engine integration: engine-specific plugins (Godot, Unity, Unreal,
  Phaser).
- Keep the prototype as the behavioral reference and its self-tests as the acceptance
  criteria for the production build.

## Sources

- [D5] TF2 readability and silhouettes; [B31] Riot clarity; [A12] Juice it or lose it;
  [D9] APX second channel; [D13] Overwatch audio as information. Full bibliography:
  `research/SOURCES.md`.
