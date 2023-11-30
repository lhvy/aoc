from util import *
from statistics import median

input = get_input_ints_comma()

# Part 1
med = median(input)
used = 0
for crab in input:
    if crab > med:
        used += crab - med
    else:
        used += med - crab

print(used)

# Part 2
min_pos = min(input)
max_pos = max(input)

min_cost = 99999999999999999

for i in range(min_pos, max_pos + 1):
    fuel = 0
    for crab in input:
        cost = 1
        if crab > i:
            diff = crab - i
        else:
            diff = i - crab
        while diff > 0:
            fuel += cost
            diff -= 1
            cost += 1
    if fuel < min_cost:
        min_cost = fuel
    else:
        break

print(min_cost)
