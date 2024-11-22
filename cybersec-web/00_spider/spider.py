#!/usr/bin/env python3
import os
import sys
import re
import requests
import argparse
from colorama import Fore, Style
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup as BS

tags_attributes = {
    'img': ['src', 'srcset'],
    'source': ['src', 'srcset'],
    'a': ['href'],
    'link': ['href'],
    'div': ['style'],
    'video': ['poster', 'srs'],
	'audio': ['src'],
    'embed': ['src'],
    'background': ['url'],
    'background-image': ['url'],
    'svg': ['href'],
    'span': ['style'],
    'p': ['style'],
    'html': ['style']
}

# pattern = rf'\b(http|ftp|https)://[^\s]+(?:.jpg|.jpeg|.png|.gif|.bmp|.index.html)\b'
# pattern = r'(https?:\/\/[^\s\'"<>]+)'
pattern = r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])'
# pattern = r'(?:https?|ftp):\/\/[^\s\'"<>#]+(?:\.[^\s\'"<>#]+)*(?:\/[^\s\'"<>#]*)?'
# pattern = r'(http|ftp|https):\/\/(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?:\/[^\s\'"<>#=]*)?[^=]'

def spider():
    try:
        parser = argparse.ArgumentParser(
                    prog='spider',
                    description='Image scraping')
        
        parser.add_argument('url', help='URL to a website')
        parser.add_argument('-r', '--recursive', action='store_true', help='Recursively download images')
        parser.add_argument('-l', '--level', type=int, default=5, help='Maximum recursion depth')
        parser.add_argument('-p', '--path', default='./data', help='Download path')

        args = parser.parse_args()
        if args.level < 0:
            raise argparse.ArgumentTypeError(f"{args.level} must be a positive integer")
        log(args.url, args.recursive, 0, args.level)
        print_colored_flags("[INFO]: ", f"Path: {os.path.abspath(args.path)}", Fore.BLUE)
        scrapePage(args.url, args.path, 0, args.level, args.recursive)

    except AssertionError as e:
        print_colored_flags("[ERROR]: ", e, Fore.RED)
        return 1
    except ValueError as e:
        print_colored_flags("[ERROR]: ", e, Fore.RED)
        return 2
    except TypeError as e:
        print_colored_flags("[ERROR]: ", e, Fore.RED)
        return 3
    except IsADirectoryError as e:
        print_colored_flags("[ERROR]: ", e, Fore.RED)
        return 4
    except Exception as e:
        print_colored_flags("[ERROR]: ", e, Fore.RED)
        return 5
    except KeyboardInterrupt:
        print()
        return 6

def log(base_url: str, recursive: bool, depth: int, maxDepth: int):
    print_colored_flags("[INFO]: ", f"Processing: {base_url}", Fore.BLUE)
    print_colored_flags("[INFO]: ", f"Recursive: {recursive}", Fore.BLUE)
    print_colored_flags("[INFO]: ", f"Depth level: {depth + 1}/{maxDepth}", Fore.BLUE)

def scrapePage(base_url: str, pathDir: str, depth: int, maxDepth: int, recursion: bool, extension=[".jpg", ".jpeg", ".png", ".gif", ".bmp"]):
    HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(base_url, headers=HEADERS, allow_redirects=True)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return print_colored_flags("[ERROR]: ", e, Fore.RED)
    if isExtension(base_url, extension):
        downloadImage(base_url, pathDir)
        return
    html_content = response.content
    if not html_content or not recursion or depth >= maxDepth:
        return
    
    soup = BS(html_content, 'html.parser')
    urls = []
    log(base_url, recursion, depth, maxDepth)
    for tag, attrs in tags_attributes.items():
        for elem in soup.find_all(tag):
            for attr in attrs:
                val = elem.get(attr)
                if not val:
                    continue
                if attr == 'style':
                    srcs = re.findall(r'url\(["\']?(.*?\.(?:jpg|jpeg|png|gif|bmp))["\']?\)', val)
                    for src in srcs:
                        if isRelative(src) and not '#' in url and not src.endswith('='):
                            urls.append(urljoin(base_url, src))
                else:
                    if isRelative(val) and isExtension(val, extension):
                        urls.append(urljoin(base_url, val))
    try:
        regex_urls = re.findall(pattern, html_content.decode())
        for url in regex_urls:
            full_url = url[0] + '://' + url[1] + url[2]
            if not '#' in full_url and not full_url.endswith('='):
                urls.append(full_url)
    except UnicodeDecodeError:
        regex_urls = []
    urls = list(set(urls))
    for url in urls:
        if isExtension(url, extension):
            downloadImage(url, pathDir)
        else:
            scrapePage(url, pathDir, depth + 1, maxDepth, recursion)
    print_colored_flags("INFO ", "DONE", Fore.GREEN)
    print_colored_flags("INFO ", "DONE", Fore.GREEN)
    print_colored_flags("INFO ", "DONE", Fore.GREEN)

def downloadImage(imageUrl: str, pathDir: str):
    """Creates directories based on the URL path and saves the image to the final directory"""
    parsed_url = urlparse(imageUrl)
    path = pathDir + os.path.dirname(parsed_url.path)
    filePath = os.path.join(path, os.path.basename(imageUrl))

    os.makedirs(path, exist_ok=True)
    if os.path.exists(filePath):
        print_colored_flags("[WARNING]: ", f"Image {imageUrl} already saved", Fore.YELLOW)

    HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(imageUrl, headers=HEADERS, stream=True)
    except requests.exceptions.RequestException as e:
        return
    file = open(filePath, "wb")
    for chunk in response.iter_content(1024):
        file.write(chunk)
    file.close()
    print_colored_flags("[SUCCESS]: ", f"{imageUrl} saved", Fore.GREEN)

def isExtension(src: str, extensions: list)-> bool:
    """Check if the URL ends with one of the specified extensions"""
    return any(src.lower().endswith(ext) for ext in extensions) and not '#' in src

def isRelative(url: str) -> bool:
    """Check if a URL is relative"""
    if not re.match(r'^(?:https?|ftp|..|./|/):', url):
        return True
    return False

def print_colored_flags(flag, message, color):
    print(f"{color}{flag}{Style.RESET_ALL}{message}")

if __name__ == "__main__":
    spider()
