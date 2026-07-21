# P16 — Time-Indexed Data: Resampling & Rolling Windows

**Dataset:** Daily Minimum Temperatures, Melbourne, Australia (1981–1990) — 3,650 daily readings.

## Objective
Practice the two core time-series operations pandas provides for a properly indexed date series: **resampling** (changing the frequency of the data) and **rolling windows** (smoothing noisy data at its native frequency).

## Data Preparation

The dataset required real cleaning before either technique could be applied honestly:

1. **Datetime index.** The `Date` column was converted to `datetime64` and set as the DataFrame index, confirmed via `df.info()` and `df.index` before proceeding.

2. **Missing calendar dates.** Comparing the index against a full `pd.date_range` revealed two missing dates — `1984-12-31` and `1988-12-31`. The DataFrame was reindexed onto the complete date range so these gaps became explicit `NaN` rows rather than silently disappearing from any later resample.

3. **A masked data-quality issue.** The `Temperature` column loaded as `object` dtype, not numeric — a signal something was wrong before any numeric operation was attempted. Coercing to numeric surfaced 3 additional missing values, all in **July** (Melbourne winter). Inspecting the raw file bytes showed each was a literal `?` character standing in for what was almost certainly a negative sign (e.g. `?0.2` → `-0.2°C`), consistent with plausible winter minimums and confirmed against the raw byte content of the source file rather than assumed. These were corrected before converting to numeric.

4. **Interpolation.** The remaining 2 missing values (the calendar gaps) were filled using linear interpolation, which respects the surrounding trend — appropriate for a single missing point in an otherwise continuous, smoothly-varying series. Interpolated values were spot-checked against their neighboring days for plausibility.

**Result:** a complete, correctly-typed daily series with zero missing values and no unexplained data-quality issues.

## Resampling

The daily series was resampled to monthly averages (`resample('ME').mean()`), collapsing 3,650 daily readings into 120 monthly values (12 months × 10 years).

The resulting plot clearly shows Melbourne's Southern Hemisphere seasonality — temperature peaks around December–February and troughs around June–August, repeating consistently across all 10 years.

## Rolling Windows

A 30-day rolling mean was computed on the **original daily data** (not the monthly resample — rolling windows and resampling solve different problems and are applied at different frequencies for that reason). Plotted against the raw daily values, the rolling mean visibly smooths day-to-day noise while preserving the underlying seasonal shape.

**Window size behavior:** with `window=30` and default `min_periods`, the first 29 rows of the rolling mean are `NaN` — not because of any calendar-month logic, but because a window of size *N* has no complete *N*-row lookback until row *N* is reached. This is purely a row-count mechanism, independent of dates or calendar units.

**Window size tradeoff considered:** `min_periods=1` was evaluated as an alternative that avoids losing the first 29 days, but was rejected — a rolling "mean" computed from a 1-day or 2-day window isn't comparable in reliability to one computed from a full 30-day window, and blending both under one column would be less honest than leaving the early values as `NaN`.

**Window size comparison:** a 7-day rolling mean was plotted alongside the 30-day rolling mean and the raw daily data. The 7-day mean still shows visible short-term noise and jumps that the 30-day mean smooths out — a direct illustration that window size is a real modeling choice, trading responsiveness to short-term change against stability of the long-term trend.

## Key Takeaways
- A column's reported dtype should never be trusted without verification — `object` where numeric data is expected is a signal to investigate, not a formatting quirk to work around.
- Reindexing onto a complete date range before analysis prevents silent data loss that later resampling/rolling operations would otherwise mask.
- Resampling changes frequency; rolling windows smooth at existing frequency. They are not interchangeable and answer different questions.
- Window size in a rolling calculation is a genuine tradeoff between noise reduction and responsiveness — not just a parameter to set and forget.
