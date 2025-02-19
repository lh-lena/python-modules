#p1 5409 How many distinct positions will the guard visit before leaving the mapped area?
#p2  How many different positions could you choose for this obstruction? # 542, 543 too low | 747, 810, 811
def d06():
    res = 0
    res2 = 0
    data = ""
    cols = 0
    rows = 0
    with open("input.txt", "r") as f:
    # with open("input_41.txt", "r") as f:
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
    # res2 = obstructionNbr(data, pos_x, pos_y, cols, rows)
    print(res - 1)

    """
    3 6
    6 7
    7 7
    1 8
    3 8
    7 9
    """

def getPath(data, pos_x, pos_y, cols, rows):
    steps = 0
    res2 = 0
    visited = set()
    obstructions = set()
    dir = -1
    while ( pos_x > 0 and pos_x < cols - 1 and pos_y > 0 and pos_y < rows - 1):
        while (data[(pos_x) + cols * pos_y] != '#' and ((pos_y  + (1 * dir) < rows) and (pos_y  + (1*dir) > 0))):
            print(pos_x, pos_y)
            pos_y += (1 * dir)
            steps += 1
            visited.add((pos_x, pos_y))

            #(pos_x + 1, pos_y+ (1 * dir)) in visited) or
            if ((pos_x + (1 * dir), pos_y + (1 * dir)) in visited):
                print("y ", (pos_x - (1 * dir), pos_y + (1 * dir)))
                print("y ",(pos_x + (1 * dir), pos_y + (1 * dir)))
                res2 += 1
                obstructions.add((pos_x + (1 * dir), pos_y + (1 * dir)))
            if ((pos_y  + (1 * dir) < rows) and data[(pos_x) + cols * (pos_y + (1 * dir))] == '#' ):
                dir *= -1
                
                break
            
        while (data[((pos_x) + cols * pos_y)] != '#' and ((pos_x  + (1*dir) > 0) and (pos_x  + (1 * dir) < cols))):
            print(pos_x, pos_y)
            pos_x += (1 * dir)
            
            steps += 1
            #(pos_x + (1 * dir) , pos_y + 1) in visited) or 
            if ((pos_x + (1 * dir), pos_y + (1 * dir)) in visited):
                print((pos_x + (1 * dir), pos_y - (1 * dir)))
                print((pos_x + (1 * dir), pos_y + (1 * dir)))
                res2 += 1
                obstructions.add((pos_x + (1 * dir), pos_y + (1 * dir)))
            if ((pos_x + (1*dir)) + cols * pos_y) >= cols * rows:
                break
            visited.add((pos_x, pos_y))
            if (data[((pos_x + (1*dir)) + cols * pos_y)] == '#'):
                pos = (pos_x - 1) - pos_x
                if pos > 0:
                    dir = -1
                break
    print("res : ", steps)
    print("res2 : ", res2)
    print("obstructions : ", len(obstructions))
    steps = len(visited)
    return steps

# def obstructionNbr(data, pos_x, pos_y, cols, rows):
#     """_summary_
#         returns max amount where to place the new obstruction in such a way that the guard will get stuck in a loop.
#     """
    
    

if __name__ == "__main__":
    d06()

    """
    def d06():
    with open("input_41.txt", "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    rows, cols = len(grid), len(grid[0])
    start_x, start_y = -1, -1

    # Find the start position '^'
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == '^':
                start_x, start_y = x, y
                break
        if start_x != -1:
            break

    if start_x == -1 or start_y == -1:
        print("No starting position found!")
        return

    result = get_path(grid, start_x, start_y)
    print("Result:", result)


def get_path(grid, start_x, start_y):
    rows, cols = len(grid), len(grid[0])
    visited = set()  # Track visited cells
    direction = (-1, 0)  # Initial direction (up)
    x, y = start_x, start_y
    visited.add((x, y))
    steps = 1  # Start position is counted as a used cell

    while True:
        # Move in the current direction
        next_x, next_y = x + direction[0], y + direction[1]

        # Check if we hit the border or a visited cell
        if not (0 <= next_x < cols and 0 <= next_y < rows) or (next_x, next_y) in visited:
            break

        # If we hit a '#', turn right
        if grid[next_y][next_x] == '#':
            direction = turn_right(direction)
        else:
            # Otherwise, move to the next cell
            x, y = next_x, next_y
            if (x, y) not in visited:
                steps += 1
                visited.add((x, y))

    return steps


def turn_right(direction):
    # Turn right based on the current direction
    if direction == (-1, 0):  # Up
        return (0, 1)  # Right
    elif direction == (0, 1):  # Right
        return (1, 0)  # Down
    elif direction == (1, 0):  # Down
        return (0, -1)  # Left
    elif direction == (0, -1):  # Left
        return (-1, 0)  # Up

    """