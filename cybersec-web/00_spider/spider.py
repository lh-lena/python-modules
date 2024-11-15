import os
from urllib import request as URLR
from urllib import parse as Parse
from bs4 import BeautifulSoup as BS
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
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    if not imageUrl.startswith('http'):
        imageUrl = Parse.urljoin(pageUrl, imageUrl)
    req = URLR.Request(imageUrl, headers=HEADERS)
    response = URLR.urlopen(req)
    if not os.path.exists(pathDir):
        os.makedirs(pathDir, exist_ok=True)
    absp = os.path.abspath(pathDir)
    filePath = absp + "/" + os.path.basename(imageUrl)
    file = open(filePath, "wb")
    file.write(response.read())
    file.close()

    # print(f"Image {imageUrl} downloaded and saved at {absp}")

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

    req = URLR.Request(url, headers=HEADERS)
    response = URLR.urlopen(req).read()
    soup = BS(response, 'html.parser')

    imgUrls = parseUrls(soup, "img", "src")
    for tag in imgUrls:
        if isExtention(tag, extension):
            downloadImage(url, tag, pathDir)
    
    pictureUrls = parseUrls(soup, "pictures", "srcset")
    for pic in pictureUrls:
        if isExtention(pic, extension):
            downloadImage(url, pic, pathDir)

    if depth >= maxDepth:
        return

    pageUrls = parseUrls(soup, "a", "href")
    for page in pageUrls:
        if not page.startswith("#") and not page == "index.html":
            if not page.startswith("http"):
                page = Parse.urljoin(url, page)
            try:
                print(f"Found link: {page} at depth {depth + 1}")
                scrapePage(page, pathDir, depth + 1, maxDepth)
            except URLR.HTTPError as e:
                print(f"Error scraping {page}: {e}")
