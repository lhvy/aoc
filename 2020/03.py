from util import *

input = get_input_lines()


class Position:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width

    def move_right(self, n):
        self.x += n
        if self.x >= self.width:
            self.x -= self.width

    def move_down(self, n):
        self.y += n

    def x(self):
        return self.x

    def y(self):
        return self.y


def count_trees(right, down):
    pos = Position(0, 0, len(input[0]))
    trees = 0

    while pos.y < len(input):
        if input[pos.y][pos.x] == "#":
            trees += 1
        pos.move_right(right)
        pos.move_down(down)
    return trees


# Part 1
print(count_trees(3, 1))

# Part 2
print(
    count_trees(1, 1)
    * count_trees(3, 1)
    * count_trees(5, 1)
    * count_trees(7, 1)
    * count_trees(1, 2)
)
