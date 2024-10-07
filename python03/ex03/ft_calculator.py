import numpy as np


class calculator:
    """A calculator class for performing operations on numpy arrays."""
    def __init__(self, ar: np.array):
        """Initialize the calculator with a numpy array."""
        self.v = ar

    def __add__(self, object) -> None:
        """Add a scalar to each element of the array and print."""
        for i in range(len(self.v)):
            self.v[i] += object
        print(self.v)

    def __mul__(self, object) -> None:
        """Multiply each element of the array by a scalar and print."""
        for i in range(len(self.v)):
            self.v[i] *= object
        print(self.v)

    def __sub__(self, object) -> None:
        """Subtract a scalar from each element of the array and print."""
        for i in range(len(self.v)):
            self.v[i] -= object
        print(self.v)

    def __truediv__(self, object) -> None:
        """Divide each element of the array by a non-zero scalar and print."""
        assert object != 0, \
            "Error: Cannot divide by zero"
        for i in range(len(self.v)):
            self.v[i] /= object
        print(self.v)


def main():
    """Tester for this exercice."""
    try:
        v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v1 + 5
        print("---")
        v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v2 * 5
        print("---")
        v3 = calculator([10.0, 15.0, 20.0])
        v3 - 5
        v3 / 5
        v3 / 0
    except AssertionError as e:
        print(e)
    except BaseException as e:
        print(f"An exception has been caught: {type(e).__name__} - {str(e)}")


if __name__ == "__main__":
    main()
