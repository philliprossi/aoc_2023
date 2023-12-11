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
current_cell = (71,119) #(1,4)  #(2, 1)

step_count = 1
loop_coords = [start_location]
while current_cell != start_location:
    loop_coords.append(current_cell)
    loop_coords.append(( (current_cell[0] + previous_cell[0])/2, (current_cell[1]+ previous_cell[1])/2 ))


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

possible_tiles = [x for x in all_cells if x not in loop_coords]

#see if possible tile has path off grid by .5 steps
tiles_true = []
tiles_false = [] 
 
def check_tile_surroundings(tile, seen_tiles):
    seen_tiles.append(tile)

    if tile in tiles_true:
        return True
    
    if tile in tiles_false:
        return False

    #if tile is on edge return 'outside'
    if tile[0] == 0 or tile[0] == max_rows or tile[1] == 0 or tile[1] == max_cols:
        tiles_true.append(tile)
        return True
    
    if tile in loop_coords:
        tiles_false.append(tile)
        return False
    
    if tile[0] != int(tile[0]) and tile[1] != int(tile[1]):
        tiles_false.append(tile)
        return False
    
    possible_options = [
        (tile[0] - .5   , tile[1]),
        (tile[0] + .5   , tile[1]),
        (tile[0]        , tile[1] -.5),
        (tile[0]        , tile[1] +.5),
    ]

    returns = [] 
    for option in possible_options:
        if option not in seen_tiles:
            returns.append(check_tile_surroundings(option, seen_tiles))

    if any(returns):
        return True
    else:
        return False

tile_count = 0 
for tile in possible_tiles:

    if tile in tiles_true:
        continue

    seen_tiles = []
    returns = check_tile_surroundings(tile, seen_tiles)

    if not returns:
        tiles_false.append(seen_tiles)
        tile_count += 1
    else:
        tiles_true.append(seen_tiles)

    if tile_count>0:
        print(tile_count) 

print(tile_count)