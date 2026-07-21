# Bivariate EDA — Palmer Penguins Dataset

**Project:** P24 — Bivariate EDA (Correlation & Groupwise Comparison)
**Dataset:** `seaborn.load_dataset("penguins")` — 344 rows, 7 columns

---

## 1. Dataset Overview

Column              Type        Description

species             object      Adelie / Chinstrap / Gentoo
island              object      Torgersen / Biscoe / Dream
bill_length_mm      float64     Continuous numeric
bill_depth_mm       float64     Continuous numeric
flipper_length_mm   float64     Continuous numeric
body_mass_g         float64     Continuous numeric
sex                 object      Male / Female

**Duplicates:** None found.

**Missing values:**

Column              Missing     Percentage
-----------------------------------------
species             00          0.00%
island              00          0.00%
bill_length_mm      02          0.58%
bill_depth_mm       02          0.58%
flipper_length_mm   02          0.58%
body_mass_g         02          0.58%
sex                 11          3.20%

**Notes:**
- Unlike `tips`, this dataset has real missing data. One row (index 3) has all four physical measurements and sex missing simultaneously
- Most likely a single bird whose entire record failed to be captured, rather than five independent missing values.
- `sex` is missing far more often (3.2%) than the physical measurements (0.58%) — likely a different failure mode (harder to determine sex without invasive checks)
- Missing values were left as-is for this stage. Imputation is a modeling decision, not an EDA one — pandas' `.corr()` and `.groupby()` already handle NaNs gracefully - - Filling them now would inject assumptions into data we haven't finished exploring yet.

---

## 2. Numeric vs Numeric — Correlation

                    bill_length_mm  bill_depth_mm   flipper_length_mm   body_mass_g

bill_length_mm      1.00            -0.24           0.66                0.60
bill_depth_mm       -0.24           1.00            -0.58               -0.47
flipper_length_mm   0.66            -0.58           1.00                0.87
body_mass_g         0.60            -0.47           0.87                1.00

- `flipper_length_mm` ↔ `body_mass_g` at **0.87** which makes biological sense, a structurally bigger bird (longer flippers) carries more mass.
- `bill_depth_mm` is negatively correlated with everything else, including body mass (-0.47).
- On the surface this is odd — bigger animals usually have bigger parts across the board, not smaller ones. This became the focus of the groupwise investigation below.

---

## 3. Categorical vs Numeric — Groupwise Comparison

**Mean physical stats per species:**

Species     bill_depth_mm   body_mass_g     flipper_length_mm 

Adelie      18.35           3700.66         189.95
Chinstrap   18.42           3733.09         195.82
Gentoo      14.98           5076.02         217.19

Gentoo is simultaneously the **heaviest, longest-flippered, and shallowest-billed** species — the opposite of what you'd expect if bill depth simply scaled with body size. This asymmetry is the root cause of the negative pooled correlation above.

### Simpson's Paradox — within-species correlation (bill_depth_mm vs body_mass_g)

Group           Correlation

Adelie only     +0.58
Chinstrap only  +0.60
Gentoo only     +0.72

The sign completely flips once species is accounted for. Within every individual species, bill depth and body mass are **positively** correlated, exactly as biological intuition would predict — bigger individuals of the same species have deeper bills. The negative correlation in the pooled data was never a real relationship; it was an artifact of species mixing, since Gentoo occupies a structurally different region of the trait space (big body, shallow bill as a species-level trait) than Adelie/Chinstrap.

**Visual confirmation:**

A scatter plot of `bill_depth_mm` vs `body_mass_g`, colored by species, makes the paradox visible directly: Gentoo forms a distinct cluster (shallow bill, high mass) separate from the shared Adelie/Chinstrap cloud (deeper bill, lower mass) — and within that shared cloud, the trend is clearly positive, not negative. A `sns.pairplot(df, hue='species')` across all numeric variables confirms the same clustering pattern holds broadly across trait pairs.

**Takeaway:** Never trust a pooled correlation at face value when an obvious categorical grouping exists in the data (species, region, segment, etc.) — always check whether the relationship holds *within* each subgroup before drawing conclusions.

---

## 4. Categorical vs Categorical — Cross-tabulation (species × island)

**Raw counts:**

            island	Biscoe	Dream	Torgersen
species			
Adelie	            44	    56	    52
Chinstrap	        0	    68	    0
Gentoo	            124	    0	    0


**Row-normalized (% of each species, by island):**

            island	Biscoe      Dream	    Torgersen
species			
Adelie	            0.289474	0.368421	0.342105
Chinstrap	        0.000000	1.000000	0.000000
Gentoo	            1.000000	0.000000	0.000000

**Column-normalized (% of each island, by species):**

            island	Biscoe	    Dream	    Torgersen
species			
Adelie	            0.261905	0.451613	1.0
Chinstrap	        0.000000	0.548387	0.0
Gentoo	            0.738095	0.000000	0.0

**Findings:**
- **Torgersen** is 100% Adelie — the purest single-species island in the dataset.
- **Biscoe** is Gentoo-dominant (73.8%), with the remainder Adelie.
- **Dream** is the most mixed island, split roughly 45/55 between Adelie and Chinstrap.
- Gentoo and Chinstrap never co-occur on the same island in this dataset — species and island are far from independent.

---

## 5. Key Takeaways

- Flipper length is the strongest single predictor of body mass among the numeric traits (r = 0.87).
- Pooled correlation between bill depth and body mass is misleading (-0.47) due to Simpson's Paradox
- Species is a confounding variable that reverses the true within-group relationship (positive in all three species).
- Species and island are strongly associated, not independent — Gentoo and Chinstrap are geographically segregated, while Adelie is the only species present everywhere
- Missing data (esp. in `sex`) was noted but intentionally left unimputed at this stage — imputation belongs to a later, modeling-focused step.