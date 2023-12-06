with open('inputs/day05.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


seeds = [int(s) for s in lines[0].split(':')[1].split()]
lines = lines[2:]

def create_mapping(lines):
    mappings = {}
    current_key = None
    for line in lines:
        if line.endswith(':'):
            current_key = line[:-1]
            mappings[current_key] = []
        else:
            if len(line.split())>0:
                mappings[current_key].append(list(map(int, line.split())))
    return mappings

def mapping_source_to_ouput(seed, mappings):
    for mapping in mappings:
        if seed >= mapping[1] and seed <= mapping[1] + mapping[2] - 1:
            return mapping[0] + (seed - mapping[1])
    return seed


mappings = create_mapping(lines)
seed_location = []
for seed in seeds:
    intermim_mapping = seed
    for mapping, maps in mappings.items():
        intermim_mapping = mapping_source_to_ouput(intermim_mapping, maps)
    seed_location.append(intermim_mapping)

print(f"Day 5 Part 1 - {min(seed_location)}")



## Part 2
# reverse from lowest locations to seed in rangs

with open('inputs/day05.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


seeds = [int(s) for s in lines[0].split(':')[1].split()]
seed_ranges = []
# group every 2 sees in seeds
for i in range(0, len(seeds), 2):
    seed_ranges.append((seeds[i], seeds[i+1]))

lines = lines[2:]
mappings = create_mapping(lines)

min_range = [0, 180532143] #manual pick

def mapping_ouput_to_source(reverse_seed, mappings):
    for mapping in mappings:
        if reverse_seed >= mapping[0] and reverse_seed <= mapping[0] + mapping[2] - 1:
            return mapping[1] + (reverse_seed - mapping[0])
    return reverse_seed

def check_if_seed_in_seed_range(seed,seed_ranges):
    for seed_range in seed_ranges:
        if seed >= seed_range[0] and seed <= seed_range[0] + seed_range[1] -1:
            return True
    return False


for x in range(min_range[0],min_range[1]):
    intermim_mapping = x
    for mapping, maps in reversed(list(mappings.items())):
        intermim_mapping = mapping_ouput_to_source(intermim_mapping, maps)

    if check_if_seed_in_seed_range(intermim_mapping, seed_ranges):
        print(f"Day 5 Part 2 - {x}")
        break
    