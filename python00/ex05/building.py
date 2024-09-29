import sys


def count(string, fun):
    '''
Return the number of time the method fun is true

Args:
    string (str): The input string.
    fun (callable): A function that returns True for specific characters.
'''
    return sum(1 for char in string if fun(char))


def print_num_char(input_str: str):
    """
Print counts of character types in the input string.

Counts uppercase letters, lowercase letters, digits, spaces,
and punctuation marks, then prints the results.

Args:
    input_str (str): The string to analyze.
"""
    marks = 0

    for i in input_str:
        if i in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            marks += 1

    print(f"The text contains {len(input_str)} characters:")
    print(f"{count(input_str, str.isupper)} upper letters")
    print(f"{count(input_str, str.islower)} lower letters")
    print(f"{marks} punctuation marks")
    print(f"{count(input_str, str.isspace)} spaces")
    print(f"{count(input_str, str.isdigit)} digits")


def main():
    '''
Handle text input, perform character count, and manage exceptions.

Accepts 0-1 command-line arguments.
Prompts for input if none provided.
Calls print_num_char() for analysis.
Handles AssertionError and other exceptions.

Usage:
- Run without arguments to input text interactively.
- Run with one argument to analyze the provided text.
'''
    try:
        txt = None
        assert len(sys.argv) <= 2, \
            "AssertionError: only one or zero arguments is provided"
        if len(sys.argv) == 1:
            print("What is the text to count ?")
            txt = sys.stdin.readline()
            print("\n---\n\"", txt, "\"---\n")
        else:
            txt = sys.argv[1]
        print_num_char(txt)
    except AssertionError as msg:
        print(msg)
    except BaseException as e:
        print(f"An exception has been catch: {type(e).__name__}")


if __name__ == "__main__":
    main()
