import re

with open("inputs/day19.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


def parse_input(lines):
    dict_operations = {}
    list_xmas = []
    for line in lines:
        if line == "":
            continue
        if "=" in line:
            line = line.strip("{}")
            pairs = line.split(",")
            list_xmas.append(
                {pair.split("=")[0]: int(pair.split("=")[1]) for pair in pairs}
            )
        else:
            key, commands = line.split("{")
            commands = commands.strip("}").split(",")
            dict_operations[key] = commands
    return dict_operations, list_xmas


dict_operations, list_xmas = parse_input(lines)


def run_through_options(calc_list: list, xmas: dict, dict_operations: dict):
    for calc in calc_list:
        val = calculator(calc, xmas, dict_operations)
        if val in ("A", "R"):
            return val
    return False


def calculator(calc_key: str, xmas: dict, dict_operations: dict):
    if calc_key == "A":
        return "A"
    elif calc_key == "R":
        return "R"
    if ":" in calc_key:
        calculation = calc_key.split(":")[0]
        parts = re.split("(<|>)", calculation)
        letter = parts[0]
        letter_value = xmas[letter]
        operator = parts[1]
        number = int(parts[2].split(":")[0])
        next_calc = calc_key.split(":")[1]

        if eval(f"{letter_value} {operator} {number}"):
            if next_calc in ("A", "R"):
                return next_calc
            next_calc_list = dict_operations[next_calc]
            return run_through_options(next_calc_list, xmas, dict_operations)
    else:
        return run_through_options(dict_operations[calc_key], xmas, dict_operations)


score = 0
for xmas in list_xmas:
    val = run_through_options(dict_operations["in"], xmas, dict_operations)
    if val == "A":
        score += xmas["x"] + xmas["m"] + xmas["a"] + xmas["s"]

score
