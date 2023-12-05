with open('inputs/day05.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


seeds = [int(s) for s in lines[0].split(':')[1].split()]
lines = lines[2:]

mappings = {}
current_key = None
for line in lines:
    if line.endswith(':'):
        current_key = line[:-1]
        mappings[current_key] = []
    else:
        if len(line.split())>0:
            mappings[current_key].append(list(map(int, line.split())))


def mapping_source_to_ouput(seed, mappings):
    for mapping in mappings:
        if seed >= mapping[1] and seed <= mapping[1] + mapping[2] - 1:
            return mapping[0] + (seed - mapping[1])
    return seed


seed_location = []
for seed in seeds:
    intermim_mapping = seed
    for mapping, maps in mappings.items():
        intermim_mapping = mapping_source_to_ouput(intermim_mapping, maps)
    seed_location.append(intermim_mapping)

print(f"Day 5 Part 1 - {min(seed_location)}")