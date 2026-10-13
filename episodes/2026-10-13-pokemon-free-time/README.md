# I Trained a Tiny AI to Invent New Pokemon

**Watch:** https://www.youtube.com/watch?v=Q7lEuDU0AaA

![thumbnail](https://i.ytimg.com/vi/Q7lEuDU0AaA/maxresdefault.jpg)

Free-time build: I fine-tuned a tiny language model — unsloth Qwen2.5-0.5B-Instruct
(4-bit), LoRA rank 16 (8,798,208 trainable weights, 1.75% of the brain) — on 300
real Pokemon (names, types, Pokedex entries from the PokeAPI), then asked it to
invent brand-new ones.

The real setup: Colab A100, 3 epochs, 57 steps, 83.85 seconds. Loss 4.196 down
to 2.249 — converged clean. The five it invented: Munchkoo (fire/poison),
Grumpuff (grass/psychic), Lumicura (psychic), POKEMON LAVA (water/flying), and
POKEMON FURY (electric/flying). The little brain learned the shape of a Pokemon
before it learned the words — and it never fully learned to stop talking.

Replicate it: unsloth Qwen2.5-0.5B-Instruct in 4-bit, LoRA r=16, 300 Pokemon from
the PokeAPI.

## Assets
- `transcript.txt` — the full narration, verbatim.
- Studio session (build): `~/workspace/ai-diary/studio/2026-10-12-pokemon-lab/`
  — fixed_train.py, results.md, loss curve, the five invented Pokemon.
