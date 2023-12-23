import sys
sys.setrecursionlimit(10000) 

with open("inputs/day23.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]



def find_longest_hike_corrected(map_grid, ignore_directions = False):
    # Parsing the map into a grid
    grid = map_grid
    rows = len(grid)
    cols = len(grid[0])

    if ignore_directions:
        grid = [[c if c == '#' else '.' for c in row] for row in grid]

    # Directions for slopes
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

    # Function to check if a move is valid
    def is_valid(x, y, visited):
        return 0 <= x < rows and 0 <= y < cols and grid[x][y] != '#' and (x, y) not in visited

    # Backtracking function to explore all paths
    def backtrack(x, y, visited):
        # Add current position to visited
        visited.add((x, y))
        max_length = 0

        # If we reach the bottom row, return the length of the path
        if x == rows - 1:
            max_length = len(visited)

        # Check adjacent cells based on the type of the current cell
        if not ignore_directions and grid[x][y] in directions:
            dx, dy = directions[grid[x][y]]
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, visited):
                max_length = max(max_length, backtrack(new_x, new_y, visited))

        # For '.' tiles, try all four directions
        elif grid[x][y] == '.':
            for dx, dy in directions.values():
                new_x, new_y = x + dx, y + dy
                if is_valid(new_x, new_y, visited):
                    max_length = max(max_length, backtrack(new_x, new_y, visited))

        # Remove current position from visited before backtracking
        visited.remove((x, y))
        return max_length

    # Find the starting point in the top row
    start_col = grid[0].index('.')
    longest_hike = backtrack(0, start_col, set())

    return longest_hike


# Calculate the longest hike
# Recalculate the longest hike
longest_hike_corrected = find_longest_hike_corrected(lines)
print(longest_hike_corrected -1)


longest_hike_corrected = find_longest_hike_corrected(lines, True)
print(longest_hike_corrected -1)