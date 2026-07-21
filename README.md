# DS/ML Track

A project-based journey from Python/NumPy fundamentals to production-grade ML systems — 128 projects, built one at a time, each with real datasets, real bugs, and real corrections along the way.

This repo is a running log of that process. No project moves forward until it's actually working and understood — not just passing.

## Tech Stack

- **Language:** Python 3.10
- **Core libraries:** NumPy, Pandas, Matplotlib, Seaborn
- **Environment:** conda (`ds-ml-track`)
- **Tools:** Jupyter Notebook, Git

## Structure

Each project lives in its own folder under `projects/`, numbered in the order it was built. Any project using a real dataset keeps it in a local, gitignored `data/` subfolder — see that project's README for the source/download link.

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
├── p09_SeriesDataFrame/
├── p10_sales_filtering_groupby/
├── p11_merging_joining/
├── p12_missing_values/
├── p13_outliers/
├── p14_feature_derivation/
├── p15_reshaping_melting_multiindex/
├── p16_time_indexed_data/
├── p17_univariate_eda/
├── p18_bivariate_eda/
├── p19_matplotlib_fundamentals/
├── p20_seaborn_categorical_distribution/
├── p21_storytelling_with_data/
├── p22_plotly_interactive_viz/
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
| 9 | [Series/DataFrame Fundamentals](projects/p09_SeriesDataFrame) | Pandas Series vs DataFrame structure, indexing, `.info()`/`.describe()` (Titanic dataset) |
| 10 | [Filtering, Sorting & GroupBy](projects/p10_sales_filtering_groupby) | Boolean filtering, multi-key sorting, per-column groupby aggregations (tips dataset) |
| 11 | [Merge/Join Across Tables](projects/p11_merging_joining) | Inner/left/right/outer joins, mismatch handling, join-induced row duplication |
| 12 | [Handling Missing Data](projects/p12_missing_values) | Missingness diagnosis, per-group imputation via `.transform()`, dropna vs fill tradeoffs (penguins dataset) |
| 13 | [Outlier Detection & Treatment](projects/p13_outliers) | IQR vs Z-score comparison, how skew produces false positives, log-transform as a fix (diamonds dataset) |
| 14 | [Derived Columns & Vectorized Ops](projects/p14_feature_derivation) | `.apply()`/lambda vs vectorized (`np.select`) performance comparison, string ops, chronological time features (flights dataset) |
| 15 | [Reshaping: Pivot/Melt/Multi-Index](projects/p15_reshaping_melting_multiindex) | Long-to-wide-to-long round trips, ordered categorical sorting, multi-index groupby access |
| 16 | [Time-Indexed Data Basics](projects/p16_time_indexed_data) | Resampling, rolling windows, datetime indexing fundamentals |
| 17 | [Univariate EDA](projects/p17_univariate_eda) | Distribution shape, summary statistics, single-variable diagnostics |
| 18 | [Bivariate EDA](projects/p18_bivariate_eda) | Correlation analysis, groupwise comparison across variable pairs |
| 19 | [Matplotlib Fundamentals](projects/p19_matplotlib_fundamentals) | Multi-panel figures, subplot layouts, core plotting API |
| 20 | [Seaborn Categorical & Distribution Plots](projects/p20_seaborn_categorical_distribution) | Categorical plot types, distribution visualization, styling conventions |
| 21 | [Storytelling with Data](projects/p21_storytelling_with_data) | Full EDA report on a real dataset, from cleaning to narrative findings (Olympic history dataset) |
| 22 | [Interactive Viz with Plotly](projects/p22_plotly_interactive_viz) | Interactive plotting, hover/zoom interactions, Plotly Express vs Graph Objects |

*(Table updated as new projects are completed.)*

## Setup

```bash
conda create -n ds-ml-track python=3.10
conda activate ds-ml-track
pip install -r requirements.txt
```
