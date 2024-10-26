import sys
import ft_filter as ft_filter
# The program must contain at least one list comprehension expression 
# and one lambda.

def filterstring(s, n):
    """
    Returns a list of words from S that have a length greater than N.
    """
    new_list = ft_filter(lambda x: (x < n), s)
    return new_list

def main():
    try:
        l = len(sys.argv)
        assert l == 3, "the arguments are bad"
    except AssertionError as msg:
        print(msg)
        return -1
    string = sys.argv[1]
    lenth = sys.argv[2]
    word_list = string.split()
    print(filterstring(word_list, lenth))
    

if __name__ == "__main__":
    main()