# DS/ML Track

A project-based journey from Python/NumPy fundamentals to production-grade ML systems — 128 projects, built one at a time, each with real datasets, real bugs, and real corrections along the way.

This repo is a running log of that process. No project moves forward until it's actually working and understood — not just passing.

## Tech Stack

- **Language:** Python 3.10
- **Core libraries:** NumPy, Pandas, Matplotlib
- **Environment:** conda (`ds-ml-track`)
- **Tools:** Jupyter Notebook, Git

## Structure

Each project lives in its own folder under `projects/`, numbered in the order it was built:

```
projects/
├── p01_setup/
├── p02_vectorization/
├── p03_array_indexing/
├── p04_dot_product/
├── p05_monte_carlo_simulations/
├── p06_calculus101/
├── p07_linear_systems/
├── p08_vector_simulation/
└── ...
```

## Projects

| # | Project | What it covers |
|---|---------|-----------------|
| 1 | [Environment & Git Setup](projects/p01_setup) | Clean conda environment, project structure, `.gitignore` rationale, first commit |
| 2 | [Vectorization vs Loops](projects/p02_vectorization) | Benchmarking Python loops vs NumPy across array sizes, log-log scaling analysis |
| 3 | [Array Indexing & Broadcasting](projects/p03_array_indexing) | Slicing, indexing, NumPy broadcasting rules and failure cases |
| 4 | [Dot Products & Linear Algebra](projects/p04_dot_product) | Dot products, vector norms, angle between vectors, physical interpretation |
| 5 | [Monte Carlo π Estimation](projects/p05_monte_carlo_simulations) | Random sampling, vectorized simulation, convergence and error analysis |
| 6 | [Numerical Calculus](projects/p06_calculus101) | Central difference differentiation, trapezoidal integration, floating-point error behavior |
| 7 | [Linear Systems (Statics)](projects/p07_linear_systems) | Solving `Ax=b` for a real statically-determinate truss problem, `np.linalg.solve` |
| 8 | [Vectorized Random Walk](projects/p08_vector_simulation) | Naive loop vs vectorized simulation using `np.cumsum`, ~100x speedup |

*(Table updated as new projects are completed.)*

## Setup

```bash
conda create -n ds-ml-track python=3.10
conda activate ds-ml-track
pip install -r requirements.txt
``