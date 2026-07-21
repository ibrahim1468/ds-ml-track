# Seaborn Fundamentals — Distributions, Categorical, Relational & Matrix Plots

**Project: P26** — Seaborn (categorical + distribution plots)
**Data:** Synthetic DataFrames throughout, each tailor-built to isolate a specific plotting concept
**Note:** As with P25, no single capstone dataset here — Zara sales is reserved as the shared capstone for P27–P29 (storytelling, Plotly, Streamlit dashboard).

---

## 1. Seaborn Fundamentals

Seaborn is built on top of Matplotlib — every Seaborn plot ultimately produces a Matplotlib Figure/Axes underneath. What it adds: sensible defaults, native pandas DataFrame support (`data=df, x='col', y='col'`), and built-in statistical plotting (confidence intervals, KDEs, regression lines) without manual computation.

**Two function families — a distinction that matters throughout this stage:**
- **Axes-level** (`histplot`, `boxplot`, `scatterplot`, `kdeplot`, `violinplot`, `heatmap`, `regplot`, etc.) — draw onto a single Matplotlib Axes, accept `ax=`, and can be dropped into a custom `plt.subplots()`/GridSpec layout exactly like the P25 work.
- **Figure-level** (`catplot`, `relplot`, `displot`, `lmplot`) — manage their own Figure internally, support automatic faceting (`col=`, `row=`), but do **not** accept `ax=` — they can't be placed inside a custom subplot grid.

This distinction directly determines whether a plot can be embedded in a custom dashboard layout (P25-style GridSpec) or whether it needs to stand alone.

---

## 2. Distribution Plots — `kdeplot`, `rugplot`

Built two overlapping groups (`X ~ N(50, 10)`, `Y ~ N(65, 8)`) and plotted both as KDEs on one Axes via `hue=`, with a `rugplot` showing raw data ticks beneath.

**Finding:** The two distributions visually overlap in the range ~55–58, meaning individual values in that band can't be confidently assigned to either group. A minor secondary bump appeared in one KDE curve — a reminder that KDE smoothing can produce small spurious structure from sampling noise alone at moderate sample sizes (n=100/group), and should always be sanity-checked against the histogram before reading it as real multimodality.

---

## 3. Categorical Plots (Counts) — `countplot` vs `barplot`

- `countplot(x=...)` — counts rows per category (no `y=` needed).
- `barplot(x=..., y=...)` — plots a summary statistic (default: mean) per category, **with automatic error bars** representing the confidence interval around that mean.

Built a `store` (North/South/East/West, uneven row counts) × `daily_sales` dataset.

**Finding:** The store with the widest error bar (East) had both the highest variance and a smaller sample size, making its mean estimate the least statistically reliable — despite East also having the highest average. Bar height (the estimate) and error bar width (the confidence in that estimate) are independent pieces of information, and both should be read together, especially when comparing groups with unequal sample sizes.

---

## 4. Categorical Plots (Spread) — `boxplot`, `violinplot`, `stripplot`, `swarmplot`

All four plotted in a 2×2 grid (axes-level functions + `ax=`, tying back to P25 subplot skills) for the same `store`/`daily_sales` data.

**Finding:** Since the underlying data was generated from `np.random.normal()` per store — genuinely symmetric, unimodal distributions — the violin plots added little beyond what the boxplots already showed. Violin plots earn their value specifically on distributions that are bimodal, skewed, or lumpy; on clean Gaussian data, a boxplot and violin tell nearly the same story in different visual packaging. Choosing a more sophisticated plot type doesn't automatically add information — that depends on the actual shape of the data.

---

## 5. Relational Plots — `lineplot`, `scatterplot`

Built a 30-day, 2-sensor time series with 5 noisy readings per sensor per day, forcing `lineplot` to aggregate.

**Key behavior:** Unlike raw `ax.plot()`, `sns.lineplot()` automatically aggregates repeated y-values at the same x and draws a shaded confidence band around the trend — band width reflects the variability of readings at that point.

**Recommended workflow:** view the scatterplot first to confirm the raw structure looks reasonable (no gaps, no non-random noise patterns), *then* trust the lineplot's smoothed aggregate. Going straight to a smoothed trend without checking the raw points risks trusting an aggregation artifact.

---

## 6. Matrix/Pairwise Plots — `heatmap`, `pairplot`, `jointplot`

Built a 3-numeric-column dataset (`x`, `y = 0.8x + noise`, `z = -0.5x + noise`) plus a `group` column assigned **independently** of the numeric values (`np.random.choice`, no causal link).

- `heatmap(corr, annot=True, cmap='coolwarm')` — correctly shows strong positive (x↔y: 0.85) and negative (x↔z: -0.79) relationships.
- `pairplot(hue='group')` and `jointplot(hue='group')` — marginal distributions for groups A/B/C were nearly fully overlapping.

**Finding:** This near-identical overlap is expected, not a plotting artifact — since `group` was generated with no link to `x`/`y`/`z`, there is no real reason for the groups' marginal distributions to differ, and any small visual wiggle between them is sampling noise. The general lesson: a plot only reveals a real group difference if the data-generating process actually encodes one — always check what a chart *actually* shows against how the underlying data was built, rather than assuming a tool's theoretical capability applies to the case in front of you.

---

## 7. Faceting — `col=` / `row=`

Built a `region` (East/West) × `product` (A/B/C) × `revenue` dataset, plus an optional `quarter` (Q1/Q2) dimension.

- `sns.catplot(x='product', y='revenue', col='region', kind='box')` — auto-generated a 2-panel grid, one boxplot trio per region.
- Adding `row='quarter'` extended this to a 2×2 grid (quarter × region), confirming the product ranking (C > B > A for East; B > C > A for West) held consistently across both quarters.

**Comparison to manual subplots:** what `catplot`'s faceting replaces is the entire manual loop-plus-filter-plus-`ax[i,j]`-indexing pattern used in P23/P25 — one declarative call produces the full grid instead of hand-written iteration.

---

## 8. Regression Plots — `regplot`, `lmplot`

Built two groups with deliberately different slopes (`A: y = 2x + noise`, `B: y = 0.3x + noise`), plotted via `lmplot` two ways: overlaid (`hue='group'`) and faceted (`col='group'`).

**Finding:** For directly comparing slope steepness between groups, the **overlaid** (`hue=`) version is more effective — both regression lines sit on shared axes, making the difference immediately visible at a glance. Faceted panels are better suited to cases where overlapping scatter clouds would obscure each other, or when comparing raw point density matters more than direct slope comparison.

**Caveat:** a regression line will fit itself to any scatter of points, including ones with no real linear relationship — `regplot`/`lmplot` visualize what a linear fit *would* look like, they don't validate that the relationship is genuinely linear.

---

## 9. Styling & Palettes

Three palette types, each suited to a different kind of data:
- **Qualitative** (`'Set2'`, `'tab10'`) — distinct, unordered colors for categories with no inherent order.
- **Sequential** (`'Blues'`, `'viridis'`) — ordered/continuous data where "darker = higher."
- **Diverging** (`'coolwarm'`, `'RdBu'`) — data with a meaningful zero/center point in both directions, e.g. correlation matrices.

**Finding:** Replotting the correlation heatmap from Step 6 with a sequential palette (`'Blues'`) instead of diverging (`'coolwarm'`) caused the sign of each correlation to become visually indistinguishable — a strong negative correlation (-0.79) and a strong positive one (+0.79) would both render as similarly "dark," since sequential palettes encode only magnitude. Diverging palettes are required whenever the sign of a value carries meaning, not just its size.

---

## 10. Key Takeaways

- Axes-level vs Figure-level is the single most important distinction in Seaborn — it determines whether a plot can be embedded in a custom dashboard layout or must stand alone.
- Confidence intervals (bar plot error bars, lineplot shaded bands) carry real information about estimate reliability — always read them alongside the point estimate itself, especially with unequal sample sizes.
- Fancier plot types (violin over box, pairplot over scatter) only add value when the underlying data's shape actually warrants it — check before assuming.
- Any observed "difference" in a plot should be traceable back to how the data was actually generated — a plot can only show a real pattern if the data-generating process actually encodes one.
- Palette type (qualitative/sequential/diverging) must match the semantic type of the data being encoded, or the most important feature (e.g., sign of a correlation) can be visually erased.

**Next:** P27 — Storytelling with data (EDA report on a real dataset), followed by P28 (Plotly) and P29 (Streamlit dashboard) — all converging on the Zara sales capstone.
