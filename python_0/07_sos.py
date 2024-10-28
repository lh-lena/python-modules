import sys

"""
Make a program that takes a string as an argument and encodes it into Morse Code.
• The program supports space and alphanumeric characters
• An alphanumeric character is represented by dots . and dashes -
• Complete morse characters are separated by a single space
• A space character is represented by a slash /
You must use a dictionary to store your morse code.
If the number of arguments is different from 1, 
or if the type of any argument is wrong,
the program prints an AssertionError.

Allowed functions: sys or any other library that allows to receive the args.
"""

""" Test cases:
$> python sos.py "sos" | cat -e
... --- ...$
$> python sos.py 'h$llo'
AssertionError: the arguments are bad
$>
"""

NESTED_MORSE = { " ": "/ ",
                 "A": ".- ",
                 "B": "-... ",
                 "C": "-.-. ",
                 "D": "-.. ",
                 "E": ". ",
                 "F": "..-. ",
                 "G": "--. ",
                 "H": ".... ",
                 "I": ".. ",
                 "J": ".--- ",
                 "K": "-.- ",
                 "L": ".-.. ",
                 "M": "-- ",
                 "N": "-. ",
                 "O": "--- ",
                 "P": ".--. ",
                 "Q": "--.- ",
                 "R": ".-. ",
                 "S": "... ",
                 "T": "- ",
                 "U": "..- ",
                 "V": "...- ",
                 "W": ".-- ",
                 "X": "-..- ",
                 "Y": "-.-- ",
                 "Z": "--.. ",
                 "1": ".---- ",
                 "2": "..--- ",
                 "3": "...-- ",
                 "4": "....- ",
                 "5": "..... ",
                 "6": "-.... ",
                 "7": "--... ",
                 "8": "---.. ",
                 "9": "----. ",
                 "0": "----- "
}

def process_str(S) -> int:
    """
    Encodes a string of spaces and alphanumeric characters into Morse Code based on NESTED_MORSE
    """
    s = S.upper()
    res = ""
    for n in s:
        assert (n >= 'A' and n <= 'Z' or n >= '0' and n <= '9' or n == ' '), "the arguments are bad"
        res = res + NESTED_MORSE[n]
    print(res)
    return 1


def main():
    try:

        arg = len(sys.argv)
        assert arg == 2, "the arguments are bad"
        assert process_str(sys.argv[1]) == 1, "the arguments are bad"
    except AssertionError as msg:
        print("AssertionError: ", msg)
        return -1

if __name__ == "__main__":
    main()