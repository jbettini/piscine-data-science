import numpy as np


class calculator:

    def __init__(self, ar: np.array):
        self.v = ar

    def __add__(self, object) -> None:
        for i in range(len(self.v)):
            self.v[i] += object
        print(self.v)

    def __mul__(self, object) -> None:
        for i in range(len(self.v)):
            self.v[i] *= object
        print(self.v)

    def __sub__(self, object) -> None:
        for i in range(len(self.v)):
            self.v[i] -= object
        print(self.v)

    def __truediv__(self, object) -> None:
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
