with open("inputs/day08.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


# Separate the data into two lists
rl_list = list(lines[0])
list2 = lines[2:]

# Create a dictionary from the assignments
assignments = {}
for item in list2:
    key, value = item.split(" = ")
    assignments[key] = value.strip("()").split(", ")


nodes = ["GPA", "GTA", "VDA", "BBA", "AAA", "VSA"]

rl_spot = 0
count = 0
distance_to_z = []
while True:
    count += 1
    rl = rl_list[rl_spot]
    new_nodes = []
    for node in nodes:
        if rl == "L":
            new_nodes.append(assignments[node][0])
        else:
            new_nodes.append(assignments[node][1])
    nodes = new_nodes
    rl_spot += 1
    rl_spot = rl_spot % len(rl_list)
    for node in nodes:
        if node[2] == "Z":
            keep_going = True
            distance_to_z.append(count)
    if len(distance_to_z) == len(nodes):
        break


import math

numbers = distance_to_z


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


lcm_value = numbers[0]
for num in numbers[1:]:
    lcm_value = lcm(lcm_value, num)

print("Part 2: " + str(lcm_value))
