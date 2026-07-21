# Zara Sales Dataset — Exploratory Data Analysis (Report Formatting (only) by AI)

**Dataset:** 20,252 records · 17 features
**Tools:** Python (pandas, seaborn, matplotlib)

---

## Table of Contents
1. [Dataset Familiarization](#1-dataset-familiarization)
2. [Data Quality](#2-data-quality)
3. [Univariate Analysis](#3-univariate-analysis)
4. [Bivariate Analysis](#4-bivariate-analysis)
5. [Multivariate Analysis](#5-multivariate-analysis)
6. [Business Insights](#6-business-insights)
7. [Data Quality Deep Dive: The URL Anomaly](#7-data-quality-deep-dive-the-url-anomaly)
8. [Final Summary](#8-final-summary)

---

## 1. Dataset Familiarization

**Shape:** 20,252 rows × 17 columns

| Feature | Type | Notes |
|---|---|---|
| Product ID | int | Row identifier — **not** a numeric feature, excluded from numeric summaries |
| Product Position | categorical | Aisle / End-cap / Front of Store |
| Promotion | categorical | Yes / No |
| Product Category | categorical | Constant — all "clothing" |
| Seasonal | categorical | Yes / No |
| Sales Volume | numerical | **Target variable** |
| brand | categorical | Constant — all "Zara" |
| url | text | See [Section 7](#7-data-quality-deep-dive-the-url-anomaly) — **not a product identifier** |
| name | text | Product name |
| description | text | Product description |
| price | numerical | USD |
| currency | categorical | Constant — all "USD" |
| terms | categorical | Product type: jackets, shoes, sweaters, jeans, t-shirts |
| section | categorical | MAN / WOMAN |
| season | categorical | Winter, Autumn, Spring, Summer |
| material | categorical | 11 materials |
| origin | categorical | 12 countries |

**Missing values:** `name` (1), `description` (2). All other columns complete.
**Duplicate rows:** 0.
**Memory usage:** ~2.6 MB.

---

## 2. Data Quality

### Constant columns (no analytical value)
`Product Category`, `brand`, `currency` — single unique value each.

### Categorical value distributions

| Column | Unique Values | Dominant Category | Share |
|---|---|---|---|
| Promotion | 2 | No | 58.3% |
| section | 2 | WOMAN | 65.4% |
| season | 4 | Autumn | 37.8% |
| terms | 5 | jackets | 55.5% |
| Product Position | 3 | Aisle | 38.6% |
| Seasonal | 2 | No | 50.0% |
| material | 11 | Cotton | 19.0% |

### Value ranges
- **price:** $12.00 – $134.99 — realistic for the brand, no impossible values.
- **Sales Volume:** 518 – 1,940 — all positive, no zero/negative entries.

### Data types
All types are appropriate as loaded (`int64`, `float64`, `object`); no conversion required for this analysis.

> **Note:** The `url` column shows only 228 unique values across 20,252 rows. This is investigated in depth in [Section 7](#7-data-quality-deep-dive-the-url-anomaly) — the finding materially affects how the rest of this report should be interpreted.

---

## 3. Univariate Analysis

### Sales Volume
| Metric | Value |
|---|---|
| Mean | 1,097.4 |
| Median | 990 |
| Std Dev | 298.2 |
| Range | 518 – 1,940 |

Distribution is **bimodal**: a primary peak around 850–950 units and a secondary peak around 1,400–1,500 units, with a right-leaning tail.

### Price
| Metric | Value |
|---|---|
| Mean | $41.95 |
| Median | $35.95 |
| Std Dev | $23.38 |
| Range | $12.00 – $134.99 |

Distribution is **right-skewed**, concentrated between $15–$45, with a long tail toward premium items.

### Categorical breakdown
- **Promotion:** 58.3% not promoted, 41.7% promoted.
- **section:** 65.4% WOMAN, 34.6% MAN.
- **season:** Autumn (37.8%) > Winter (25.4%) > Spring (22.4%) > Summer (14.3%).
- **terms:** Jackets dominate at 55.5%; jeans are rare at 3.3%.
- **Product Position:** fairly even — Aisle (38.6%), End-cap (33.5%), Front of Store (27.9%).
- **material:** Cotton, Wool, and Wool Blend lead; Silk and Satin are rare (<1% combined).

---

## 4. Bivariate Analysis

### Price vs. Sales Volume
A moderate negative correlation (**r = -0.34**) — higher-priced items tend toward lower sales volume. This is a real pattern, but see the confounding note in [Section 6](#6-business-insights): promoted items are *also* cheaper on average, so price and promotion effects are entangled here, not cleanly separable.

### Sales Volume by category

| Factor | Effect Strength | Observation |
|---|---|---|
| **Promotion** | Strong | Promoted: 1,412 mean vs. Non-promoted: 872 mean (**+62%**) |
| **Section** | Moderate | WOMAN: 1,136 mean vs. MAN: 1,024 mean |
| **Season** | Mild | Summer (1,185) and Winter (1,175) outperform Autumn (1,043) and Spring (1,046) |
| **Terms** | Weak | All product types cluster around 1,088–1,105 mean |
| **Product Position** | Very weak | Aisle (1,090), End-cap (1,100), Front of Store (1,103) — negligible difference |

### Categorical relationships
- **Promotion rate is consistent across gender** (MAN: 41.2%, WOMAN: 41.9%) and across product type (~41–42% for all terms) — promotions are not targeted by segment.
- **Section distribution is proportional across seasons** — WOMAN represents ~65% of records in every season, indicating no seasonal shift in gender focus.

---

## 5. Multivariate Analysis

### Promotion × Section
| Promotion | Section | Mean Sales | Count |
|---|---|---|---|
| No | MAN | 816 | 4,112 |
| No | WOMAN | 902 | 7,700 |
| Yes | MAN | 1,319 | 2,886 |
| Yes | WOMAN | 1,461 | 5,554 |

Promotion effect is stronger than the gender effect — even promoted men's items (1,319) outsell non-promoted women's items (902).

### Promotion × Season
| Promotion | Season | Mean Sales |
|---|---|---|
| No | Autumn | 830 |
| No | Spring | 830 |
| No | Summer | 935 |
| No | Winter | 937 |
| Yes | Autumn | 1,341 |
| Yes | Spring | 1,342 |
| Yes | **Summer** | **1,520** |
| Yes | **Winter** | **1,522** |

Promotion lift is consistent across seasons but peaks in Summer and Winter.

### Promotion × Terms
Promotion lift is remarkably consistent (~540–550 additional units) regardless of product type — a universal effect, not category-specific.

### Price × Promotion
| Promotion | Average Price |
|---|---|
| No | $44.69 |
| Yes | $38.11 |

Promoted items are priced lower on average — this is important context for the price-volume relationship (see [Section 6](#6-business-insights)).

---

## 6. Business Insights

### What drives Sales Volume?
Promotion is the single strongest lever identified in this dataset, associated with a ~62% lift in average units sold, consistent across gender, season, and product type.

### Price range performance
The $20–$60 range (particularly $25–$45) shows the highest concentration of high-volume products. **Caveat:** promoted items are both cheaper *and* higher-volume in this dataset, so the price-volume relationship is confounded with the promotion effect — this should be read as an observed association, not a proven causal price effect.

### Segment performance
Women's products outperform men's overall, and the strongest segment is promoted women's items in Summer/Winter.

### Seasonal performance
Summer and Winter outperform Autumn and Spring, especially for promoted items — despite Autumn holding the most records.

### Strategic recommendations

| Priority | Recommendation | Rationale |
|---|---|---|
| High | Maintain/expand promotion strategy | Largest, most consistent lift on sales volume |
| High | Emphasize Women's section in inventory & marketing | Outperforms Men's across every cut examined |
| Medium | Maintain presence in the $25–$45 price band | Highest observed volume concentration (confounded with promotion — see caveat above) |
| Medium | Review high-price (>$80) item strategy | Consistently lower volume |
| Low | Re-evaluate in-store product positioning | Negligible measured effect on volume |

---

## 7. Data Quality Deep Dive: The URL Anomaly

During data quality review, `url` was found to have only **228 unique values** across 20,252 rows — an average of ~89 rows per url. The initial hypothesis was that this reflected **repeated sales observations of the same product** (e.g., daily/weekly records).

**This hypothesis was tested and rejected.** For the most frequent url (187 rows), a direct check found:

- **187 of 187 rows had distinct `name` values**
- **125 of 187 rows had distinct `description` values**

If these rows represented one product observed repeatedly, `name` and `description` should have been near-constant. Instead, they are almost entirely different products (e.g., a t-shirt name paired with a jacket description in one row; a sweater name paired with a jeans description in another).

**Conclusion:** `url` does not function as a product identifier in this dataset. What it actually represents — a scraping artifact, a broken upstream join, or something else — is **unresolved** and flagged here as an open data-quality issue rather than a solved one.

**Implication for this report:** the assumption "one row = one product" cannot be relied on anywhere in this analysis. The findings above (promotion effects, price-volume relationship, segment comparisons) are all computed at the row level and remain valid as row-level statistical patterns — but they should not be interpreted as per-product insights until the true meaning of a "row" in this dataset is established.

---

## 8. Final Summary

This dataset of 20,252 records shows several consistent, statistically supported patterns:

- **Promotion is the dominant driver of sales volume**, with an effect that holds across gender, season, and product type (~62% average lift).
- **Women's products outperform men's**, and the strongest-performing combination is promoted Women's items in Summer/Winter.
- **Mid-priced products ($25–$45) show the highest volume concentration**, though this is entangled with the promotion effect and should not be read as a pure price effect.
- **Promotion is applied evenly** across gender and product type — this is not a targeted strategy, it's a broad one.
- **A significant open data-quality issue was identified**: the `url` column, despite having far fewer unique values than rows, does not identify unique products. This was verified directly (not assumed) and is flagged for further investigation before any per-product conclusions are drawn from this data.

---

*Analysis conducted in Jupyter Notebook using pandas, seaborn, and matplotlib.*