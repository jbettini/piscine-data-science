import sys
from ft_filter import ft_filter
import string

def main():
    try:
        assert len(sys.argv) == 3, \
            "AssertionError: the arguments are bad 1"
        n = int(sys.argv[2])
        s = sys.argv[1].split(" ")
        del_marks = lambda str : all(char not in string.punctuation \
            and char in string.printable for char in str)
        s1 = ft_filter(del_marks, s)
        del_len = lambda str : len(str) >= n
        print(ft_filter(del_len, s1))
    except AssertionError as msg:
        print(msg)
    except ValueError:
        print("AssertionError: the arguments are bad 2")
    except Exception as msg:
        print(f"An exception has been catch : {msg}")


if __name__ == "__main__":
    main()