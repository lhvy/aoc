from copy import deepcopy
from util import *

input = get_input_ints_comma()

input_population = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for fish in input:
    input_population[fish] += 1


def tick(days, input):
    for _ in range(days):
        population = deepcopy(input)
        for i in range(len(input)):
            if i == 0:
                population[6] += input[i]
                population[8] += input[i]
                population[0] -= input[i]
            else:
                population[i - 1] += input[i]
                population[i] -= input[i]
        input = deepcopy(population)
    return sum(input)


# Part 1
print(tick(80, input_population))

# Part 2
print(tick(256, input_population))
