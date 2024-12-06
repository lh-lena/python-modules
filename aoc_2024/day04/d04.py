
import numpy as np
#Take a look at the little Elf's word search. How many times does XMAS appear? 
# Part1: 2336
# Part2: 1831

def d04():

    res = 0
    res2 = 0
    with open("input_d04.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    res += search_matrix(data, "XMAS")
    res += search_matrix(data, "SAMX")
    res2 += search_x_maxrix_part2(data, "MAS")
    print(res)
    print(res2)

def search_x_maxrix_part2(matrix, pattern):
    res = 0
    rows, cols = len(matrix), len(matrix[0])
    plen = len(pattern)
    rev_pat = pattern[::-1]

    for i in range(rows - plen + 1):
        for j in range(cols):
            if j + plen <= cols:
                if (all(matrix[i+k][j+k] == pattern[k] for k in range(plen)) or \
                    all(matrix[i+k][j+k] == rev_pat[k] for k in range(plen))) and \
                    ((j + 2 - (plen - 1) >= 0 and j+2 < cols) and \
                    (all(matrix[i+k][j+2-k] == pattern[k] for k in range(plen)) or \
                    all(matrix[i+k][j+2-k] == rev_pat[k] for k in range(plen)))):
                    res += 1

    return res

def search_matrix(matrix, pattern):
    res = 0
    rows, cols = len(matrix), len(matrix[0])
    plen = len(pattern)

    # horizontal
    for i in range(rows):
        for j in range(cols - plen + 1):
            if matrix[i][j:j+plen] == pattern:
                res += 1

    # vertical
    for j in range(cols):
        for i in range(rows - plen + 1):
            if ''.join(matrix[i+k][j] for k in range(plen)) == pattern:
                res += 1

    #top-left to bottom-right
    for i in range(rows - plen + 1):
        for j in range(cols - plen + 1):
            if ''.join(matrix[i+k][j+k] for k in range(plen)) == pattern:
                res += 1

    # top-right to bottom-left
    for i in range(rows - plen + 1):
        for j in range(plen - 1, cols):
            if ''.join(matrix[i+k][j-k] for k in range(plen)) == pattern:
                res += 1

    return res

if __name__ == "__main__":
    d04()


# https://cs.stackexchange.com/questions/153510/algorithm-that-finds-4-os-or-4-xs-on-a-diagonal-horizontal-or-vertical

"""
to find all 
M.S
.A.
M.S

Here's the same example from before, but this time all of the X-MASes have been kept instead:
# 9
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

print(matrix[i][j], i, j, matrix[i][j+2], i, j+2)
M 0 1 S 0 3
M 1 5 M 1 7
S 1 6 S 1 8
M 2 1 S 2 3
S 2 3 M 2 5
M 5 4 X 5 6 // invalid
S 6 0 S 6 2
S 6 2 S 6 4
S 6 4 S 6 6
S 6 6 S 6 8

"""