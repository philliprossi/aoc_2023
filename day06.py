import numpy as np

with open('inputs/day06.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


times = list(map(int, lines[0].split()[1:]))
distances = list(map(int, lines[1].split()[1:]))
time_distance_pairs = [{'time': t, 'distance': d} for t, d in zip(times, distances)]

"""
[{'time': 7, 'distance': 9},
 {'time': 15, 'distance': 40},
 {'time': 30, 'distance': 200}]
"""

# b = time 
# c = distance 
def get_distinces(b,c):
    # Coefficients of the quadratic equation
    a = 1
    b = -b
    c = c

    # Calculate the discriminant
    D = b**2 - 4*a*c

    # If the discriminant is non-negative, the equation has real roots
    if D >= 0:
        x1 = int((-b - np.sqrt(D)) / (2*a))  # Smaller root
        x2 = int((-b + np.sqrt(D)) / (2*a))  # Larger root
        # Find the integer values of x that satisfy the inequality
        x_values = [x for x in range(x1, x2+1) if a*x**2 + b*x + c < 0]
        # Find the corresponding values of D
        D_values = [7*x - x**2 for x in x_values]
    else:
        pass

    return x_values

record = 1 
for run in time_distance_pairs:
    record =  record * len(get_distinces(run['time'], run['distance']))

print(f"Day 6 Part 1 - {record}")


print(f"Day 6 Part 1 - {len(get_distinces(60808676,601116315591300))}")

