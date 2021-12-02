from util import *

input = get_input_lines()


class Submarine:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_x(self, x):
        self.x += x

    def move_y(self, y):
        self.y += y

    def position(self):
        return self.x * self.y


class SubmarineAim:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.aim = 0

    def move_x(self, x):
        self.x += x
        self.y += self.aim * x

    def move_y(self, y):
        self.aim += y

    def position(self):
        return self.x * self.y


def calculate(sub):
    for line in input:
        direction, distance = line.split()
        distance = int(distance)
        if direction == "forward":
            sub.move_x(distance)
        elif direction == "down":
            sub.move_y(distance)
        elif direction == "up":
            sub.move_y(-distance)
        else:
            print("Unknown direction:", direction)
    print(sub.position())


# Part 1
sub = Submarine()
calculate(sub)

# Part 2
sub_with_aim = SubmarineAim()
calculate(sub_with_aim)
