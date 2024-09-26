import sys

if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
elif not int(sys.argv[1]):
    print("AssertionError: argument is not an integer")
elif len(sys.argv) == 1:
    print("")
else:
    sys.argv[1] % 3 ? print("Im Even.") : print("Im Odd.")
