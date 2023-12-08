
with open('inputs/day08.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


# Separate the data into two lists
rl_list = list(lines[0])
list2 = lines[2:]

# Create a dictionary from the assignments
assignments = {}
for item in list2:
    key, value = item.split(' = ')
    assignments[key] = value.strip('()').split(', ')

rl_spot = 0
node = 'AAA'
count = 0
while node != 'ZZZ':
    count += 1
    rl = rl_list[rl_spot]

    if rl == 'L':
        node = assignments[node][0]
    else:
        node = assignments[node][1]
    rl_spot += 1
    rl_spot = rl_spot % len(rl_list)

print("Part 1: " + str(count))

