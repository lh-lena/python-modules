import sys

def ft_filter(func, iterable):
    """
    Returns a sequence from those elements of iterable for which function returns True
    """
    new_list = [x for x in iterable if func]
    return new_list

def main():
    try:
        n = len(sys.argv)
        assert n == 3, "the arguments are bad"
    except AssertionError as msg:
        print(msg)
    print(ft_filter.__doc__)


if __name__ == "__main__":
    main()

