from util import *

input = get_input_lines()


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Grid:
    def __init__(self, max_x, max_y):
        self.grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    def draw(self, line):
        dir_x = 1 if line.x2 > line.x1 else -1
        dir_y = 1 if line.y2 > line.y1 else -1
        if line.x1 == line.x2:
            dir_x = 0
        if line.y1 == line.y2:
            dir_y = 0
        x = line.x1
        y = line.y1
        self.grid[y][x] += 1
        while x != line.x2 or y != line.y2:
            x += dir_x
            y += dir_y
            self.grid[y][x] += 1

    def find_intersections(self, num):
        intersections = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] > num:
                    intersections.append((x, y))
        return intersections


lines = []
max_x = 0
max_y = 0
for line in input:
    x1y1, x2y2 = line.split(" -> ")
    x1, y1 = x1y1.split(",")
    x2, y2 = x2y2.split(",")
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    if x1 > max_x:
        max_x = x1
    if x2 > max_x:
        max_x = x2
    if y1 > max_y:
        max_y = y1
    if y2 > max_y:
        max_y = y2
    if x1 > x2:  # Make line go left to right so gradient can be calculated
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    lines.append(Line(x1, y1, x2, y2))

# Part 1
grid = Grid(max_x, max_y)

for line in lines:
    if line.x1 == line.x2 or line.y1 == line.y2:
        grid.draw(line)

print(len(grid.find_intersections(1)))

# Part 2
grid = Grid(max_x, max_y)

for line in lines:
    if line.x1 == line.x2 or line.y1 == line.y2:
        grid.draw(line)
    elif abs((line.y2 - line.y1) / (line.x2 - line.x1)) == 1:
        grid.draw(line)

print(len(grid.find_intersections(1)))
