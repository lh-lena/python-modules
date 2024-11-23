import sys

def ft_opt():
    try:
        ac = len(sys.argv)
        assert ac == 3, f"{sys.argv[0]}: Invalid input\nUsage: {sys.argv[0]} [OPTION] [KEY_FILE]\n-g:  to save encrypted key given as argument to file\n-k:  to generate a new temporary password based on the key given as argument"

    except AssertionError as e:
        print(f"Error, {e}")
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    ft_opt()