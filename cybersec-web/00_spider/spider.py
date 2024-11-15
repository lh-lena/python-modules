import os
import urllib.request as URLR
from bs4 import BeautifulSoup as BS
import shutil
# from PIL import Image

class Spider:
    def __init__(self, args: list):
        # set default value
        self.recursive = False
        self.depth = 5
        self.path = "./data/"
        self.url = None

        # parse options
        self.parseOptions(args)
        self.validateOptions()
        self.downloadImages(self.url, self.path)

    def __repr__(self):
        return (f"Spider(recursive={self.recursive}, depth={self.depth}, "
                f"path='{self.path}', url='{self.url}')")

def parseOptions(self, args: list):
    i = 0;
    size = len(args);
    while (i < size):
        if args[i] == "-r":
            self.recursive = True
        elif args[i] == "-l":
            if i + 1 < size and args[i + 1].isdigit():
                self.depth = int(args[i + 1])
                i += 1
            else:
                raise AssertionError("Option -l requires a numeric depth level")
        elif args[i] == "-p":
            assert i + 1 < size, "Option -p requires a path"
            self.path = args[i + 1]
            i += 1
        elif args[i].startswith("https://") or args[i].startswith("http://"): #ftp??
            self.url = args[i]
        else:
            raise AssertionError("Invalid option")
        i += 1
        
def validateOptions(self):
    curPath = os.getcwd()
    # p = self.path
    if None == self.url:
        raise AssertionError("URL must be provided")
    # if p.startswith("./"):
    self.path = curPath + "/data"
    
def spider(self, url: str):
    if not url:
        raise AssertionError("URL must be provided")
    



def downloadImage(imageUrl, dir):
    directory = os.path.dirname(dir)
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = os.path.basename(imageUrl)
    URLR.urlretrieve(imageUrl, filename)

    print(f"Image downloaded and saved at {dir}")

def downloadImages(url, dir, extension=[".jpg", ".jpeg", ".png", ".gif", ".bmp"]):
    req = URLR.Request(url)
    with URLR.urlopen(req) as response:
        page = response.read()
    # print(page)
    # Parse the HTML content
    soup = BS(page, 'html.parser')
    print(soup.title.string)
    # imageUrl = "https://images.unsplash.com/photo-1561037404-61cd46aa615b?h=500"
    # downloadImage(imageUrl, dir)


Spider.parseOptions = parseOptions
Spider.validateOptions = validateOptions
Spider.downloadImages = downloadImages