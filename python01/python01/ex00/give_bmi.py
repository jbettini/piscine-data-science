def give_bmi(height: list[int | float], weight: list[int | float]) \
                -> list[int | float]:
    """
Calculates BMI for given lists of heights and weights.
Ensures valid input types and returns a list of BMI values.
"""
    assert len(height) == len(weight), \
        "AssertionError: Invalid number of arguments"
    lst: list[int | float] = []
    for h, w in zip(height, weight):
        if not isinstance(h, float) and not isinstance(h, int):
            raise AssertionError("AssertionError: Invalid type of arguments")
        elif not isinstance(w, float) and not isinstance(w, int):
            raise AssertionError("AssertionError: Invalid type of arguments")
        bmi = w / (h * h)
        lst.append(bmi)
    return lst


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
Checks if each BMI in the list exceeds the given limit.
Returns a list of booleans indicating the result for each BMI.
"""
    lst: list[bool] = []
    for element in bmi:
        if not isinstance(element, float) and not isinstance(element, int):
            raise AssertionError("AssertionError: Invalid type of arguments")
        lst.append(element > limit)
    return lst


def main():
    """
Example usage of give_bmi and apply_limit functions.
Calculates BMI and checks if they exceed a limit.
"""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    try:
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except AssertionError as e:
        print(f"{e}")
    except BaseException as e:
        print(f"An exception has been catch: {type(e).__name__}.")


if __name__ == "__main__":
    main()
