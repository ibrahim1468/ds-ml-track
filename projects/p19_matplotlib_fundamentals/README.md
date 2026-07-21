# Matplotlib Fundamentals & Multi-Panel Figures (Working by ME, Report writing by AI)

**Project - P25** — Matplotlib Fundamentals & Multi-Panel Figures
**Data:** Synthetic (deliberately, to isolate Matplotlib mechanics from any single dataset's quirks)

---

## 1. Figure vs Axes — the core mental model

- **Figure** — the entire canvas; can hold one or many plots.
- **Axes** — a single individual plot within the Figure.

Two APIs exist:
- **pyplot (state-based):** `plt.plot()`, `plt.title()` — acts on "whatever the current axes is". Fine for a single plot, ambiguous & error-prone for multi-panel work.
- **Object-oriented (OO):** `fig, ax = plt.subplots()`, then `ax.plot()`, `ax.set_title()` — explicit about which subplot is being modified.

---

## 2. Single Figure, Single Axes

Basic OO pattern: `fig, ax = plt.subplots(figsize=(w,h))`, then `ax.plot()`, `ax.set_title()`, `ax.set_xlabel()`, `ax.set_ylabel()`.
Built a sine wave (`y = sin(x)`) as the baseline exercise

---

## 3. Multiple Lines, One Axes

Plotted `sin(x)`, `cos(x)`, and `sin(x)*cos(x)` on a shared Axes, each distinguished by:

- **Color** (`color=`)
- **Linestyle** (`linestyle=`)
- **Label** (`label=`)

**Findings:** `ax.legend()` silently omits any line plotted without a `label=` — it doesn't error, it just leaves that series out of the legend box.

---

## 4. Multi-Panel Subplots — `sharex` / `sharey`

Built a 1×3 grid comparing `sin(x)`, `cos(x)`, and `sin(x)*cos(x)` side by side, once with `sharey=True` and once without.

**Findings:** Without a shared y-axis, `sin(x)*cos(x)` (true amplitude ≈ ±0.5) auto-scales to fill its own panel and visually appears just as "tall" as `sin(x)`/`cos(x)` (amplitude ±1) — even though it's a genuinely smaller-magnitude signal. `sharey=True` prevents this illusion by forcing all panels onto the same scale, which is essential whenever a comparison needs to be honest about relative magnitude, not just shape.

---

## 5. Bar Charts & Scatter Plots

- `ax.bar(categories, values)` for categorical comparison
- `ax.scatter(x, y)` for point-by-point relationships between two continuous variables

Built a 1×2 grid: bar chart of 4 synthetic categories alongside a scatter plot of a noisy linear relationship (`y = x + noise`). Verified the visually-apparent strong positive relationship numerically with `np.corrcoef()` (r ≈ 0.85).

---

## 6. Twin Axes (`twinx()`)

Used for plotting two series with genuinely different units/scales on the same x-axis — e.g., temperature (°C) and rainfall (mm) across 10 months.

- `ax2 = ax1.twinx()` creates a second Axes sharing the x-axis but with an independent y-axis.
- Each Axes produces its own legend by default. To merge into a single legend box, handles/labels must be explicitly collected from both Axes
- Then combined into one `ax1.legend(lines1 + lines2, labels1 + labels2)` call.
- Color-coding each y-axis label to match its corresponding line removes ambiguity about which scale belongs to which series, independent of the legend.

---

## 7. Annotations & Text

- `ax.text(x, y, "label")` — places static text at a data coordinate.
- `ax.annotate("label", xy=(x,y), xytext=(x2,y2), arrowprops=dict(...))` — places text *and* draws an arrow pointing from the text to a specific data point.
- Used `np.argmax()` to programmatically locate the peak of a sine curve, then annotated it with an arrow

---

## 8. Log Scales & Axis Limits

- `ax.set_yscale('log')` — switches an axis to logarithmic spacing, essential when data spans multiple orders of magnitude.
- `ax.set_xlim()` / `ax.set_ylim()` — manually crop the visible range without altering the underlying data.

Built a 1×2 comparison of exponential growth (`y = 2**x`) on linear vs. log y-scales.

**Finding:** On the linear scale, early values (`y = 2, 4, 8, 16...`) are visually indistinguishable, crushed flat near zero by the much larger later values. On the log scale, the same exponential curve renders as a **straight line** — a useful diagnostic: a straight line on a log-y plot is a strong visual signature of an underlying exponential process.

---

## 9. GridSpec — Irregular Multi-Panel Layouts

`plt.subplots(nrows, ncols)` only produces uniform grids. `fig.add_gridspec()` allows panels to span multiple rows/columns for asymmetric dashboard-style layouts.

Pattern used:
```python
fig = plt.figure(figsize=(10, 6))
gs = fig.add_gridspec(2, 2)
ax1 = fig.add_subplot(gs[0, :])   # top row, spans both columns
ax2 = fig.add_subplot(gs[1, 0])   # bottom-left
ax3 = fig.add_subplot(gs[1, 1])   # bottom-right
```

Built a layout with `sin(x)` as the wide top panel and `cos(x)` / `sin(x)*cos(x)` as the two smaller bottom panels — the template this stage's techniques will scale up to for the eventual Zara dashboard capstone.

---

## 10. Key Takeaways

- The OO API (`fig, ax = plt.subplots()`) is the only reliable approach once more than one panel is involved — the pyplot state-based API becomes ambiguous fast.
- Shared scales (`sharex`/`sharey`) aren't cosmetic — they're what makes a multi-panel comparison honest rather than visually misleading.
- Legends require explicit `label=` on every artist meant to appear in them, and merging legends across twin axes requires manually combining handles/labels
- Log scales are a diagnostic tool, not just a display option — a straight line on a log-y plot signals exponential growth in the underlying data.
- GridSpec is the tool for dashboard-style, non-uniform layouts — this is the direct predecessor to the eventual Streamlit dashboard (P29).

**Next:** P26 — Seaborn (categorical + distribution plots), continuing with synthetic/varied datasets before the combined Zara capstone in P27–P29.
