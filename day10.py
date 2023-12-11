import sys

sys.setrecursionlimit(100000)

with open('inputs/day10.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [list(c) for c in lines]

#(row, column): { 'symbol': next_spot (row, column) }
move_options = {
    '|': [(-1,0), (1,0)],
    '-': [(0,-1), (0,1)],
    'L': [(-1,0), (0,1)],
    'J': [(-1,0), (0,-1)],
    '7': [(0,-1), (1,0)],
    'F': [(0,1), (1,0)],
}

# Find the location of 'S'
for i, row in enumerate(lines):
    for j, cell in enumerate(row):
        if cell == 'S':
            start_location = (i, j)
start_location


map = {}
row_num = 0
all_cells = []
for row in lines:
    col_num = 0
    for cell in row:
        map[(row_num, col_num)] = cell
        all_cells.append((row_num, col_num))
        col_num +=1
    row_num += 1 

previous_cell  = start_location # (2,0) (72,119)
current_cell = (71,119) #(71,119) #(1,4)  #(2, 1)

step_count = 1
loop_coords = [start_location]
while current_cell != start_location:
    loop_coords.append(current_cell)
    #loop_coords.append(( (current_cell[0] + previous_cell[0])/2, (current_cell[1]+ previous_cell[1])/2 ))


    current_cell_val = map[current_cell]
    next_cell_options = move_options[current_cell_val]

    next_cell_coords = []
    for next_cell in next_cell_options:
        next_cell_coords.append((next_cell[0] + current_cell[0], next_cell[1] + current_cell[1]))        

    for next_cell in next_cell_coords:
        if next_cell != previous_cell:
            previous_cell = current_cell
            current_cell = next_cell
            #print(current_cell)
            break
    step_count += 1

print(step_count/2) # <<--- PART 1


#find outside walls
max_rows = len(lines) - 1
max_cols = len(lines[0]) - 1


north_facing_pipe = ['|','L','J', 'S']
north_count = 0
tile_count = 0
for row in range(len(lines)):
    north_count = 0
    for col in range(len(lines[0])):
        if (row, col) in loop_coords:
            if map[(row, col)] in north_facing_pipe:
                north_count+=1
        else:
            if north_count % 2 == 1:
                tile_count += 1

print(tile_count)