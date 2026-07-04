# Flights Dataset

## Dataset

Source: Seaborn built-in dataset — `flights`
Provider: Seaborn example datasets repository.

Load directly in Python using:

```python id="q2mf8n"
import seaborn as sns

df = sns.load_dataset("flights")
```

Official Dataset Repository:
[Seaborn Data Repository](https://github.com/mwaskom/seaborn-data?utm_source=chatgpt.com)

## Description

The dataset contains monthly airline passenger counts from 1949 to 1960. It is commonly used for time series analysis, trend visualization, seasonality analysis, pivoting, reshaping, and heatmap visualizations.

Each row represents passenger traffic for a specific month in a specific year.

## Features

| Column     | Description                             |
| ---------- | --------------------------------------- |
| year       | Year of observation                     |
| month      | Month of observation                    |
| passengers | Total airline passengers for that month |

## Time Range

* Start Year: 1949
* End Year: 1960
* Frequency: Monthly

## Notes

* The dataset is already clean and well-structured.
* Ideal for learning time series concepts such as:

  * Trend analysis
  * Seasonality
  * Rolling averages
  * Pivot tables
  * Heatmaps
  * Resampling
* Frequently reshaped between long and wide format for visualization tasks.

## Saving as CSV

To export the dataset locally:

```python id="y7d3lx"
import seaborn as sns

df = sns.load_dataset("flights")

df.to_csv("data/flights.csv", index=False)
```

Place the dataset as:

```text id="9vh3ks"
data/flights.csv
```
