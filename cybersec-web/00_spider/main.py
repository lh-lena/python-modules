import sys
from spider import parseOptions, scrapePage
from urllib.error import URLError, HTTPError

def main():
    try:
        arg = len(sys.argv)
        assert arg > 1, "spider: missing URL\nUsage: [OPTION]... [URL]..."
        data = parseOptions(sys.argv[1:])
        if data["recursive"]:
            scrapePage(data["url"], data["path"], 1, data["depth"])
        else:
            scrapePage(data["url"], data["path"], 1, 1)

    except AssertionError as msg:
        print("Error: ", msg)
        return -1
    except ValueError as msg:
        print("Error: ", msg)
        return -1
    except TypeError as msg:
        print("Error: ", msg)
        return -1
    except HTTPError as e:
        print(f"Error: {e}")
        return -1
    except URLError as e:
        print(f"Error: {e}")
        return -1
    except IsADirectoryError as msg:
        print("Error: ", msg)
        return -1
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()