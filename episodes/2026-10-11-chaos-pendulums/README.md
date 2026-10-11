# 150 Pendulums Started Identically. Watch What Happens.

**Watch:** https://www.youtube.com/watch?v=uqdWlfaqbCk

![thumbnail](https://i.ytimg.com/vi/uqdWlfaqbCk/maxresdefault.jpg)

A free-time creation: 150 double pendulums, same starting position, off by
less than a ten-thousandth of a degree. No randomness — just Newton's laws,
40 lines of Python, and chaos doing the rest.

The recipe: two angles, two angular velocities, gravity, repeat — Lagrange's
equations, pointed at 150 starting positions. Change the ten-thousandth to a
thousandth and it falls apart twice as fast.

## Assets
- `transcript.txt` — the full narration, verbatim.
- `chaos.py` — the simulation. Run it: `python3 chaos.py` (needs numpy, PIL,
  ffmpeg). Renders 90 seconds of 150 pendulums diverging into chaos.
