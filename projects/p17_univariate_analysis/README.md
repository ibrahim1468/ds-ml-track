# Univariate EDA — Tips Dataset (All working & exploration in my own but report was created with AI)

**Project:** P23 — Univariate EDA (Distributions & Summary Stats)
**Dataset:** `seaborn.load_dataset("tips")` — 244 rows, 7 columns

---

## 1. Dataset Overview

| Column | Type | Description |
|---|---|---|
| total_bill | float64 | Continuous numeric |
| tip | float64 | Continuous numeric |
| sex | category | Nominal |
| smoker | category | Nominal |
| day | category | Nominal |
| time | category | Nominal |
| size | int64 | Discrete numeric (count) |

First 5 rows:

| total_bill | tip | sex | smoker | day | time | size |
|---|---|---|---|---|---|---|
| 16.99 | 1.01 | Female | No | Sun | Dinner | 2 |
| 10.34 | 1.66 | Male | No | Sun | Dinner | 3 |
| 21.01 | 3.50 | Male | No | Sun | Dinner | 3 |
| 23.68 | 3.31 | Male | No | Sun | Dinner | 2 |
| 24.59 | 3.61 | Female | No | Sun | Dinner | 4 |

**Missing values:** None across any column (0/244, 0.0%). No imputation needed.

---

## 2. Summary Statistics (Numeric Columns)

| Stat | total_bill | tip | size |
|---|---|---|---|
| count | 244 | 244 | 244 |
| mean | 19.79 | 3.00 | 2.57 |
| std | 8.90 | 1.38 | 0.95 |
| min | 3.07 | 1.00 | 1 |
| 25% | 13.35 | 2.00 | 2 |
| 50% (median) | 17.80 | 2.90 | 2 |
| 75% | 24.13 | 3.56 | 3 |
| max | 50.81 | 10.00 | 6 |

**Notes:**
- No zero tips recorded — every party in the dataset tipped something.
- Coefficient of variation (std/mean): `total_bill` ≈ 45%, `tip` ≈ 46%. Despite tips being a much smaller absolute value, they're proportionally *more* variable than bill size — tipping behavior is less predictable relative to its own scale.

---

## 3. Outlier Detection (1.5 × IQR Rule)

| Column | Q1 | Q3 | IQR | Lower Bound | Upper Bound | Outliers |
|---|---|---|---|---|---|---|
| total_bill | 13.35 | 24.13 | 10.78 | -2.82 | 40.30 | 9 |
| tip | 2.00 | 3.56 | 1.56 | -0.34 | 5.91 | 9 |
| size | 2.00 | 3.00 | 1.00 | 0.50 | 4.50 | 9 |

**Observations:**
- Lower bounds for `total_bill` and `tip` are negative, which is meaningless in practice — neither variable can go below 0. Only the upper bound is a useful outlier signal for these two.
- The 9 flagged `total_bill` outliers aren't data errors — they correspond to larger parties (avg. party size ≈ 3.78 among outlier rows vs. 2.57 overall). Larger tables naturally produce higher bills; this is a real pattern, not noise.
- `size` is a discrete, low-cardinality variable, so applying a continuous-data rule (IQR) to it is shakier — party sizes of 5–6 get flagged as "outliers" but are just legitimate, less common group sizes.

---

## 4. Distribution Shape

**Histograms + KDE:**
- `total_bill` — right-skewed, most bills fall between \$10–\$25, peak around \$15–\$20, long tail up to \$50.
- `tip` — right-skewed, most tips \$1–\$4, sharp peak around \$2–\$3, tail up to \$10.
- `size` — discrete, dominant peak at size = 2, tapering off for larger parties.

**Boxplots:**
- `total_bill` — median ≈ \$17.80, IQR box roughly \$13–\$24, several high-end outliers.
- `tip` — median ≈ \$2.90, IQR box \$2–\$3.56, multiple high outliers (generous tippers).
- `size` — median = 2, most parties 2–3 people, larger groups appear as outliers due to the discreteness issue noted above.

*(See notebook for the actual histogram/KDE/boxplot grid — 3 rows × 2 columns, one row per numeric column.)*

---

## 5. Categorical Feature Breakdown

**sex**

| | Count | % |
|---|---|---|
| Male | 157 | 64.34 |
| Female | 87 | 35.66 |

**smoker**

| | Count | % |
|---|---|---|
| No | 151 | 61.89 |
| Yes | 93 | 38.11 |

**day**

| | Count | % |
|---|---|---|
| Sat | 87 | 35.66 |
| Sun | 76 | 31.15 |
| Thur | 62 | 25.41 |
| Fri | 19 | 7.79 |

**time**

| | Count | % |
|---|---|---|
| Dinner | 176 | 72.13 |
| Lunch | 68 | 27.87 |

**Key imbalance flags:**
- `Fri` is heavily underrepresented (7.79%, only 19 rows) — any conclusions drawn about Friday-specific behavior should be treated with caution given the small sample.
- `time` skews strongly toward Dinner (72%) over Lunch (28%) — worth keeping in mind for any groupwise comparisons later.

---

## 6. Takeaways

- Dataset is complete — no missing values, no cleaning required at this stage.
- Both `total_bill` and `tip` are right-skewed with legitimate high-end outliers tied to larger party sizes, not data errors.
- `size` being discrete limits how meaningful quantile-based outlier detection is for it.
- Categorical splits are imbalanced in places (`Fri`, `Lunch`) — a factor to account for in bivariate/groupwise analysis (P24).
