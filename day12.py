import re
import itertools

with open('inputs/day12.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


def find_matches(springs, length):
    pattern = r'(?=(\?|#){{{}}})'.format(length)
    matches = re.finditer(pattern, springs)
    ranges = []
    for i, match in enumerate(matches, start=1):
        ranges.append((match.start(), match.start() + length - 1))
    return ranges


def generate_spring_options(springs):
    spring_list = springs.split(' ')[0]
    quides = springs.split(' ')[1].split(',')
    spring_options = []
    for guide in quides:
        spring_options.append({guide: find_matches(springs, int(guide))})
    return spring_options


def ranges_overlap(r1, r2):
    return not (r1[1] < r2[0] - 1 or r2[1] < r1[0] - 1)

def no_overlap(ranges_to_check):
    ranges_to_check = list(ranges_to_check)
    for i in range(len(ranges_to_check)):
        for j in range(i+1, len(ranges_to_check)):  # Start from i+1 to avoid comparing a range with itself
            if ranges_overlap(ranges_to_check[i], ranges_to_check[j]):
                return False
    return True

def get_combinations(spring_options):
    arrays = [list(d.values())[0] for d in spring_options]
    return list(itertools.product(*arrays))

def check_non_overlap(combinations):
    comb_subset = []
    for combination in combinations:
        if no_overlap(combination):
            comb_subset.append(combination)
    return comb_subset

def find_springs(springs):
    return [i for i, char in enumerate(springs) if char == '#']
        

def is_has_in_range(spring_location, ranges):
    for r in ranges:
        if spring_location >= r[0] and spring_location <= r[1]:
            return True
    return False

def check_spings_are_covered(comb_subset, spring_locations):
    final_comb_subset = []
    for subset in comb_subset:
        springs_covered = True 
        for spring_location in spring_locations:
            if not is_has_in_range(spring_location, subset):
                springs_covered = False
                break
        if springs_covered:
            final_comb_subset.append(subset)
    return final_comb_subset

def ranges_in_order(ranges):
    for i in range(len(ranges) - 1):
        if ranges[i][0] > ranges[i+1][0]:
            return False
    return True

def get_only_in_order_subsets(final_comb_subset):
    final_final_comb_subset = []
    for subset in final_comb_subset:
        if ranges_in_order(subset):
            final_final_comb_subset.append(subset)
    return final_final_comb_subset


# total = 0
# for line in lines:
#     print(line)
#     spring_options = {}
#     spring_options = generate_spring_options(line)

#     combinations = get_combinations(spring_options)

#     comb_subset = check_non_overlap(combinations)

#     spring_locations = find_springs(line.split(' ')[0])

#     final_comb_subset =  check_spings_are_covered(comb_subset, spring_locations)

#     final_final_comb_subset = get_only_in_order_subsets(final_comb_subset)

#     print(len(final_final_comb_subset))

#     total += len(final_final_comb_subset)

# print(total)



from multiprocessing import Pool
import pprint

def process_line(line):
    print(line)
    spring_options = {}
    spring_options = generate_spring_options(line)

    pprint.pprint(spring_options)

    combinations = get_combinations(spring_options)

    print(len(combinations))

    comb_subset = check_non_overlap(combinations)
    spring_locations = find_springs(line.split(' ')[0])
    final_comb_subset =  check_spings_are_covered(comb_subset, spring_locations)
    final_final_comb_subset = get_only_in_order_subsets(final_comb_subset)
    return len(final_final_comb_subset)

if __name__ == "__main__":
    with Pool() as p:
        results = p.map(process_line, lines)
    total = sum(results)
    print(total)

