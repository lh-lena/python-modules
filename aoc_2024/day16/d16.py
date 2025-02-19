#! /usr/bin/env python3

def d16():

    with open("input.txt", "r") as f:
    # with open("input_day16.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    # for i in range(len(data)):
    #     if data[i].find("S") != -1:
    #         x = data[i].find("S")
    #         y = i
    #     elif data[i].find("E") != -1:
    #         end_x = data[i].find("E")
    #         end_y = i
    
    print(min_turns_path(data))

from collections import deque

def min_turns_path(grid):
    n, m = len(grid), len(grid[0])
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    reverse_directions = {v: k for k, v in directions.items()}

    # Find start and end positions
    start, end = None, None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                start = (i, j)
            if grid[i][j] == 'E':
                end = (i, j)

    # BFS with state: (x, y, direction, turns)
    queue = deque()
    for d in directions:  # Start with all possible initial directions
        dx, dy = directions[d]
        nx, ny = start[0] + dx, start[1] + dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.':
            queue.append((nx, ny, d, 0))  # No turns initially

    visited = set()

    while queue:
        x, y, direction, turns = queue.popleft()
        if (x, y) == end:
            return turns  # Found the end with the least turns

        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        # Continue moving in the current direction
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] in {'.', 'E'}:
            queue.append((nx, ny, direction, turns))

        # Try turning to all other directions
        for new_dir, (ndx, ndy) in directions.items():
            if new_dir == direction:  # Skip the current direction
                continue
            nx, ny = x + ndx, y + ndy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] in {'.', 'E'}:
                queue.append((nx, ny, new_dir, turns + 1))

    return -1  # No path found


def algo(data, path, x, y):
    new_p = []
    rows = len(data)
    cols = len(data[0])
    dir = 1
    
    for p in path:
        while True:
            if (data[y][x] == "E"):
                return new_p
            if x + dir < cols and (data[y][x + dir] == "." or data[y][x + dir] == "E") and (y,x+dir) not in p:
                x += dir
                new_p.append((y,x))
            if y + dir < rows and (data[y+dir][x] == "." or data[y][x + dir] == "E") and (y+dir,x) not in p:
                y+=dir
                new_p.append((y,x))
            dir += -1
                
    return new_p

if __name__ == "__main__":
    d16()
