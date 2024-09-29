import sys


def main():
    """
Converts a text to Morse code. Takes a single command-line argument,
consisting of spaces, letters and numbers only.
Prints the corresponding Morse code or an error if the format is incorrect.
"""
    mors = {
            " ": "/ ",
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            "0": "-----"
    }
    try:
        cypher = ""
        assert len(sys.argv) == 2, \
            "AssertionError: the arguments are bad"
        for letter in sys.argv[1]:
            if letter == ' ':
                cypher += mors[letter.upper()]
            elif str.isalnum(letter):
                cypher += mors[letter.upper()] + ' '
            else:
                raise AssertionError("AssertionError: the arguments are bad")
        print(cypher)
    except AssertionError as msg:
        print(msg)
    except BaseException as e:
        print(f"An exception has been catch: {type(e).__name__}")


if __name__ == "__main__":
    main()
