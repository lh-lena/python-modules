import re
# too low: 246
# 274 439 430 225
# too high: 446 431
# Part1: 361
# Part2: 1249

def d08():
    res = 0
    # with open("input_14.txt", "r") as f:
    with open("input_d08.txt", "r") as f:
        context = f.read()
    # line_len = context.index('\n')
    print(len(context))
    # grid = [context.split('\n')]
    # print( count_max_elements(grid))
    # return

    chars = set()
    for char in context:
        if (char != '.' and char != '\n'):
            chars.add(char)
    print(chars)
    res = set()
    lenn = 50
    # lenn = 12
    lrow = 50
    len_cont = len(context)
    for char in chars:
        seq = [(m.start()) for m in re.finditer((char), context)]
        for s in range(len(seq)):
            
            l = s
            while l < (len(seq) - 1):
                cur1 = seq[s]
                cur2 = seq[l+1]
                cur1_f = cur1 // lenn
                cur1_s = cur1 % lenn
                cur2_f = cur2 // lenn
                cur2_s = cur2 % lenn
                shift_f = abs(cur1_f - cur2_f)
                shift_s = abs(cur1_s - cur2_s)
                dir_backward = 1 if cur2_s >= cur1_s else -1
                dir_forward = 1 if cur2_s >= cur1_s else -1
                if (cur1_f >= 0 and cur1_f < lrow and \
                    cur2_f >= 0 and cur2_f < lrow and \
                    cur1_s >= 0 and (cur1_s * lrow) < (len_cont ) and \
                    cur2_s >= 0 and (cur2_s * lrow) < (len_cont)):
                    back_f = cur1_f
                    back_s = cur1_s
                    while (back_f >= 0 and back_s >= 0):
                        back_f = back_f - shift_f
                        back_s = back_s - (shift_s * dir_backward)
                        if (back_f >= 0 and back_s >= 0 and back_s < lrow):
                            res.add((back_f, back_s))
                        else:
                            break
                    
                    forw_f = cur2_f
                    forw_s = cur2_s
                    while (forw_f < (len_cont // lrow) and forw_s < (lrow)):
                        forw_f +=  shift_f
                        forw_s =  forw_s + (shift_s * dir_forward)
                        if (forw_f >= 0 and forw_s >= 0 and \
                            forw_f * lrow < (len_cont) and forw_s < (lrow)):
                            res.add((forw_f, forw_s))
                        else:
                            break
                    res.add((cur1_f, cur1_s))
                    res.add((cur2_f, cur2_s))
                l += 1
    print(res)
    print(len(res))
    
    """
    def d08():
    res = 0
    # with open("input_14.txt", "r") as f:
    with open("input_d08.txt", "r") as f:
        context = f.read()
    # line_len = context.index('\n')
    print(len(context))

    chars = set()
    for char in context:
        if (char != '.' and char != '\n'):
            chars.add(char)
    print(chars)
    res = set()
    lenn = 50
    for char in chars:
        seq = [(m.start()) for m in re.finditer((char), context)]
        for s in range(len(seq)):
            
            l = s
            while l < (len(seq) - 1):
                dif = 0
                dif = seq[l+1] - seq[s]
                r = (seq[s] - dif)
                if (r) > 0:
                    if ((abs((r // lenn) - (seq[s]//lenn)) == abs((seq[l+1] // lenn ) - (seq[s]//lenn))) and ((abs((r % lenn) - (seq[s]%lenn)) == abs((seq[l+1] % lenn) - (seq[s]%lenn))))):
                        res.add(r)
                r = (seq[l+1] + dif)
                if  (r) < len(context):
                    if ((abs((r // lenn) - (seq[l+1]//lenn)) == abs((seq[l+1] // lenn) - (seq[s]//lenn))) and (abs((r % lenn) - (seq[l+1]%lenn)) == abs((seq[l+1] % lenn) - (seq[s]%lenn)))):
                        res.add(r)
                l += 1
    print(res)
    print(len(res))
    """

def count_max_elements(grid):
    n = len(grid)
    unique_chars = set()
    
    # Collect unique characters in the grid
    for row in grid:
        unique_chars.update(row)
    
    max_elements = 0
    
    # Check horizontal lines
    for row in grid:
        for char in unique_chars:
            max_elements += row.count(char)
    
    # Check vertical lines
    for col in range(n):
        column_chars = ''.join(grid[row][col] for row in range(n))
        for char in unique_chars:
            max_elements += column_chars.count(char)
    
    # Check diagonal lines (top-left to bottom-right)
    for d in range(-n + 1, n):
        diag_chars = ''.join(grid[i][i + d] for i in range(n) if 0 <= i + d < n)
        for char in unique_chars:
            max_elements += diag_chars.count(char)
    
    # Check diagonal lines (top-right to bottom-left)
    for d in range(2 * n - 1):
        diag_chars = ''.join(grid[i][d - i] for i in range(n) if 0 <= d - i < n)
        for char in unique_chars:
            max_elements += diag_chars.count(char)
    
    return max_elements

if __name__ == "__main__":
    d08()