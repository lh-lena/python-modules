import exif

def parseInput(argv: str, extension=[".jpg", ".jpeg", ".png", ".gif", ".bmp"]) -> list:
    data = []
    for i in argv:
        if not i or not any(i.lower().endswith(ext) for ext in extension):
            raise Exception("scorpion: Unknown file format")
        data.append(i)
    if not data:
        raise Exception("scorpion: Missing file\nUsage: main.py FILE1 [FILE2 ...]")
    return data

def scorpion(data: list):
    for file in data:
        try:
            with open(file, "rb") as f:
                image = exif.Image(f)
                tags = sorted(image.list_all())
                if not tags:
                    print(f"File {file}: No EXIF data found.")
                    continue
            print(f"Metadata from file: {file}")
            for tag in tags:
                if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                    print("%s: %s" % (tag, image.get(tag)))
        except FileNotFoundError:
            print(f"Error: File {file} not found.")
        except Exception as e:
            print(f"An error occurred while processing {file}: {e}")

