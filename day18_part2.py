with open("inputs/day18.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

directions = {0: "R", 1: "D", 2: "L", 3: "U"}


def parse_input(lines):
    parsed = []
    for line in lines:
        direction = directions[int(line.split()[2][7])]
        hex_string = line.split()[2][2:7]
        distance = int(hex_string, 16)
        parsed.append((direction, distance))
    return parsed


input = parse_input(lines)

directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

lagoon = {}
position = (0, 0)
lagoon[position] = "#"
length = 0
for command in input:
    direction = directions[command[0]]
    position = (
        position[0] + (direction[0] * command[1]),
        position[1] + (direction[1] * command[1]),
    )
    lagoon[position] = command[0]
    length = length + command[1]


def shoelace_area(lagoon):
    points = list(lagoon.keys())
    points.append(points[0])
    area = 0.5 * abs(
        sum(
            x * y_next - y * x_next
            for ((x, y), (x_next, y_next)) in zip(points, points[1:])
        )
    )
    return area


area = shoelace_area(lagoon)

f = area + (length / 2) + 1
f
