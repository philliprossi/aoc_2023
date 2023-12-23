with open("inputs/day21.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

def read_grid(lines):
    grid = {}
    start = None
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '.':
                grid[(i, j)] = c
            if c == 'S':
                start = (i, j)
                grid[(i, j)] = '.'
    return grid, start


grid, start = read_grid(lines)

def infinite_grid(i, j):
    max_i = len(lines)
    max_j = len(lines[0])
    adjusted_i = i % max_i
    adjusted_j = j % max_j
    if (adjusted_i, adjusted_j) in grid:
        return True
    else:
        return False

def walk_steps(last_steps, checks):
    new_last_steps = set([])
    for step in last_steps:
        for ij in checks:
            if infinite_grid(step[0] + ij[0], step[1] + ij[1]):
                new_last_steps.add((step[0] + ij[0], step[1] + ij[1]))
    return new_last_steps

def walk_grid(steps = 64):
    checks = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    step_grid = set([])
    last_steps = set([start])
    while steps > 0:
        new_last_steps = walk_steps(last_steps, checks)
        step_grid = step_grid.union(last_steps)
        last_steps = new_last_steps
        steps -= 1
    return last_steps

def print_grid(grid, step_grid):
    for i in range(0, len(lines)):
        for j in range(0, len(lines[0])):
            if (i, j) in step_grid:
                print('O', end='')
            elif (i, j) in grid:
                print('.', end='')
            else:
                print('#', end='')
        print()



#print_grid(grid, last_steps)
print(len(walk_grid(64))) 



#print(len(walk_grid(500))+1) 


print("part2")
print(len(walk_grid(64)))
print(len(walk_grid(128)))
print(len(walk_grid(256)))
print(len(walk_grid(1024)))    
print(len(walk_grid(4096))) 

