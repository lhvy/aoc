from util import *

input = get_input_lines()

ids = []
for seat in input:
    row = [0, 127]
    column = [0, 7]
    for char in seat:
        if char == "F" or char == "B":
            if row[1] - row[0] == 1:
                if char == "F":
                    row = row[0]
                else:
                    row = row[1]
            elif char == "F":
                row[1] -= round((int(row[1]) - int(row[0])) / 2)
            else:
                row[0] += round((int(row[1]) - int(row[0])) / 2)
        else:
            if column[1] - column[0] == 1:
                if char == "L":
                    column = column[0]
                else:
                    column = column[1]
            elif char == "L":
                column[1] -= round((int(column[1]) - int(column[0])) / 2)
            else:
                column[0] += round((int(column[1]) - int(column[0])) / 2)
    ids.append(row * 8 + column)

ids.sort()

# Part 1
print(ids[-1])

# Part 2
for i in range(len(ids) - 1):
    if ids[i + 1] - ids[i] == 2:
        print(ids[i] + 1)
