# Tips Dataset Project

## Dataset

Source: Seaborn built-in dataset — `tips`
Provider: Seaborn example datasets repository.

Load directly in Python using:

```python id="f7sk2m"
import seaborn as sns

df = sns.load_dataset("tips")
```

Official Dataset Repository:
https://github.com/mwaskom/seaborn-data

## Description

The dataset contains restaurant bill and tipping information recorded by a waiter over several days. It is commonly used for exploratory data analysis, filtering, grouping, aggregation, and statistical visualization.

Each row represents a single restaurant bill.

## Features

| Column     | Description                       |
| ---------- | --------------------------------- |
| total_bill | Total bill amount in dollars      |
| tip        | Tip amount in dollars             |
| sex        | Gender of the customer paying     |
| smoker     | Whether the customer was a smoker |
| day        | Day of the week                   |
| time       | Lunch or dinner                   |
| size       | Number of people at the table     |

## Project Overview

This project focuses on basic exploratory data analysis and data manipulation using Pandas. The analysis includes filtering rows based on conditions, sorting data by multiple columns, exploring categorical values, and performing grouped aggregations.

The project also demonstrates how customer behavior and restaurant tipping patterns can be analyzed using simple yet essential data analysis techniques.
