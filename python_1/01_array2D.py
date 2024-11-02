import numpy as np

"""
Write a function that takes as parameters a 2D array, prints its shape, and returns a
truncated version of the array based on the provided start and end arguments.
You must use the slicing method.
You have to handle error cases if the lists are not the same size, are not a list
"""

def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        print("Error: Not a list")
        return []
    arr = np.array(family)
    if not np.issubdtype(arr.dtype, np.number):
        print("Error: Not a number")
        return []
    lenth = len(family)
    print(f"My shape is : {arr.shape}")
    res = family[start:end]
    new_arr = np.array(res)
    l = len(res)
    print(f"My new shape is : {new_arr.shape}")
    return(res)

def main():
    family = [[1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

if __name__ == "__main__":
    main()

"""
Expected output:
$> python test_array2D.py
My shape is : (4, 2)
My new shape is : (2, 2)
[[1.8, 78.4], [2.15, 102.7]]
My shape is : (4, 2)
My new shape is : (1, 2)
[[2.15, 102.7]]
$>
"""