import heapq

with open("inputs/day17.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


grid = []
for line in lines:
    gl = list(line)
    gl = [int(x) for x in gl]
    grid.append(gl)


def get_neighbors(position, direction, straight_moves, grid):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    for dx, dy in directions:
        new_direction = (dx, dy)
        if direction is not None:
            # Skip reverse direction
            if new_direction == (-direction[0], -direction[1]):
                continue
            # Limit straight moves
            if new_direction == direction and straight_moves >= 3:
                continue

        new_position = (position[0] + dx, position[1] + dy)
        if 0 <= new_position[0] < len(grid) and 0 <= new_position[1] < len(grid[0]):
            new_straight_moves = straight_moves + 1 if new_direction == direction else 1
            neighbors.append((new_position, new_direction, new_straight_moves))
    return neighbors


def dijkstra(grid, start, end):
    queue = []
    for direction in [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ]:  # Initialize all possible directions from start
        heapq.heappush(
            queue, (grid[start[0]][start[1]], start, direction, 1, [start])
        )  # heat loss, position, direction, straight count, path

    visited = set()

    while queue:
        heat_loss, position, direction, straight_count, path = heapq.heappop(queue)
        if position == end:
            return path + [position], heat_loss

        if (position, direction, straight_count) in visited:
            continue
        visited.add((position, direction, straight_count))

        for new_position, new_direction, new_straight_moves in get_neighbors(
            position, direction, straight_count, grid
        ):
            new_heat_loss = heat_loss + grid[new_position[0]][new_position[1]]
            new_path = path + [position]
            heapq.heappush(
                queue,
                (
                    new_heat_loss,
                    new_position,
                    new_direction,
                    new_straight_moves,
                    new_path,
                ),
            )

    return None, None


start = (0, 0)  # Starting position
end = (len(grid) - 1, len(grid[0]) - 1)  # Ending position

path, heat_loss = dijkstra(grid, start, end)
if path:
    print("Path found:", path)
    print("Total heat loss:", heat_loss)
else:
    print("No path found")


def print_grid_with_path(grid, path):
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if (i, j) in path:
                print("#", end="")
            else:
                print(c, end="")
        print()


print_grid_with_path(grid, path)
