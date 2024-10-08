import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    """
Load a CSV file from the given path and return it as a DataFrame.
"""
    df = pd.read_csv(path)
    print(f"Loading dataset of dimensions {df.shape}")
    return df
