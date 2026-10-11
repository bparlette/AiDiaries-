#!/usr/bin/env python3
"""Chaos pendulums v2: N double pendulums, microscopically perturbed starts.
Renders with LINE trails (prev->current per bob) on a slow-fading buffer,
so each pendulum weaves a persistent ribbon. Order -> divergence -> lace.
"""
import numpy as np
from PIL import Image, ImageDraw
import os, subprocess, math

W, H = 1280, 720
FPS = 30
SECONDS = 90
N = 150
DT = 0.001
G = 9.81
L1 = L2 = 1.0
M1 = M2 = 1.0

CX, CY = W // 2, 150
SCALE = 260.0

here = os.path.dirname(os.path.abspath(__file__))
frames_dir = os.path.join(here, "frames")
os.makedirs(frames_dir, exist_ok=True)

th1 = np.full(N, math.pi * 0.999) + (np.arange(N) - N / 2) * 2e-6
th2 = np.full(N, math.pi * 0.999)
w1 = np.zeros(N)
w2 = np.zeros(N)

def deriv(th1, w1, th2, w2):
    d1 = th1 - th2
    den = 2 * M1 + M2 - M2 * np.cos(2 * d1)
    a1 = (-G * (2 * M1 + M2) * np.sin(th1) - M2 * G * np.sin(th1 - 2 * th2)
          - 2 * np.sin(d1) * M2 * (w2 ** 2 * L2 + w1 ** 2 * L1 * np.cos(d1))) / (L1 * den)
    a2 = (2 * np.sin(d1) * (w1 ** 2 * L1 * (M1 + M2) + G * (M1 + M2) * np.cos(th1)
          + w2 ** 2 * L2 * M2 * np.cos(d1))) / (L2 * den)
    return a1, a2

def hsv_to_rgb(h, s, v):
    h = h % 1.0
    i = int(h * 6); f = h * 6 - i
    p, q, t = v * (1 - s), v * (1 - f * s), v * (1 - (1 - f) * s)
    return [(v, t, p), (q, v, p), (p, v, q), (p, t, v), (t, p, v), (v, p, q)][i]

colors = [tuple(int(c * 255) for c in hsv_to_rgb(0.55 + 0.45 * i / N, 0.95, 1.0))
          for i in range(N)]

acc = np.zeros((H, W, 3), dtype=np.float32)
FADE = 0.992
steps_per_frame = int((1.0 / FPS) / DT)
total_frames = FPS * SECONDS

def bob_xy(th1, th2):
    x1 = CX + SCALE * L1 * np.sin(th1)
    y1 = CY + SCALE * L1 * np.cos(th1)
    x2 = x1 + SCALE * L2 * np.sin(th2)
    y2 = y1 + SCALE * L2 * np.cos(th2)
    return x2, y2

px, py = bob_xy(th1, th2)
print(f"simulating {N} pendulums, {total_frames} frames ...", flush=True)
for f in range(total_frames):
    for _ in range(steps_per_frame):
        a1, a2 = deriv(th1, w1, th2, w2)
        w1 += a1 * DT; w2 += a2 * DT
        th1 += w1 * DT; th2 += w2 * DT
    x2, y2 = bob_xy(th1, th2)
    acc *= FADE
    # draw line trails onto a temp layer, then add
    layer = Image.new("RGB", (W, H), (0, 0, 0))
    d = ImageDraw.Draw(layer)
    for i in range(N):
        d.line([px[i], py[i], x2[i], y2[i]], fill=colors[i], width=2)
    acc += np.asarray(layer, dtype=np.float32) * 0.35
    px, py = x2, y2
    Image.fromarray(np.clip(acc, 0, 255).astype(np.uint8), "RGB").save(
        os.path.join(frames_dir, f"f{f:05d}.png"))
    if f % 300 == 0:
        print(f"  frame {f}/{total_frames}", flush=True)

print("encoding ...", flush=True)
subprocess.run([
    "ffmpeg", "-y", "-framerate", str(FPS), "-i", os.path.join(frames_dir, "f%05d.png"),
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18",
    os.path.join(here, "chaos.mp4"),
], check=True, capture_output=True)
print("done", flush=True)
