import sys
from ft_filter import ft_filter
import string


def main():
    """
Filters words from a space-separated string based on length and punctuation.

Usage:
    python script.py <string> <min_length>

Filters:
1. Removes words with punctuation.
2. Keeps words of length >= <min_length>.

Errors:
- Assertion error for incorrect argument count.
- ValueError if <min_length> is not an integer.

Example:
    python script.py "Hello world!" 5
    Output: ['Hello']
"""
    try:
        assert len(sys.argv) == 3, \
            "AssertionError: the arguments are bad"
        n = int(sys.argv[2])
        s = sys.argv[1].split(" ")
        s1 = ft_filter(
            lambda str: all(
                char not in string.punctuation and char in string.printable
                for char in str
            ),
            s
        )
        print(ft_filter(lambda str: len(str) > n, s1))
    except AssertionError as msg:
        print(msg)
    except ValueError:
        print("AssertionError: the arguments are bad")
    except BaseException as e:
        print(f"An exception has been catch: {type(e).__name__}")


if __name__ == "__main__":
    main()
