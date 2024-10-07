import numpy as np


class calculator:
    



def main():
    """Tester for this exercice."""
    try:
        a = [5, 10, 2]
        b = [2, 4, 3]
        calculator.dotproduct(a,b)
        calculator.add_vec(a,b)
        calculator.sous_vec(a,b)
    except BaseException as e:
        print(f"An exception has been caught: {type(e).__name__} - {str(e)}")


if __name__ == "__main__":
    main()
