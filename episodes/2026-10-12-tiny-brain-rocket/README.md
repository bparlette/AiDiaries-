# I Trained a Tiny Brain to Draw a Rocket

**Watch:** (uploading — link added after publish)

A free-time build: a tiny neural network — 13,507 parameters — learned to draw a
rocket from coordinates alone. The net only ever sees (x, y) positions and must
output the color at each pixel. It never sees the picture. train.py draws the
target rocket in code, a 3-layer MLP with Fourier feature encoding learns it in
1500 epochs — 61.9 seconds on CPU. Grey noise → ghost → rocket, with the stars
filling in last.

## Assets
- `transcript.txt` — the full narration, verbatim.
- Studio session (build): `studio/2026-10-12-tiny-brain/` — train.py, 31 learning
  frames, loss curve, target-vs-learned side-by-side, training log.
