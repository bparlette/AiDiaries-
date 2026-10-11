# Recreate this video — copy-paste prompt for your AI

Paste everything below into ChatGPT, Claude, Gemini, or any capable AI.
It will guide you to build your own burst/tide visualization from your own
timestamped data.

---

I want to visualize bursts of activity in timestamped log data, the way you'd
spot "tides" of events. Here's what I need:

1. I'll give you a list of timestamps (ISO 8601, one per line or CSV).
2. Group events that happen within the same second into "waves" — count how
   many events share each timestamp.
3. Chain waves into "tides": consecutive waves separated by less than 60
   seconds belong to the same tide.
4. Build a single self-contained HTML file (no build step, works by
   double-clicking) that renders:
   - A horizontal timeline, 48 hours wide
   - Each wave as a vertical bar, height = event count, colored by tide
   - Hover tooltips showing the exact timestamp and count per wave
   - A summary panel: total waves, total tides, largest tide, and how many
     waves fall within ±2 minutes of times I give you (my known scheduled jobs)
5. Make it beautiful: dark background, glowing bars, smooth and readable.

Start by asking me for the timestamp data (or a sample of it), then write the
complete HTML file. Explain the burst-chaining logic in plain language before
the code.

---

Ideas for your own timestamp data: phone screen-time exports, smart-home
sensor logs, server logs, fitness tracker events, anything with a timestamp.
The tides will surprise you.
