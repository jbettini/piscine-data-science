from pandas import DataFrame
from load_csv import load
import matplotlib.pyplot as plt


def display_scatter(life: DataFrame, infl: DataFrame):
    """
Displays a scatter plot of life expectancy versus GDP for the year 1900.
"""
    infl_values = infl['1900']
    life_values = life['1900']
    plt.scatter(infl_values, life_values)
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.title("1900")
    plt.xscale('log')
    plt.xticks([300, 1000, 10000])
    plt.gca().set_xticklabels(['300', '1k', '10k'])
    plt.show()


def main():
    """
Tester for plot_population_projections.
"""
    try:
        df_life = load("../Ressources/life_expectancy_years.csv")
        df_infl = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
        display_scatter(df_life, df_infl)
    except AssertionError as e:
        print(f"{e}")
    except BaseException as e:
        print(f"An exception has been catch: {type(e).__name__}.")


if __name__ == "__main__":
    main()
