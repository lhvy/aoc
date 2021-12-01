from util import *

input = get_input_ints()

# Find sum to 2020
for i in range(len(input)):
    for j in range(i + 1, len(input)):
        if input[i] + input[j] == 2020:
            print(input[i] * input[j])

# Find 3 sum to 2020
for i in range(len(input)):
    for j in range(i + 1, len(input)):
        for k in range(j + 1, len(input)):
            if input[i] + input[j] + input[k] == 2020:
                print(input[i] * input[j] * input[k])
