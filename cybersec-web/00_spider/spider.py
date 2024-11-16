import os
from urllib import request as URLR
from urllib import parse as Parse
from bs4 import BeautifulSoup as BS
from lxml import html
import requests
# from PIL import Image

def parseOptions(args: list) -> dict:
    data = {
        "recursive": False,
        "depth": 5,
        "path": "./data/",
        "url": None
    }
    i = 0
    size = len(args)
    while (i < size):
        if args[i] == "-r":
            data["recursive"] = True
        elif args[i] == "-l":
            if i + 1 < size and args[i + 1].isdigit():
                data["depth"] = int(args[i + 1])
                i += 1
            else:
                raise AssertionError("Option -l requires a numeric depth level")
        elif args[i] == "-p":
            assert i + 1 < size, "Option -p requires a path"
            data["path"] = args[i + 1]
            i += 1
        elif args[i].startswith("https://") or args[i].startswith("http://"):
            data["url"] = args[i]
        else:
            raise AssertionError("Invalid option")
        i += 1
    if None == data["url"]:
        raise AssertionError("URL must be provided")
    return data

def downloadImage(pageUrl: str, imageUrl: str, pathDir: str):

    if not imageUrl.startswith('http'):
        imageUrl = Parse.urljoin(pageUrl, imageUrl)

    if not os.path.exists(pathDir):
        os.makedirs(pathDir, exist_ok=True)

    absp = os.path.abspath(pathDir)
    filePath = absp + "/" + os.path.basename(imageUrl)

    response = requests.get(imageUrl, stream=True)
    if response.status_code == 200:
        file = open(filePath, "wb")
        for chunk in response.iter_content(1024):
            file.write(chunk)
        file.close()

def isExtention(src: str, extention: list)-> bool:
    """Check if the URL ends with one of the specified extensions"""
    for ext in extention:
        if src.lower().endswith(ext):
            return True
    return False

def parseUrls(soup, tag: str, source: str) -> list:
    res = []
    for i in soup.find_all(tag, {source:True}):
        res.append(i[source])
    return res

def scrapePage(url: str, pathDir: str, depth: int, maxDepth: int, extension=[".jpg", ".jpeg", ".png", ".gif", ".bmp"]):
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return
    
    tree = html.fromstring(response.content)
    srcs = tree.xpath('//img/@src')
    # srcs = tree.xpath('//picture/@srcset')
    i = 0
    for src in srcs:
        if isExtention(src, extension):
            downloadImage(url, src, pathDir)
            i += 1
            print(f"Downloading {i}", end='\r')
    print()

    if depth >= maxDepth:
        return

    pageUrls = tree.xpath('//a/@href')
    for page in pageUrls:
        if not page.startswith("#") and page != "index.html":
            if not page.startswith("http"):
                page = Parse.urljoin(url, page)
            try:
                print(f"Found link: {page} at depth {depth + 1}")
                scrapePage(page, pathDir, depth + 1, maxDepth)
            except URLR.HTTPError as e:
                print(f"Error scraping {page}: {e}")
