# Beseri-AI (Revamped)

This repository is a cleaned and open reimplementation of the original project.
What I changed:
- Replaced protected `core/` modules with a clean implementation (`core/beseriai.py`, `core/logger.py`).
- Added a modern CLI (animated solver, history, web preview).
- Kept original project files backed up at `core_obf_backup/`.
- Full rebrand to Beseri-AI.

Run:
```
python3 main.py
```

Notes:
- The new `BeseriAi` class is a lightweight simulator (echo-based). Replace with real model calls if you have API credentials.
- History saved to `history.json`.
