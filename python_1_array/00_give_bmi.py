# Allowed functions : numpy or any lib of table manipulation

# print(dir(np.array))
# help(np)
# help(list)

# list = ["item1", item2]
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets

"""
    * The BMI is calculated by dividing an adult's weight in kilograms by their height in metres squared.

You have to handle error cases if the lists are not the same size, are not int or float...
"""

def process_input(lst: list[int | float]) -> bool:
    
    if not isinstance(lst, list):
        print("Invalid input: wrong data type")
        return False
    for h in lst:
        if not isinstance(h, (int, float)) or h < 0:
            print("Invalid input: wrong data type or negative values")
            return False
    return True

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Takes 2 lists of integers or floats in input and returns a list of Body mass index (BMI) values.
    """
    
    res = []
    if not process_input(height) or not process_input(weight):
        return res
    if len(height) != len(weight):
        print("Invalid input: different list size")
        return res
    for h, w in zip(height, weight):
        bmi = w / (h**2)
        res.append(bmi)

    return res
    # Use a list comprehension for BMI calculation in one line
    # return [w / (h**2) for h, w in zip(height, weight)]

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Accepts a list of integers or floats and an integer representing
    a limit as parameters. It returns a list of booleans (True if above the limit)
    """
    res = []
    if not process_input(bmi):
        return res
    for i in bmi:
        b = True if i > limit else False
        res.append(b)
    return  res
    # Use a list comprehension to directly produce boolean results
    # return [i > limit for i in bmi]

def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

if __name__ == "__main__":
    main()




"""
Your tester.py:
from give_bmi import give_bmi, apply_limit
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
Expected output:
$> python tester.py
[22.507863455018317, 29.0359168241966] <class 'list'>
[False, True]
$>
"""