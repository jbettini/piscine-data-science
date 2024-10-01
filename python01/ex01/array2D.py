def check_shape(shape: list) -> tuple:
    '''
Verifies that all rows in the list have the same length. 
Returns a tuple with the number of rows and columns.
'''
    rows_len = len(shape)
    cols_len = len(shape[0]) if rows_len > 0 else 0
    for cols in shape:
        assert len(cols) == cols_len, \
             "AssertionError: lisy contain different size for items"
    return (rows_len, cols_len)


def slice_me(family: list, start: int, end: int) -> list:
    """
Slices a sublist from family argument and prints its shape before and after slicing. 
Returns the sliced sublist.
"""
    assert isinstance(family, list), \
        "AssertionError: Argument is not a list"
    (rows, cols) = check_shape(family)
    print(f"My shape is : ({rows}, {cols})")
    sliced = family[slice(start, end)]
    (rows, cols) = check_shape(sliced)
    print(f"My new shape is : ({rows}, {cols})")
    return sliced


def main():
    """
Example usage of slice_me function
"""
    try:
        family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except AssertionError as e:
        print(f"{e}")
    except BaseException as e:
        print(f"An exception has been catch: {type(e).__name__}.")


if __name__ == "__main__":
    main()
