# Penguin Dataset

## Dataset

Source: Seaborn built-in dataset — `penguins`
Provider: Palmer Archipelago penguin data collected by Dr. Kristen Gorman and the Palmer Station, Antarctica LTER program

Load directly in Python using:

```python
import seaborn as sns

df = sns.load_dataset("penguins")
```

Official Dataset Repository:
https://github.com/mwaskom/seaborn-data

## Description

The dataset contains measurements for penguin species observed in the Palmer Archipelago, Antarctica. It is commonly used for exploratory data analysis, visualization, classification, and general machine learning practice.

Each row represents a single penguin observation.

## Features

| Column            | Description                           |
| ----------------- | ------------------------------------- |
| species           | Penguin species name                  |
| island            | Island where the penguin was observed |
| bill_length_mm    | Bill length in millimeters            |
| bill_depth_mm     | Bill depth in millimeters             |
| flipper_length_mm | Flipper length in millimeters         |
| body_mass_g       | Body mass in grams                    |
| sex               | Penguin sex                           |
| year              | Observation year                      |

## Species Included

* Adelie
* Chinstrap
* Gentoo

## Notes

* The dataset contains some missing values.
* Numerical features may require cleaning before modeling.
* Useful for classification, clustering, visualization, and feature engineering exercises.

## Saving as CSV

To export the dataset locally:

```python
import seaborn as sns

df = sns.load_dataset("penguins")

df.to_csv("data/penguins.csv", index=False)
```

Place the dataset as:

```text
data/penguins.csv
```
