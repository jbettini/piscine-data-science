import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    df = pd.read_csv(path)
    print(f"Loading dataset of dimensions {df.shape}")
    return df


def main():
    try:
        print(load("../Ressources/life_expectancy_years.csv")[:10])
    except BaseException as e:
        print(f"An exception has been catch: {type(e).__name__}.")


if __name__ == "__main__":
    main()
