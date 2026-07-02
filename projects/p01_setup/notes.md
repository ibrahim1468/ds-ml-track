# Project 1 — Environment Setup & Git Initialization

## Goal
Set up a clean, reproducible project environment and version control before writing any project code.

## What was done

**Environment**
- Created a dedicated conda environment (`ds-ml-track`, Python 3.10), separate from any general-purpose/pre-loaded environment.
- Installed only the minimal packages needed to start: `numpy`, `pandas`, `matplotlib`, `jupyter`.
- Rationale: an isolated, minimal environment keeps `requirements.txt` meaningful — it reflects exactly what this project needs, not an accumulated pile of unrelated packages (streaming libraries, GUI tools, etc.) from unrelated work. This matters for reproducibility: anyone (including future me) can recreate the exact environment from `requirements.txt` without installing dozens of irrelevant dependencies.

**Project structure**
```
ds-ml-track/
├── requirements.txt   # generated via `pip freeze`
├── .gitignore
├── projects/
│   └── p01_setup/
├── README.md
```

**.gitignore**
```
.ipynb_checkpoints/
__pycache__/
*.pyc
```
Rationale: these are auto-generated, non-canonical files (Jupyter checkpoint autosaves, Python bytecode caches). They don't represent intentional work, they add noise to diffs/history, and they can cause spurious merge conflicts across machines/sessions. The real source of truth is the `.ipynb`/`.py` files themselves, not their generated artifacts.

**Version control**
- Ran `git init` inside `ds-ml-track/`.
- First commit included only the structure above (env config, `.gitignore`, empty project folders) — no project code yet, so the commit history cleanly separates "setup" from "actual work."

## Key takeaway
A clean environment and deliberate `.gitignore`/structure decisions aren't busywork — they're what makes every later project reproducible, diffable, and safe to hand off or revisit months later.