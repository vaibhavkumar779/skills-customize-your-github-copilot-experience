import pandas as pd
import numpy as np


def load_data(filepath):
    return pd.read_csv(filepath)


def inspect_data(df):
    print("First rows:\n", df.head(), "\n")
    print("Data types:\n", df.dtypes, "\n")
    print("Missing values:\n", df.isnull().sum(), "\n")


def summary_statistics(df, column):
    values = df[column].dropna()
    return {
        "mean": np.mean(values),
        "median": np.median(values),
        "std": np.std(values, ddof=1),
        "variance": np.var(values, ddof=1),
        "min": values.min(),
        "max": values.max(),
    }


def grouped_summary(df, group_col, agg_col):
    return df.groupby(group_col)[agg_col].mean().reset_index()


if __name__ == "__main__":
    filepath = "sample-data.csv"
    df = load_data(filepath)
    inspect_data(df)

    stats = summary_statistics(df, "Value")
    print("Summary statistics for Value:")
    for key, value in stats.items():
        print(f"{key.title()}: {value}")

    group_stats = grouped_summary(df, "Category", "Value")
    print("\nGrouped summary by Category:")
    print(group_stats)
