
with open('inputs/day09.txt') as f:
    lines = f.readlines()
    lines = [line.strip().split() for line in lines]
    lines = [[int(c) for c in line] for line in lines]


def build_matrix(line):
    all_rows = []
    all_rows.append(line)
    while True: 
        new_line = []
        for x in range(len(line)-1):
            new_line.append(line[x+1] - line[x])
        all_rows.append(new_line)

        #if every value in new_line == 0
        if all(x == 0 for x in new_line):
            break
        else:
            line = new_line
    return all_rows

def add_score(all_rows):
    previous_value = 0
    for row in all_rows[::-1]:
        row.append(row[-1] + previous_value)
        previous_value = row[-1]
    return all_rows

def final_score(all_rows):
    return all_rows[0][-1]

all_scores = []
for line in lines:
    all_rows = build_matrix(line)
    add_score(all_rows)
    final_score_num = final_score(all_rows)
    all_scores.append(final_score_num)

print(sum(all_scores))

def add_score_start(all_rows):
    previous_value = 0
    for row in all_rows[::-1]:
        row.insert(0, row[0] - previous_value)
        previous_value = row[0]
    return all_rows

def final_score_reverse(all_rows):
    return all_rows[0][0]

all_scores_reverse = []
for line in lines:
    all_rows_reverse = build_matrix(line)
    add_score_start(all_rows_reverse)
    final_score_num = final_score_reverse(all_rows_reverse)
    all_scores_reverse.append(final_score_num)

print(sum(all_scores_reverse))