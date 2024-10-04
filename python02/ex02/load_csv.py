import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    df = pd.read_csv(path)
    print(f"Loading dataset of dimensions {df.shape}")
    return df
