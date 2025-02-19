# too low: 6288751362253
# 6288751362253
# test input: 1928

def d10():
    grid = []
    with open("input.txt", "r") as f:
    # with open("input_d09.txt", "r") as f:
        grid = [line.strip() for line in f.readlines()]
    print(grid)
    final_state = simulate_map(grid)
    print(final_state)

def simulate_map(grid):
    cols, rows = len(grid[0]), len(grid)
    start_pos = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                start_pos.append((r, c))
    
    print("start_pos \n", start_pos)
    
    # Directions for moving in the grid: right, left, down, up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    total_paths = 0

    def dfs(r, c, visited):
        nonlocal total_paths
        if grid[r][c] == 9:
            total_paths += 1
            return
        
        visited.add((r, c))
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc): #not in visited
                if abs(grid[nr][nc] - grid[r][c]) == 1:  # Check if the difference is 1
                    dfs(nr, nc, visited)
        
        visited.remove((r, c))  # Backtrack
        
        # Start DFS from each starting position
    # Start DFS from each starting position
    for start in start_pos:
        paths_from_start = 0
        # Reset total_paths for each starting position
        total_paths = 0
        dfs(start[0], start[1], set())
        print(f"From {start} -> {total_paths} ways")
    
    return total_paths

    return res
        



if __name__ == "__main__":
    d10()