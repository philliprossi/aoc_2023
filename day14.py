from progress.bar import Bar


with open('inputs/day14.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


def read_in_board(lines):
    round_rocks = {}
    cube_rocks = {}
    row = 0
    for line in lines:
        col = 0
        for c in line:
            if c == 'O':
               round_rocks[(row,col)] = c
            elif c == '#':
                cube_rocks[(row,col)] = c
            col += 1
        row += 1
    return round_rocks, cube_rocks, row, col


def sort_round_rocks(round_rocks_list, index = 0, reverse = False):
    #sort the round rocks by column
    return sorted(round_rocks_list, key=lambda x: x[index], reverse=reverse)



def shift_round_rocks(round_rocks, cube_rocks, direction = [-1,0], d = 'N'):
    #go through all the round rocks and shift them up until they hit the top or #
    new_round_rocks = {}

    if d == 'N':
        round_rocks = sort_round_rocks(list(round_rocks.keys()), 0, False)
    elif d == 'S':
        round_rocks = sort_round_rocks(list(round_rocks.keys()), 0, True)
    elif d == 'E':
        round_rocks = sort_round_rocks(list(round_rocks.keys()), 1, True)
    elif d == 'W':
        round_rocks = sort_round_rocks(list(round_rocks.keys()), 1, False)

    for rock in round_rocks:
        row, col = rock
        while True:
            if (d == 'N' and row == 0) or (d =='S' and row == rows - 1) or (d == 'E' and col == columns - 1) or (d == 'W' and col == 0):
                new_round_rocks[row,col] = 'O'
                break
            elif (row + direction[0], col + direction[1]) in cube_rocks:
                new_round_rocks[row,col] = 'O'
                break
            elif (row + direction[0], col + direction[1]) in new_round_rocks:
                new_round_rocks[row,col] = 'O'
                break
            else:
                row += direction[0]
                col += direction[1]

    return new_round_rocks

def print_board(new_round_rocks, cube_rocks, rows, columns):
    for x in range(rows):
        for y in range(columns):
            if (x,y) in new_round_rocks:
                print('O', end='')
            elif (x,y) in cube_rocks:
                print('#', end='')
            else:
                print('.', end='')
        print()


round_rocks, cube_rocks, rows, columns = read_in_board(lines)
new_round_rocks = shift_round_rocks(round_rocks, cube_rocks, [-1,0])

score = 0
for rock in new_round_rocks:
    score += columns - rock[0] 
print(score)

## PART 2
cycles = 1000000000
sample_cycles = 2000

round_rocks, cube_rocks, rows, columns = read_in_board(lines)

scores = []
for i in range(sample_cycles):
    round_rocks = shift_round_rocks(round_rocks, cube_rocks, [-1,0], 'N')
    round_rocks = shift_round_rocks(round_rocks, cube_rocks, [0,-1], 'W')
    round_rocks = shift_round_rocks(round_rocks, cube_rocks, [1,0], 'S')
    round_rocks = shift_round_rocks(round_rocks, cube_rocks, [0,1], 'E')

    score = 0
    for rock in round_rocks:
        score += columns - rock[0] 
    print(score)
    scores.append(score)    
        
def find_pattern(lst):
    length = len(lst)
    for pattern_length in range(1, length // 2 + 1):
        is_pattern = True
        for i in range(pattern_length, length):
            if lst[i] != lst[i % pattern_length]:
                is_pattern = False
                break
        if is_pattern:
            return lst[:pattern_length]
    return None

# Your list
pattern = find_pattern(scores[-1000:])
print(pattern)

first = 235
possible = [104820, 104870, 104900, 104911, 104919, 104911, 104914, 104921, 104909, 104889, 104866, 104826, 104771, 104708, 104640, 104568, 104508, 104450, 104394, 104330, 104248, 104157, 104080, 104002, 103909, 103819, 103735, 103661, 103621, 103589, 103557, 103521, 103489, 103462, 103445, 103436, 103443, 103462, 103479, 103513, 103548, 103582, 103637, 103685, 103733, 103800, 103882, 103963, 104049, 104142, 104223, 104294, 104367, 104434, 104504, 104577, 104642, 104698, 104759]
for i in range(235, 1000000000):
    i = (i+1) % len(possible)

possible[(1000000000 - 235) % 59 +1]