import sys
from ft_filter import ft_filter

# The program must contain at least one list comprehension expression 
# and one lambda.

def filterstring(s, n):
    """
    Returns a list of words from S that have a length greater than N.
    """
    new_list = ft_filter(lambda x: len(x) > n, s)
    return new_list

def main():
    try:
        l = len(sys.argv)
        assert l == 3, "AssertionError: the arguments are bad"
        length = int(sys.argv[2])
    except AssertionError as msg:
        print(msg)
        return -1
    except ValueError:
        print("AssertionError: the arguments are bad")
        return -1
    string = sys.argv[1]
    word_list = string.split()
    print(filterstring(word_list, length))
    

if __name__ == "__main__":
    main()

"""
Expected outputs:
$> python3 06_filterstring.py 'Hello the World' 4
['Hello', 'World']
$>
$> python3 06_filterstring.py 'Hello the World' 99
[]
$>
$> python3 06_filterstring.py 3 'Hello the World'
AssertionError: the arguments are bad
$>
$> python3 06_filterstring.py
AssertionError: the arguments are bad
$>
"""