import sys

if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
elif len(sys.argv) == 1:
    print("")
else:
    try:
        nb = int(sys.argv[1])
        print("I'm Odd.") if int(sys.argv[1]) % 2 else print("I'm Even.")
    except ValueError:
        print("AssertionError: argument is not an integer")
