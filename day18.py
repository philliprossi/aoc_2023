with open("inputs/day18.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


def parse_input(lines):
    parsed = []
    for line in lines:
        line = line.split()
        direction = line[0]
        distance = int(line[1])
        colour = line[2][1:8]
        parsed.append((direction, distance, colour))
    return parsed


input = parse_input(lines)

directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

lagoon = {}
position = (0, 0)
lagoon[position] = "#"

for command in input:
    direction = directions[command[0]]
    for i in range(command[1]):
        position = (position[0] + direction[0], position[1] + direction[1])
        lagoon[position] = command[0]

# get the min and max x and y values
x = [i[0] for i in lagoon.keys()]
y = [i[1] for i in lagoon.keys()]

min_x = min(x)
max_x = max(x)
min_y = min(y)
max_y = max(y)

# print the lagoon
for i in range(min_x - 1, max_x + 2):
    for j in range(min_y - 1, max_y + 2):
        if (i, j) in lagoon:
            print(lagoon[(i, j)], end="")
        else:
            print(".", end="")
    print("")


start = (1, 1)
seen = set()
to_check = [start]
while to_check:
    current = to_check.pop()
    seen.add(current)
    x, y = current
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_pos = (x + dx, y + dy)
        if next_pos not in seen and next_pos not in to_check and next_pos not in lagoon:
            to_check.append(next_pos)

print(len(seen) + len(lagoon))
