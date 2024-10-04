from pandas import DataFrame
from load_csv import load
import matplotlib.pyplot as plt


def plot_life_expectancy(country: str, df: DataFrame):
    """
Plot life expectancy projections for a specified
country using data from the given DataFrame.
"""
    data = df[df['country'] == 'France']
    if data.empty:
        print(f"No data found for {country}")
        return
    years = list(data.columns[1:])
    values = data.iloc[0, 1:].values
    plt.plot(years, values, color='g')
    plt.xlabel('Years')
    plt.ylabel('Life Expectancy')
    plt.title(f"{country} Life Expectancy Projections")
    plt.xticks(years[::40])
    plt.tight_layout()
    plt.show()


def main():
    '''
Tester for plot_life_expectancy function.
'''
    try:
        df = load("../Ressources/life_expectancy_years.csv")
        plot_life_expectancy("France", df)
    except BaseException as e:
        print(f"An exception has been catch: {type(e).__name__}.")


if __name__ == "__main__":
    main()
