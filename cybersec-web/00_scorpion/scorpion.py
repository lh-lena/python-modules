import exif
import sys

def main():
    try:
        ac = len(sys.argv)
        assert ac >= 2, f"Missing file\nUsage: {sys.argv[0]} FILE1 [FILE2 ...]"
        data = parseInput(sys.argv[1:])
        scorpion(data)
    except AssertionError as e:
        print(f"{sys.argv[0]}: Error: {e}")
        return -1
    except Exception as e:
        print(f"{sys.argv[0]}: Error: {e}")
        return -1

def parseInput(argv: str, extension=[".jpg", ".jpeg", ".png", ".gif", ".bmp"]) -> list:
    data = []
    for i in argv:
        if i and any(i.lower().endswith(ext) for ext in extension):
            data.append(i)
    assert data, "Missing file\nUsage: main.py FILE1 [FILE2 ...]"
    return data

def scorpion(data: list):
    for file in data:
        try:
            with open(file, "rb") as f:
                image = exif.Image(f)
                # tags = sorted(image.list_all())
                tags = image.list_all()
                if not tags:
                    print(f"File {file}: No EXIF data found.")
                    continue
            print(f"Metadata from file: {file}")
            for tag in tags:
                if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                    print("%s: %s" % (tag, image.get(tag)))
        except FileNotFoundError:
            print(f"File {file} not found.")
        except Exception as e:
            print(f"An error occurred while processing {file}: {e}")

if __name__ == "__main__":
    main()