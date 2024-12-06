
def d06():
    res = 0
    res2 = 0
    data = ""
    cols = 0
    rows = 0
    with open("input_41.txt", "r") as f:
        for line in f.readlines():
            cols = len(line)
            rows += 1
            data += line.strip()
    guard = "^"
    print(data.count("X"))
    print(data.index(guard))
    pos_x = data.index(guard) % cols
    pos_y = data.index(guard) // cols
    res = getPath(data, pos_x, pos_y, cols, rows)
        
    print(res)

def getPath(data, pos_x, pos_y, cols, rows):
    res = 0
    x = {}
    dir = -1
    while (((pos_x  + (1*dir)) > 0 and (pos_x  + (1 * dir)) < rows) and ((pos_y  + (1 * dir)) < cols and  (pos_y  + (1*dir)) > 0)):

        while (data[(pos_x) + cols * pos_y] != '#'):
            print(pos_x, pos_y)
            pos_y += (1 * dir)
            res += 1
            if (data[(pos_x) + cols * (pos_y + (1 * dir))] == '#'):
                print(pos_x, pos_y, (pos_x + (1*dir)) + cols * pos_y)
                dir *= -1
                break

        while (data[((pos_x) + cols * pos_y)] != '#'):
            print(pos_x, pos_y)
            pos_x += (1 * dir)
            res += 1
            if (data[((pos_x + (1*dir)) + cols * pos_y)] == '#'):
                print(pos_x, pos_y, (pos_x + (1*dir)) + cols * pos_y)
                break

    print("res:  ", res)
    return res


if __name__ == "__main__":
    d06()
