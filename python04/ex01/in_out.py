def square(x: int | float) -> int | float:
    """Calculate and return the square of x."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Calculate and return x raised to the power of x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Create a closure that repeatedly applies 'function' to 'x'."""
    count = x

    def inner() -> float:
        nonlocal count
        count = function(count)
        return count
    return inner


def main():
    """Tester for this exercice."""
    try:
        my_counter = outer(3, square)
        print(my_counter())
        print(my_counter())
        print(my_counter())
        print("---")
        another_counter = outer(1.5, pow)
        print(another_counter())
        print(another_counter())
        print(another_counter())
    except BaseException as e:
        print(f"An exception has been caught: {type(e).__name__} - {str(e)}")


if __name__ == "__main__":
    main()
