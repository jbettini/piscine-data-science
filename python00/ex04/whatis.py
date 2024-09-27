import sys

try:
    assert len(sys.argv) <= 2, \
        "AssertionError: more than one argument is provided"
    if len(sys.argv) == 1:
        print("")
    else:
        nb = int(sys.argv[1])
        print("I'm Odd.") if int(sys.argv[1]) % 2 else print("I'm Even.")
except ValueError:
    print("AssertionError: argument is not an integer")
except AssertionError as msg:
    print(msg)
