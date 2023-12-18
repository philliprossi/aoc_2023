with open("inputs/day15.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

codes = lines[0].split(",")

hashes = []
for code in codes:
    hash = 0
    for c in code:
        ascii_value = ord(c)
        hash = (hash + ascii_value) * 17 % 256
    hashes.append(hash)

print(sum(hashes))


boxes = [[] for _ in range(256)]
for code in codes:
    focal_length = None
    if "=" in code:
        lense = code.split("=")[0]
        focal_length = int(code.split("=")[1])
    elif "-" in code:
        lense = code.split("-")[0]

    hash = 0
    for c in lense:
        ascii_value = ord(c)
        hash = (hash + ascii_value) * 17 % 256

    if focal_length:
        placed = False
        for box_lense in boxes[hash]:
            if box_lense[0] == lense:
                box_lense[1] = focal_length
                placed = True
                break
        if not placed:
            boxes[hash].append([lense, focal_length])
    else:
        x = 0
        found = False
        for box_lense in boxes[hash]:
            if box_lense[0] == lense:
                found = True
                break
            x += 1
        if found:
            boxes[hash].pop(x)


score = 0
for x, box in enumerate(boxes):
    for y, lense in enumerate(box):
        score += (1 + x) * (1 + y) * lense[1]

print(score)
