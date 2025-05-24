#!/usr/bin/env python3
import os
import re
import requests
import argparse
from colorama import Fore, Style
from urllib import parse
from bs4 import BeautifulSoup as BS

tags_attributes = {
    'img': ['src', 'srcset'],
    'image': ['href'],
    'source': ['src', 'srcset'],
    'a': ['href'],
    'link': ['href'],
    'div': ['style'],
    'video': ['poster', 'srs'],
	'audio': ['src'],
    'embed': ['src'],
    'object': ['data'],
    'background': ['url'],
    'background-image': ['url'],
    'svg': ['href'],
    'span': ['style'],
    'p': ['style'],
    'html': ['style']
}

pattern = r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])(?!(?:\.xml)(?=\s|$))'

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
        assert args.url, f"Invalid URL {args.url}"
        assert args.path, f"Invalid path {args.path}"
        print_colored_flags("[INFO]    ", "Initial data", Fore.BLUE)
        log(args.url, args.recursive, 0, args.level)
        print_colored_flags("[INFO]    ", f"Path: {os.path.abspath(args.path)}\n", Fore.BLUE)
        visited_urls = set()
        scrapePage(args.url, args.path, 0, args.level, args.recursive, visited_urls)

    except AssertionError as e:
        print_colored_flags("[ERROR]   ", e, Fore.RED)
        return 1
    except ValueError as e:
        print_colored_flags("[ERROR]   ", e, Fore.RED)
        return 2
    except TypeError as e:
        print_colored_flags("[ERROR]   ", e, Fore.RED)
        return 3
    except IsADirectoryError as e:
        print_colored_flags("[ERROR]   ", e, Fore.RED)
        return 4
    except Exception as e:
        print_colored_flags("[ERROR]   ", e, Fore.RED)
        return 5
    except KeyboardInterrupt:
        print()
        return 6

def log(base_url: str, recursive: bool, depth: int, maxDepth: int):
    print_colored_flags("[INFO]    ", f"Processing: {base_url}", Fore.BLUE)
    print_colored_flags("[INFO]    ", f"Recursive: {recursive}", Fore.BLUE)
    print_colored_flags("[INFO]    ", f"Depth level: {depth}/{maxDepth}", Fore.BLUE)

def scrapePage(base_url: str, pathDir: str, depth: int, maxDepth: int, recursion: bool, visited_urls: list, extension=[".jpg", ".jpeg", ".png", ".gif", ".bmp"]):
    if base_url in visited_urls:
        return
    log(base_url, recursion, depth, maxDepth)
    if depth >= maxDepth:
        print_colored_flags("[WARNING] ", "Maximum recursion depth is reached and no image is found", Fore.YELLOW)
        return

    visited_urls.add(base_url)

    if isExtension(base_url, extension):
        downloadImage(base_url, pathDir)
        print(base_url, "\n")
        return
    
    response = getResponse(base_url)
    if not response:
        return

    content = response.content
    if not content or not recursion:
        print_colored_flags("[WARNING] ", "Recursion, depth level are not given or no image is found", Fore.YELLOW)
        return

    if '<?xml' in content.decode(errors='ignore'):
        soup = BS(content, "lxml-xml")
    else:
        soup = BS(content, 'html.parser')
    urls = []
    for tag, attrs in tags_attributes.items():
        for elem in soup.find_all(tag):
            for attr in attrs:
                val = elem.get(attr)
                if not val:
                    continue
                if attr == 'style':
                    srcs = re.findall(r'url\(["\']?(.*?\.(?:jpg|jpeg|png|gif|bmp))["\']?\)', val)
                    for src in srcs:
                        if isRelative(src) and not '#' in src and not src.endswith('='):
                            urls.append(parse.urljoin(base_url, src))
                        else:
                            urls.append(src)
                else:
                    if isRelative(val):
                        urls.append(parse.urljoin(base_url, val))
                    else:
                        urls.append(val)
    try:
        regex_urls = re.findall(pattern, content.decode())
        for url in regex_urls:
            full_url = url[0] + '://' + url[1] + url[2]
            if not '#' in full_url and not full_url.endswith('='):
                urls.append(full_url)
    except UnicodeDecodeError:
        pass
    urls = list(set(urls))
    for url in urls:
        if isExtension(url, extension):
            log(url, recursion, depth + 1, maxDepth)
            downloadImage(url, pathDir)
        else:
            scrapePage(url, pathDir, depth + 1, maxDepth, recursion, visited_urls)

def downloadImage(imageUrl: str, pathDir: str):
    """Creates directories based on the URL path and saves the image to the final directory"""
    parsed_url = parse.urlparse(imageUrl)
    path = pathDir + os.path.dirname(parsed_url.path)
    filePath = os.path.join(path, os.path.basename(imageUrl))

    os.makedirs(path, exist_ok=True)
    if os.path.exists(filePath):
        print_colored_flags("[WARNING] ", f"Image {imageUrl} already saved", Fore.YELLOW)
        return

    response = getResponse(imageUrl)
    if not response:
        return
    file = open(filePath, "wb")
    for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk)
    file.close()
    print_colored_flags("[SUCCESS] ", f"{imageUrl} saved", Fore.GREEN)
    

def getResponse(url: str):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.ConnectTimeout as e:
        print_colored_flags("[ERROR]   ", "{e}", Fore.RED)
        return []
    except requests.exceptions.RequestException as e:
        print_colored_flags("[ERROR]   ", e, Fore.RED)
        return []

def isValidUrl(url):
    parsed = parse.urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def isExtension(src: str, extensions: list)-> bool:
    """Check if the URL ends with one of the specified extensions"""
    return any(src.lower().endswith(ext) for ext in extensions) and not '#' in src

def isRelative(url: str) -> bool:
    """Check if a URL is relative"""
    if not re.match(r'^(?:https?|ftp):', url):
        return True
    return False

def print_colored_flags(flag, message, color):
    print(f"{color}{flag}{Style.RESET_ALL}{message}")

if __name__ == "__main__":
    spider()
