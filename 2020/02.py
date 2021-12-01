from util import *

input = get_input_lines()


class Line:
    def __init__(self, min, max, char, password):
        self.min = min
        self.max = max
        self.char = char
        self.password = password

    def validate(self):
        return self.min <= self.password.count(self.char) <= self.max

    def validate_2(self):
        return (
            self.password[self.min - 1] == self.char != self.password[self.max - 1]
            or self.password[self.max - 1] == self.char != self.password[self.min - 1]
        )


valid = 0
valid_2 = 0

for line in input:
    min, max = line.split("-")
    max, char, password = max.split(" ", 2)
    min = int(min)
    max = int(max)
    char = char.strip(":")
    print(min, max, char, password)

    line = Line(min, max, char, password)
    if line.validate():
        valid += 1
    if line.validate_2():
        valid_2 += 1

print("Part 1:", valid)
print("Part 2:", valid_2)
