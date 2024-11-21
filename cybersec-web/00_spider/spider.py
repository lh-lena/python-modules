#!/usr/bin/env python3
import os
import sys
import re
import requests
import argparse
import urllib.parse as Parse
from bs4 import BeautifulSoup as BS

tags_attributes = {
    'img': ['src', 'srcset'],
    'source': ['src', 'srcset'],
    'a': ['href'],
    'link': ['href'],
    'meta': ['content'],
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

pattern = rf'\b(?:https?|ftp)://[^\s]+(?:.jpg|.jpeg|.png|.gif|.bmp)\b'

def spider():
    try:
        arg = len(sys.argv)
        parser = argparse.ArgumentParser(
                    prog='spider',
                    description='Image scraping')
        
        parser.add_argument('url', help='URL to a website')
        parser.add_argument('-r', '--recursive', action='store_true', help='Recursively download images')
        parser.add_argument('-l', '--level', type=unsg_int, default=5, help='Maximum recursion depth')
        parser.add_argument('-p', '--path', default='./data', help='Download path')

        args = parser.parse_args()
        print(f"Url       : {args.url}")
        print(f"Recursive : {args.recursive}")
        print(f"Level     : {args.level}")
        print(f"Path      : {args.path}")
        if args.recursive:
            scrapePage(args.url, args.path, 1, args.depth)
        else:
            downloadImage(args.url, args.path)

    except AssertionError as e:
        print(f"Error: {e}")
        return 1
    except ValueError as e:
        print(f"Error: {e}")
        return 2
    except TypeError as e:
        print(f"Error: {e}")
        return 3
    except IsADirectoryError as e:
        print(f"Error: {e}")
        return 4
    except Exception as e:
        print(f"Error: {e}")
        return 5
    except KeyboardInterrupt:
        print()
        return 6

def unsg_int(val: int):
    if val <= 0:
        raise argparse.ArgumentTypeError(f"{val} must be a positive integer")
    return val

def scrapePage(base_url: str, pathDir: str, depth: int, maxDepth: int, extension=[".jpg", ".jpeg", ".png", ".gif", ".bmp"]):
    HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(base_url, headers=HEADERS, allow_redirects=True)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return
    html_content = response.content
    if isExtension(base_url, extension):
        downloadImage(base_url, pathDir)
    if not depth >= maxDepth or maxDepth <= 0:
        return
    soup = BS(html_content, 'html.parser')
    urls = []
    srcs = []
    for tag, attrs in tags_attributes.items():
            for elem in soup.find_all(tag):
                for attr in attrs:
                    val = elem.get(attr)
                    if not val:
                        continue
                    if attr == 'style':
                        srcs = re.findall(r'url\((.*?)\)', val)
                    else:
                        if isRelative(val) and isExtension(val, extension):
                            urls.append(Parse.urljoin(base_url, val))
                    for src in srcs:
                        src = src.strip(' "\'')
                        if isRelative(src) and isExtension(src):
                            urls.append(Parse.urljoin(base_url, src))
    try:
        regex_urls = re.findall(pattern, html_content.decode())
    except UnicodeDecodeError:
        regex_urls = []
    print(len(urls))
    urls.extend(regex_urls)
    print(len(regex_urls))
    print(len(urls))
    for url in regex_urls:
        downloadImage(url, pathDir)

    if depth >= maxDepth:
        print(f"\tdepth : {depth}")
        return

    # pageUrls = extractData(response.text, '<a ', 'href="', '"')
    # print(f"len pageUrls-> {len(pageUrls)}")
    # for page in pageUrls:
    #     if "#" not in page and page != "index.html":
    #         if not page.startswith("http"):
    #             page = urljoin(url, page)
    #         print(f"Found link: {page} at depth {depth + 1}")
    #         scrapePage(page, pathDir, depth + 1, maxDepth)


def downloadImage(imageUrl: str, pathDir: str):
    """Creates directories based on the URL path and saves the image to the final directory"""
    parsed_url = Parse.urlparse(imageUrl)
    path = pathDir + os.path.dirname(parsed_url.path)
    filePath = path + "/" + os.path.basename(imageUrl)
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    else:
        return print(f"Warning  : Image {imageUrl} already saved")

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
    print(f"Downloading {imageUrl}")

def isExtension(src: str, extensions: list)-> bool:
    """Check if the URL ends with one of the specified extensions"""
    return any(src.lower().endswith(ext) for ext in extensions)

def isRelative(url: str) -> bool:
    """Check if a URL is relative"""
    if not re.match(r'^(?:https?|ftp):', url) and not '#' in url:
        return True
    return False

def extractData(data, tag, attr_start, attr_end) -> list:
    """Search for all tags specified as a parameter tag"""
    links = []
    pos = 0
    while True:
        el = data.find(tag, pos)
        if -1 == el:
            break
        link_start = data.find(attr_start, el)
        if -1 == link_start:
            break
        link_start += len(attr_start)
        link_end = data.find(attr_end, link_start)
        elem = data[link_start:link_end]
        if elem:
            elem = elem.strip()
            links.append(elem)
        pos = link_end
    return links

if __name__ == "__main__":
    spider()
