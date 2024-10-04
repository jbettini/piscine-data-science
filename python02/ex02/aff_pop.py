from pandas import DataFrame
from load_csv import load
import matplotlib.pyplot as plt


def get_datas(country: str, df: DataFrame) -> list:
    """
Extract and return life expectancy data
for a specified country from the given DataFrame.
"""
    data = df[df['country'] == country]
    assert not data.empty, "Assertion Error: Invalid Country"
    return list(data.iloc[0, 1:].values)


def plot_population_projections(country1: str, country2: str, df: DataFrame):
    """
Generate and display a comparative plot of population
projections up to 2050 for two specified countries.
"""
    years = [
        year for year in df.columns
        if year.isdigit() and int(year) <= 2050
    ]
    data1 = get_datas(country1, df)[:len(years)]
    data2 = get_datas(country2, df)[:len(years)]
    values1 = [float(v[:-1]) for v in data1]
    values2 = [float(v[:-1]) for v in data2]
    plt.plot(years, values2, color='b', label=country2)
    plt.plot(years, values1, color='g', label=country1)
    plt.legend(loc='lower right')
    plt.xlabel('Years')
    plt.ylabel('Population')
    plt.title("Population Projections")
    plt.xticks(years[::40])
    plt.yticks([20, 40, 60], ['20M', '40M', '60M'])
    plt.show()


def main():
    """
Tester for plot_population_projections.
"""
    try:
        df = load("../Ressources/population_total.csv")
        plot_population_projections("France", "Belgium", df)
    except AssertionError as e:
        print(f"{e}")
    except BaseException as e:
        print(f"An exception has been catch: {type(e).__name__}.")


if __name__ == "__main__":
    main()
