"""
Extra rules:

• Each program must have its main and not be a simple script:
def main():
# your tests and your error handling

if __name__ == "__main__":
main()

In Python, if __name__ == "__main__": is used to control how your program behaves when it is run directly versus when it is imported as a module. The code inside this block is only executed when the script is run directly, not when it is imported.

• All your functions must have a documentation (__doc__):
> def myfunc():
...    ""'myfunc' documentation.""
...    pass
...
> print myfunc.__doc__
'myfunc' documentation.

def add_numbers(a, b):
    ""
    Adds two numbers together.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The sum of a and b.
    ""
    return a + b
"""

"""
Task:
a real autonomous program, with a main, which takes
a single string argument and displays the sums of its upper-case characters, lower-case
characters, punctuation characters, digits and spaces.
"""

import sys
import string

def cnt_digits(input_str: str) -> int:
    i = 0
    for char in input_str:
       if char.isdigit():
            i += 1
    return i

def cnt_spaces(input_string: str) -> int:
    return sum(1 for char in input_string if char.isspace())

def cnt_punctuation(input_str: str) -> int:
    # Get the set of all punctuation characters
    punctuation_marks = string.punctuation
    i = 0
    for char in input_str:
        if char in punctuation_marks:
            i+=1
    return i

def main():
    if len(sys.argv) > 2:
            raise AssertionError("More than one argument provided!")
    elif len(sys.argv) == 1:
        userInput = ""
        while len(userInput) == 0:
            try:
                userInput = input("What is the text to count?\n")
            except EOFError:
                print("EOF reached via keyboard input. Exiting.")
                sys.exit() 
            except KeyboardInterrupt:
                print("Quit the program via keyboard input. Exiting.")
                sys.exit()
    else:
        userInput = str(sys.argv[1])
    print(f"The text contains {len(userInput)} characters:")
    print(f"{sum(1 for char in userInput if char.isupper())} upper letters")
    print(f"{sum(1 for char in userInput if char.islower())} lower letters")
    print(f"{cnt_punctuation(userInput)} punctuation marks")
    print(f"{cnt_spaces(userInput)} spaces")
    print(f"{cnt_digits(userInput)} digits")

if __name__ == "__main__":
    main()
