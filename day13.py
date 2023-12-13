with open('inputs/day13.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


def find_identical_columns(matrix):
    column_indexes = []
    for i in range(len(matrix[0]) - 1):
        if all(row[i] == row[i+1] for row in matrix):
            column_indexes.append(i)
    return column_indexes

def do_columns_match(matrix, index1, index2):
    if index1 < 0 or index2 >= len(matrix[0]):
        return False

    for row in matrix:
        if row[index1] != row[index2]:
            return False
    return True

def do_rows_match(matrix, index1, index2):
    if index1 < 0 or index2 >= len(matrix):
        return False

    if matrix[index1] != matrix[index2]:
        return False
    return True


def find_identical_rows(matrix):
    row_indexes = []
    for i in range(len(matrix) - 1):
        if matrix[i] == matrix[i + 1]:
            row_indexes.append(i)
    return row_indexes


def find_all_mirrored_columns(matrix, index):
    current_index = index
    index_offset = 1 
    matching_index = []
    last_range = []
    while True:
        if do_columns_match(matrix, current_index, current_index + index_offset):
            matching_index.append([current_index, current_index + index_offset])
            last_range = [current_index, current_index + index_offset]
        else:
            break

        current_index -= 1
        index_offset =  index_offset + 2

        if current_index < 0:
            break
        if current_index + index_offset > len(matrix[0]):
            break

    return last_range

def find_all_mirrored_rows(matrix, index):
    current_index = index
    index_offset = 1 
    matching_index = []
    last_range = []
    while True:

        if do_rows_match(matrix, current_index, current_index + index_offset):
            matching_index.append([current_index, current_index + index_offset])
            last_range = [current_index, current_index + index_offset]
        else:
            break
        current_index -= 1
        index_offset =  index_offset + 2

        if current_index < 0:
            break
        if current_index + index_offset > len(matrix):
            break

    return last_range


def process_input(file_path):
    with open(file_path, 'r') as file:
        matrices = file.read().strip().split('\n\n')
    matrices = [matrix.split('\n') for matrix in matrices]
    return matrices


def does_range_touch_edge_of_matrix(range, start, end):
    if range[0] == start or range[1] == end:
        return True
    return False


matrices = process_input('inputs/day13.txt')
total_score = 0
for i, matrix in enumerate(matrices):
    print(f"Matrix {i + 1}:---------------------------------------------------")

    column_match = find_identical_columns(matrix)
    row_match = find_identical_rows(matrix)

    range_columns = []
    for match in column_match:
        print(f"Column match at {match}")
        print(find_all_mirrored_columns(matrix, match))
        range_columns.append(find_all_mirrored_columns(matrix, match))

    range_rows = []
    for match in row_match:
        print(f"Row match at {match}")
        print(find_all_mirrored_rows(matrix, match))
        range_rows.append(find_all_mirrored_rows(matrix, match))

    for range_mirror in range_columns:
        if does_range_touch_edge_of_matrix(range_mirror, 0, len(matrix[0]) -1 ):
            print("Column range touches edge of matrix " + str(range_mirror))
            final_range = range_mirror
            score = (((final_range[1] - final_range[0] + 1)/2) + final_range[0])
            print(f"Score: {score}")
            total_score += score
            break
    
    for range_mirror in range_rows:
        if does_range_touch_edge_of_matrix(range_mirror, 0, len(matrix) -1 ):
            print("ROW range touches edge of matrix : " + str(range_mirror))
            final_range = range_mirror
            score =  ((((final_range[1] - final_range[0] + 1)/2) + final_range[0]))*100
            print(f"Score: {score}")
            total_score += score
            break


    print(f"Score: {score}")

    total_score += score


total_score

