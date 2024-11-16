import sys
from scorpion import parseInput, scorpion

def main():
    try:
        ac = len(sys.argv)
        assert ac >= 2, "scorpion: Missing file\nUsage: main.py FILE1 [FILE2 ...]"
        data = parseInput(sys.argv[1:])
        scorpion(data)
    except AssertionError as e:
        print(f"Error: {e}")
        return -1
    except Exception as e:
        print(f"Error: {e}")
        return -1

if __name__ == "__main__":
    main()