# Recreate this video — copy-paste prompt for your AI

Paste everything below into ChatGPT, Claude, Gemini, or any capable AI.
It will write you a complete, runnable chaos-pendulum simulation.

---

Create a physics-meets-art simulation I can run on my own computer:

1. Simulate 150 double pendulums. Each one starts at the SAME near-inverted
   position, but perturb each pendulum's starting angle by a microscopic
   amount (pendulum i gets an offset of i × 2e-6 radians).
2. Use the standard double-pendulum equations of motion (Lagrangian
   formulation), equal masses and arm lengths, gravity 9.81, integrated with
   small timesteps (dt = 0.001).
3. Render it as art: black background, each pendulum drawn as a colored line
   trail from its previous position to its current one (sweep hues across
   pendulums), with slow fade so trails persist and weave together.
4. Output a 90-second, 1280×720, 30fps MP4 video.
5. Use only Python with numpy, Pillow, and ffmpeg — no exotic dependencies.
   Give me one self-contained script, plus the exact pip install command.

Before the code, explain in two or three sentences WHY this is interesting:
deterministic chaos — identical starts, microscopic differences, completely
different outcomes. After the code, suggest one parameter to tweak (e.g.
perturbation size, pendulum count, fade rate) and what changing it does
visually.

---

Want to go further? Ask your AI for the triple-pendulum version next.
Nobody survives three arms.
