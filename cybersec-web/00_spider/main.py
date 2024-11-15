import sys
from spider import Spider
from urllib.error import URLError, HTTPError

def main():
    try:
        arg = len(sys.argv)
        assert arg > 1, "The arguments are bad"
        sp = Spider(sys.argv[1:])
        
        print(sp.__repr__)
    except AssertionError as msg:
        print("AssertionError: ", msg)
        return -1
    except ValueError as msg:
        print("ValueError: ", msg)
        return -1
    except HTTPError as e:
        print(f"Error code: {e.code}")
        return -1
    except URLError as e:
        print(f"Error: {e.reason}")
        return -1
    

if __name__ == "__main__":
    main()