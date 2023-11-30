from util import *

input = get_input_ints()

# Part 1
prev = []
for i in range(len(input)):
    if i < 25:
        prev.append(input[i])
    else:
        valid = False
        for j in range(len(prev)):
            for k in range(j, len(prev)):
                if prev[j] + prev[k] == input[i]:
                    valid = True
        prev.pop(0)
        prev.append(input[i])
        if not valid:
            print(input[i])
