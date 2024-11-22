#!/usr/bin/env python3
import sys
import os
from datetime import datetime
from PIL import Image, UnidentifiedImageError
from PIL.ExifTags import TAGS
import chardet

''' to run with all .jpg images from data directory
find data -name "*.jpg" | xargs ./scorpion.py
'''

def scorpion():
    try:
        ac = len(sys.argv)
        assert ac >= 2, f"Missing file\nUsage: {sys.argv[0]} FILE1 [FILE2 ...]"
        data = parseInput(sys.argv[1:])
        for file in data:
            try:
                image = Image.open(file)
                get_basic_metadata(image)
                get_data_attr(file)
                get_exifdata(image)
            except UnidentifiedImageError as e:
                print(f"{sys.argv[0]}: Error: {e}")
                continue
    except AssertionError as e:
        print(f"{sys.argv[0]}: Error: {e}")
        return -1
    except Exception as e:
        print(f"{sys.argv[0]}: Error: {e}")
        return -1

def get_data_attr(image_path):
    file_stat = os.stat(image_path)
    creation_time = datetime.fromtimestamp(file_stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S')

    print(f"Creation Date: {creation_time}")

def parseInput(argv: str, extension=[".jpg", ".jpeg", ".png", ".gif", ".bmp"]) -> list:
    data = []
    for i in argv:
        if i and any(i.lower().endswith(ext) for ext in extension):
            data.append(i)
    assert data, "Missing file\nUsage: scorpion.py FILE1 [FILE2 ...]"
    return data

def get_basic_metadata(image):
    info_dict = {
        "Filename": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1)
    }
    print()
    for label, value in info_dict.items():
        print(f"{label:25}: {value}")

def get_exifdata(image):
    exif_data = image.getexif()
    if exif_data:
        print("\nEXIF Metadata:")
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            if isinstance(value, bytes):
                value = decode_with_chardet(value)
            print(f"{tag_name}: {value}")
        creation_date = exif_data.get("DateTimeOriginal")
        modification_date = exif_data.get("DateTime")
        print(f"Creation Date           : {creation_date}")
        print(f"Modification Date       : {modification_date}")

    else:
        print("No EXIF metadata found\n")

def decode_with_chardet(value):
    result = chardet.detect(value)
    encoding = result['encoding']
    if not encoding:
        return ""
    return value.decode(encoding, errors='replace')

if __name__ == "__main__":
    scorpion()