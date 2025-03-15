# Allowed functions : all libs for load images and table manipulation


# Importing Image from PIL package 
from PIL import Image
import numpy as np

def ft_load(path: str) -> list:
    """
    loads an image, prints its format, and its pixels
content in RGB format.
    """
    # creating a image object
    im = Image.open(path)

    # im.show()

    a = np.asarray(im)
    print(f"The shape of image is: {a.shape}")
    return a

def main():
    print(ft_load("landscape.jpg"))
    print(ft_load("animal.jpeg"))

if __name__ == "__main__":
    main()

"""
Expected output:
$> python tester.py
The shape of image is: (257, 450, 3)
[[[19 42 83]
[23 42 84]
[28 43 84]
...
[ 0 0 0]
[ 1 1 1]
[ 1 1 1]]]
$>
"""