class calculator:
    """A calculator class for vector operations."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the dot product of two vectors."""
        res = 0
        for (a, b) in zip(V1, V2):
            res += (a * b)
        print(f"Dot product : {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors element-wise."""
        res = [float(a + b) for (a, b) in zip(V1, V2)]
        print(f"Add Vector is : {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract the second vector from the first element-wise."""
        res = [float(a - b) for (a, b) in zip(V1, V2)]
        print(f"Sous Vector is : {res}")


def main():
    """Tester for this exercice."""
    try:
        a = [5, 10, 2]
        b = [2, 4, 3]
        calculator.dotproduct(a, b)
        calculator.add_vec(a, b)
        calculator.sous_vec(a, b)
    except BaseException as e:
        print(f"An exception has been caught: {type(e).__name__} - {str(e)}")


if __name__ == "__main__":
    main()
