from pandas import DataFrame
from load_csv import load
import matplotlib.pyplot as plt

def get_datas(country: str, df: DataFrame) -> list:
    data = df[df['country'] == country]
    assert not data.empty, "Assertion Error: Invalid Country"
    return list(data.iloc[0, 1:].values)


def display_country(country1: str, country2: str, df: DataFrame):
    years = [year for year in df.columns if year.isdigit() and int(year) <= 2050]
    
    data1 = get_datas(country1, df)[:len(years)]
    data2 = get_datas(country2, df)[:len(years)]
    
    values1 = [float(v[:-1]) for v in data1]
    values2 = [float(v[:-1]) for v in data2]
    
    plt.plot(years, values1, color='g', label=country1)
    plt.plot(years, values2, color='b', label=country2)
    plt.legend(loc='lower right')
    plt.xlabel('Years')
    plt.ylabel('Life Expectancy')
    plt.title("Population Projections")
    plt.xticks(years[::40])
    plt.yticks([20, 40, 60], ['20M', '40M', '60M'])
    
    plt.show()


def main():
    try:
        df = load("../Ressources/population_total.csv")
        display_country("France", "Belgium", df)
    except AssertionError as e:
        print(f"{e}")
    except BaseException as e:
        print(f"An exception has been catch: {type(e).__name__}.")


if __name__ == "__main__":
    main()
