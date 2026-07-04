# Diamonds Dataset

## Dataset

Source: Seaborn built-in dataset — `diamonds`
Provider: Based on the ggplot2 diamonds dataset containing pricing and quality information for diamonds.

Load directly in Python using:

```python id="f2n3ke"
import seaborn as sns

df = sns.load_dataset("diamonds")
```

Official Dataset Repository:
https://github.com/mwaskom/seaborn-data

## Description

The dataset contains information about the characteristics and prices of nearly 54,000 diamonds. It is widely used for exploratory data analysis, regression modeling, feature engineering, and data visualization.

Each row represents a single diamond.

## Features

| Column  | Description                                                  |
| ------- | ------------------------------------------------------------ |
| carat   | Weight of the diamond                                        |
| cut     | Quality of the cut                                           |
| color   | Diamond color grading                                        |
| clarity | Measurement of diamond clarity                               |
| depth   | Total depth percentage                                       |
| table   | Width of the top of the diamond relative to the widest point |
| price   | Price in US dollars                                          |
| x       | Length in mm                                                 |
| y       | Width in mm                                                  |
| z       | Depth in mm                                                  |

## Cut Quality Categories

* Fair
* Good
* Very Good
* Premium
* Ideal

## Notes

* The dataset contains both categorical and numerical features.
* Useful for regression tasks such as predicting diamond prices.
* Some rows may contain unusual or extreme values that are suitable for outlier analysis exercises.

## Saving as CSV

To export the dataset locally:

```python id="8zpr2a"
import seaborn as sns

df = sns.load_dataset("diamonds")

df.to_csv("data/diamonds.csv", index=False)
```

Place the dataset as:

```text id="qj8m2p"
data/diamonds.csv
```
