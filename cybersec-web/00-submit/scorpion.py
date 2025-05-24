#!/usr/bin/env python3
import sys
import os
import time
from datetime import datetime
from PIL import Image, UnidentifiedImageError
from PIL.ExifTags import TAGS
from colorama import Fore, Style

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
                get_date_attr(file)
                get_exifdata(image)
            except UnidentifiedImageError as e:
                print(f"{Fore.RED}{sys.argv[0]}: Error: {e}{Style.RESET_ALL}")
                continue
    except AssertionError as e:
        print(f"{Fore.RED}{sys.argv[0]}: Error: {e}{Style.RESET_ALL}")
        return -1
    except Exception as e:
        print(f"{Fore.RED}{sys.argv[0]}: Error: {e}{Style.RESET_ALL}")
        return -1

def get_date_attr(image_path):
    file_stat = os.stat(image_path)
    creation_time = datetime.fromtimestamp(file_stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S')

    print(f"  Creation Date: {creation_time}")

def parseInput(argv: str, extension=[".jpg", ".jpeg", ".png", ".gif", ".bmp"]) -> list:
    data = []
    for i in argv:
        if i and any(i.lower().endswith(ext) for ext in extension):
            data.append(i)
    assert data, "Missing file\nUsage: scorpion.py FILE1 [FILE2 ...]"
    return data

def get_basic_metadata(image: Image):
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
        print(f"  {label}: {value}")

def get_exifdata(image: Image):
    exif_data = image._getexif()
    if exif_data:
        print(f"{Fore.BLUE}\nEXIF Metadata:{Style.RESET_ALL}")
        exif = {}
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            exif[tag_name] = value
        for tag, value in exif.items():
            print(f"  {tag}: {value}")

    else:
        print(f"{Fore.YELLOW}No EXIF metadata found\n{Style.RESET_ALL}")

if __name__ == "__main__":
    scorpion()