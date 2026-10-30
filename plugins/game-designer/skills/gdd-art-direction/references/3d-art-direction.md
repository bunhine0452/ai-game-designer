# 3D art direction, space and camera

In 3D the player sees the world through a moving camera, so art direction, level layout and
camera design are one problem. Decide the style, the **metrics** and the **camera** together,
and test them in greybox before any final art.

## 1. Choose a style you can finish

| Style | Reads well for | Cost drivers | Small-team fit |
|---|---|---|---|
| Low-poly flat or gradient shading | Clean silhouettes, mobile, web | Lighting and color design carry the look | High |
| Stylized toon (cel shading, outlines) | Characters and expressions, bright worlds | A custom shader, outline technique, hand-painted textures | Medium |
| Stylized PBR (painterly materials) | Rich worlds with soft realism | Material authoring, texture memory | Medium–low |
| Realistic PBR | Immersion, simulation | Scanning or sculpting, high asset counts, lighting | Low |

Write the choice as visual pillars with "do / don't" examples, as in `art-direction.md`.

## 2. Budgets (write them down per platform)

- **Triangles** per hero character, per enemy, per prop, and per screen. Web and mobile need
  tight budgets; profile on the weakest target device.
- **Texel density:** one value for the world (for example 512 px per meter), so detail matches
  across assets. Characters can go higher.
- **Draw calls and materials:** fewer, shared materials and texture atlases beat many unique
  ones. Instance repeated props.
- **LOD and culling:** 2–3 LODs for anything that spans distances, fog or a far plane to hide
  the swap.
- **Lighting:** baked where the world is static, real-time for a few key lights. Shadows are
  expensive: limit the casters.

## 3. Metrics before art

Agree on the player's numbers, then build every level from them:

```
Player: 1.8 m tall, 0.5 m radius · walk 4 m/s · run 7 m/s
Jump: 1.2 m high, 3.5 m long (running) · climbable ledge ≤ 1.0 m
Doors: 2.2 m × 1.2 m · corridors ≥ 2.5 m wide (camera room)
Camera: 6 m behind, 2 m above, 60° vertical FOV
```

Greybox with these numbers and test them with the real camera. Gaps that are 10% under the
maximum jump feel fair; exactly at the maximum they feel cheap.

## 4. Camera

- **Choose the camera type for the verbs:** third-person follow (exploration and action),
  fixed or rail (authored framing), top-down or isometric (tactics and readability), first-person
  (immersion and precision aiming).
- **Follow with damping, look ahead:** lead the camera in the direction of travel. Ease
  position and rotation separately. Never snap unless the player asked for it.
- **Avoid occlusion:** pull the camera in, fade walls, or move it when geometry blocks the
  view. Never let the player lose sight of themselves.
- **Respect player control:** if the player rotates the camera, don't fight them right away.
  Wait 1–2 seconds before auto-centering.
- **Comfort:** avoid fast unrequested rotation, roll and heavy bob. Offer FOV, camera-shake and
  motion-blur settings, and keep at least one mode with a stable horizon.

## 5. Readability and wayfinding in space

- **Landmarks:** one tall, unique, visible-from-everywhere object per area (a tower, a tree, a
  lighthouse) that orients the player and pulls them forward.
- **Lead the eye** with light, color, lines in the architecture, and motion (birds, flags,
  particles). The critical path is the brightest or warmest thing on screen.
- **Silhouette and value:** characters and interactables separate from the background by value
  first, then by color. Grayscale-test screenshots from the real camera.
- **Affordances:** climbable, breakable and dangerous surfaces each get one consistent visual
  language (a color, a trim, a material), taught once and never broken.
- **Scale cues:** doors, stairs and props at real-world sizes so players can judge distance and
  jumps.

## 6. Color script and lighting

Plan the emotional arc of the game as a strip of key colors per level or beat: calm and open,
then tense and narrow, then a climax with the strongest contrast. Pair it with the interest
curve (`fun-curve`). Key light sets the mood, fill keeps shadows readable, and rim light
separates characters from the background.

## 7. Style guide block (copy into the style guide)

```
Style: low-poly, flat shading, gradient sky, fog to 80 m · 1 key + ambient, baked AO
Budgets (web): hero 3k tris, enemy 1.5k, prop ≤ 800, ≤ 150 draw calls per frame
Texel density: 256 px/m (world), 512 px/m (hero) · palette textures, no normal maps
Metrics: see above · Camera: third-person, damped follow, look-ahead 1.5 m, occlusion fade
Reserved: gold = collectible, red-orange = danger, cyan = interactable
Comfort: FOV slider 60–90°, shake toggle, no camera roll
```

## Sources
- [D19] Totten, C. W. (2019). *An Architectural Approach to Level Design* (2nd ed.). CRC Press.
- [D20] Haigh-Hutchinson, M. (2009). *Real-Time Cameras: A Guide for Game Designers and Developers*. Morgan Kaufmann.
- [D21] Nesky, J. (2014). *50 Game Camera Mistakes*. GDC 2014.
- [D22] Keren, I. (2015). *Scroll Back: The Theory and Practice of Cameras in Side-Scrollers*. GDC 2015.
- [D5] TF2 readability; [D6] *The Art of Journey* (color and landmarks); [A11] Swink, *Game Feel*.
- Full bibliography: `research/SOURCES.md` in the repository.
