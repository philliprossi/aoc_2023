with open("inputs/day11.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [list(c) for c in lines]

num_rows = len(lines)
num_cols = len(lines[0])

grid = {}
for row in range(num_rows):
    for col in range(num_cols):
        if lines[row][col] != ".":
            grid[(row, col)] = lines[row][col]

# find expansion on rows
expansion_factor_row = {}
for x in range(num_rows):
    # if none of the keys[0] of grid then expansion
    empty = True
    for y in range(num_cols):
        if (x, y) in grid:
            empty = False
            break

    if empty:
        for key, value in grid.items():
            if key[0] > x:
                if key not in expansion_factor_row:
                    expansion_factor_row[key] = 1
                else:
                    expansion_factor_row[key] += 1

# find expansion on cols
expansion_factor_col = {}
for y in range(num_cols):
    # if none of the keys[0] of grid then expansion
    empty = True
    for x in range(num_rows):
        if (x, y) in grid:
            empty = False
            break
    if empty:
        for key, value in grid.items():
            if key[1] > y:
                if key not in expansion_factor_col:
                    expansion_factor_col[key] = 1
                else:
                    expansion_factor_col[key] += 1


# adjust the grid based on the expansion factors
def created_adjusted_grid(
    grid, expansion_factor_row, expansion_factor_col, expansion_multiple=1
):
    adjusted_grid = {}
    for key, value in grid.items():
        if key in expansion_factor_row:
            adjusted_row = key[0] + (expansion_factor_row[key] * expansion_multiple)
        else:
            adjusted_row = key[0]
        if key in expansion_factor_col:
            adjusted_col = key[1] + (expansion_factor_col[key] * expansion_multiple)
        else:
            adjusted_col = key[1]
        adjusted_grid[(adjusted_row, adjusted_col)] = value
    return adjusted_grid


adjusted_grid = created_adjusted_grid(grid, expansion_factor_row, expansion_factor_col)

coords_list = list(adjusted_grid.keys())


# get the pair combinations of each value in coords_list
def get_pair_combinations(coords_list):
    pair_combinations = []
    for i in range(len(coords_list)):
        for j in range(i + 1, len(coords_list)):
            pair_combinations.append((coords_list[i], coords_list[j]))
    return pair_combinations


pair_combinations = get_pair_combinations(coords_list)


def get_manhatten_distance_between_each_point(pair_combinations):
    def manhattan_distance(point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    pair_distances = []
    for pair in pair_combinations:
        pair_distances.append(manhattan_distance(pair[0], pair[1]))
    return pair_distances


pair_distances = get_manhatten_distance_between_each_point(pair_combinations)

print(sum(pair_distances))


# Part 2

adjusted_grid_p2 = created_adjusted_grid(
    grid, expansion_factor_row, expansion_factor_col, expansion_multiple=(1000000 - 1)
)
coords_list_p2 = list(adjusted_grid_p2.keys())
pair_combinations_p2 = get_pair_combinations(coords_list_p2)
pair_distances_p2 = get_manhatten_distance_between_each_point(pair_combinations_p2)
print(sum(pair_distances_p2))
