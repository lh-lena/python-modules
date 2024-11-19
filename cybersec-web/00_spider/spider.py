import os
import sys
from urllib.parse import urljoin
import requests

def spider():
    try:
        arg = len(sys.argv)
        assert arg > 1, f"{sys.argv[0]}: missing URL\nUsage: [-rlp]... [URL]...\n\n-r:  recursively downloads the images in a URL\n-l [N]: indicates the maximum depth level of the recursive download\n-p [PATH]: indicates the path where the downloaded files will be saved"
        data = parseOptions(sys.argv[1:])
        if data["recursive"]:
            scrapePage(data["url"], data["path"], 1, data["depth"])
        else:
            scrapePage(data["url"], data["path"], 1, 1)

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
            if not i + 1 < size or not args[i + 1].isdigit():
                raise Exception("Option -l requires a positive numeric depth level")
            data["depth"] = int(args[i + 1])
            i += 1
        elif args[i] == "-p":
            assert i + 1 < size, "Option -p requires a path"
            data["path"] = args[i + 1]
            i += 1
        elif args[i].startswith("http"):
            data["url"] = args[i]
        else:
            raise Exception("Invalid option")
        i += 1
    if not data["url"]:
        assert Exception("URL must be provided")
    return data

def scrapePage(url: str, pathDir: str, depth: int, maxDepth: int, extension=[".jpg", ".jpeg", ".png", ".gif", ".bmp"]):
    HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Connection": "keep-alive"
    }

    try:
        response = requests.get(url, headers=HEADERS, allow_redirects=True)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return
    srcs = extractData(response.text, '<img ', 'src="', '"')
    srcs_pct = extractData(response.text, '<source ', 'srcset="', '"')
    srcs.extend(srcs_pct)
    srcs_img_css = extractData(response.text, 'background','url(', ')')
    srcs.extend(srcs_img_css)
    print(f"{len(srcs)} -> pct: {len(srcs_pct)}, img_css: {len(srcs_img_css)}")
    if not srcs:
        return print(f"No images found")
    for src in srcs:
        if src and isExtension(src, extension):
            downloadImage(url, src, pathDir)

    if depth >= maxDepth:
        print(f"\tdepth : {depth}")
        return

    pageUrls = extractData(response.text, '<a ', 'href="', '"')
    print(f"len pageUrls-> {len(pageUrls)}")
    for page in pageUrls:
        if "#" not in page and page != "index.html":
            if not page.startswith("http"):
                page = urljoin(url, page)
            print(f"Found link: {page} at depth {depth + 1}")
            scrapePage(page, pathDir, depth + 1, maxDepth)


def downloadImage(pageUrl: str, imageUrl: str, pathDir: str):

    if not imageUrl.startswith('http'):
        imageUrl = urljoin(pageUrl, imageUrl)

    if not os.path.exists(pathDir):
        os.makedirs(pathDir, exist_ok=True)
    absp = os.path.abspath(pathDir)
    filePath = absp + "/" + os.path.basename(imageUrl)

    HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Connection": "keep-alive"
    }
    try:
        response = requests.get(imageUrl, headers=HEADERS, stream=True)
    except requests.exceptions.RequestException:
        return
    file = open(filePath, "wb")
    for chunk in response.iter_content(1024):
        file.write(chunk)
    file.close()
    print(f"Downloading {imageUrl}")

def isExtension(src: str, extension: list)-> bool:
    """Check if the URL ends with one of the specified extensions"""
    for ext in extension:
        if src.lower().endswith(ext):
            return True
    return False

def extractData(data, tag, attr_start, attr_end) -> list:
    """Search for all tags specified as a parameter tag """
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

def url_join(base_url: str, relt_path: str):
    scheme_dom = base_url.partition("://")
    dom_path = scheme_dom[2].partition("/")
    base_path = dom_path[2]
    if not base_path.endswith("/"):
        base_path += "/"
    base_parts = base_path.split("/")[:-1]
    relt_parts = relt_path.split("/")
    for p in relt_parts:
        if p == "..":
            if base_parts:
                base_parts.pop()
        elif p == "." or p == "":
            continue
        else:
            base_parts.append(p)
    res = "/".join(base_parts)
    return (f"{scheme_dom[0]}{scheme_dom[1]}{dom_path[0]}/{res}")


if __name__ == "__main__":
    spider()
