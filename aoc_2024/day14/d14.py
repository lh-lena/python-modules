#! /usr/bin/env python3
#part2: 43 38 39 48 49 69 98 97 99 
def d14():
    res = 0
    data = []

    # with open("input.txt", "r") as f:
    with open("input_day14.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            if (line):
                parts = line.split(' ')
                p_coords = parts[0].split('=')[1].split(',')
                v_coords = parts[1].split('=')[1].split(',')

                px, py = (p_coords[0]), (p_coords[1])
                vx, vy = (v_coords[0]), (v_coords[1])

                data.append((int(px), int(py), int(vx), int(vy)))
    # print(data)
    
    # rows = 7
    # cols = 11
    rows = 103
    cols = 101
    sec = 0
    while sec < 100:
        
        for i in range(len(data)):
            px, py, vx, vy = data[i]
            px += vx
            py += vy
            if px >= cols:
                px = (px - cols)
            elif px < 0:
                px = (cols + px)
            if py >= rows:
                py = py - rows
            elif py < 0:
                py = rows + py
            data[i] = (px, py, vx, vy)
        sec += 1
        ft_print(sec, data, rows, cols)



    # print(data)
    
    mid_x = cols // 2
    mid_y = rows//2
    print(mid_x, mid_y)
    l_top = 0
    r_top = 0
    l_btm = 0
    r_btm = 0
    for i in range(len(data)):
            px, py, vx, vy = data[i]
            if (px < mid_x and py < mid_y):
                l_top += 1
            elif (px > mid_x and py < mid_y):
                r_top += 1
            elif (px < mid_x and py > mid_y):
                l_btm += 1
            elif (px > mid_x and py > mid_y):
                r_btm += 1
    print(l_top, r_top, l_btm, r_btm)
    print(l_top * r_top * l_btm * r_btm)
    
    
def ft_print(sec, data, rows, cols):
    
    tmp = set()
    for i in range(len(data)):
            px, py, vx, vy = data[i]
            tmp.add((px, py))

    def print_board(board):
        for row in board:
            print(''.join(row))

    def create_board(rows, cols):
        return [['.' for _ in range(cols)] for _ in range(rows)]

    board = create_board(rows, cols)
    for x, y in tmp:
        board[y][x] = 'l'
    print_board(board)
    print(sec)  
if __name__ == "__main__":
    d14()
