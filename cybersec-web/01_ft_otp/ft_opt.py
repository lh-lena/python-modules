import sys

def main():
    try:
        ac = len(sys.argv)
        assert ac == 3, "ft_opt: Invalid input\nUsage: ft_opt [OPTION] [KEY_FILE]"

    except AssertionError as e:
        print(f"Error, {e}")
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    main()