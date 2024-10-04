import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    """
Load a CSV file from the given path and return it as a DataFrame.
"""
    df = pd.read_csv(path)
    print(f"Loading dataset of dimensions {df.shape}")
    return df


def main():
    '''
Tester for load functions
'''
    try:
        print(load("../Ressources/life_expectancy_yeas.csv")[:10])
    except FileNotFoundError:
        print("Error: File not found")
        return None
    except BaseException as e:
        print(f"An exception has been catch: {type(e).__name__}.")


if __name__ == "__main__":
    main()
