from util import *

input = get_input_lines()

grid = []
for line in input:
    grid.append([])
    for c in line:
        grid[-1].append(c)


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y


safe = 0
basins = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        current = grid[y][x]
        if y > 0:
            # if x > 0:
            #     if grid[y - 1][x - 1] < current:
            #         continue
            if grid[y - 1][x] <= current:
                continue
            # if x < len(grid[y]) - 1:
            #     if grid[y - 1][x + 1] < current:
            #         continue
        if x > 0:
            if grid[y][x - 1] <= current:
                continue
        if x < (len(grid[y]) - 1):
            if grid[y][x + 1] <= current:
                continue
        if y < (len(grid) - 1):
            # if x > 0:
            #     if grid[y + 1][x - 1] < current:
            #         continue
            if grid[y + 1][x] <= current:
                continue
            # if x < len(grid[y]) - 1:
            #     if grid[y + 1][x + 1] < current:
            #         continue
        safe += 1 + int(current)
        basins.append(Pos(x, y))

print(safe)


def sum_lower_points(x, y):
    print(x, y, grid[y][x])
    current = int(grid[y][x])
    if current == 9:
        return 0
    s = 1
    if y > 0:
        if x > 0:
            if int(grid[y - 1][x - 1]) == current + 1:
                s += sum_lower_points(x - 1, y - 1)
        if int(grid[y - 1][x]) == current + 1:
            s += sum_lower_points(x, y - 1)
        if x < len(grid[y]) - 1:
            if int(grid[y - 1][x + 1]) == current + 1:
                s += sum_lower_points(x + 1, y - 1)
    if x > 0:
        if int(grid[y][x - 1]) == current + 1:
            s += sum_lower_points(x - 1, y)
    if x < (len(grid[y]) - 1):
        if int(grid[y][x + 1]) + 1 == current:
            s += sum_lower_points(x + 1, y)
    if y < (len(grid) - 1):
        if x > 0:
            if int(grid[y + 1][x - 1]) == current + 1:
                s += sum_lower_points(x - 1, y + 1)
        if int(grid[y + 1][x]) == current + 1:
            s += sum_lower_points(x, y + 1)
        if x < len(grid[y]) - 1:
            if int(grid[y + 1][x + 1]) == current + 1:
                s += sum_lower_points(x + 1, y + 1)
    return s


s = 1
print(sum_lower_points(basins[0].x, basins[0].y))
# s *= sum_lower_points(basins[0].x, basins[0].y)

print(s)
