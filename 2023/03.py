raw = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()


class Gear:
    def __init__(self):
        self.gears = {}

    def add(self, y, x, number):
        if (x, y) in self.gears:
            self.gears[(x, y)].append(number)
        else:
            self.gears[(x, y)] = [number]

    def finish(self):
        print(self.gears)
        total = 0
        for gear in self.gears.values():
            if len(gear) != 2:
                continue
            total += gear[0] * gear[1]
        return total


def isSymbol(c: str):
    return c != "." and not c.isalnum()


def isGear(c: str):
    return c == "*"


y = 0
x = 0
total = 0
while y < len(raw):
    x = 0
    number = ""
    adjacent = False
    while x < len(raw[y]):
        if not raw[y][x].isdigit():
            if adjacent:
                total += int(number)
            number = ""
            adjacent = False
            x += 1
            continue
        number += raw[y][x]
        up = y > 0 and isSymbol(raw[y - 1][x])
        up_left = y > 0 and x > 0 and isSymbol(raw[y - 1][x - 1])
        up_right = y > 0 and x < len(raw[y]) - 1 and isSymbol(raw[y - 1][x + 1])
        down = y < len(raw) - 1 and isSymbol(raw[y + 1][x])
        down_left = y < len(raw) - 1 and x > 0 and isSymbol(raw[y + 1][x - 1])
        down_right = (
            y < len(raw) - 1 and x < len(raw[y]) - 1 and isSymbol(raw[y + 1][x + 1])
        )
        left = x > 0 and isSymbol(raw[y][x - 1])
        right = x < len(raw[y]) - 1 and isSymbol(raw[y][x + 1])
        if not adjacent and (
            up
            or down
            or left
            or right
            or up_left
            or up_right
            or down_left
            or down_right
        ):
            adjacent = True
        x += 1
    if adjacent:
        total += int(number)
    y += 1

y = 0
x = 0
gears = Gear()
while y < len(raw):
    x = 0
    number = ""
    adjacent = False
    while x < len(raw[y]):
        if not isGear(raw[y][x]):
            x += 1
            continue

        if x > 0:
            number = ""
            temp_x = x - 1
            while temp_x >= 0 and raw[y][temp_x].isdigit():
                number = raw[y][temp_x] + number
                temp_x -= 1
            if len(number) > 0:
                gears.add(x, y, int(number))

        if x < len(raw[y]) - 1:
            number = ""
            temp_x = x + 1
            while temp_x <= len(raw[y]) - 1 and raw[y][temp_x].isdigit():
                number += raw[y][temp_x]
                temp_x += 1
            if len(number) > 0:
                gears.add(x, y, int(number))

        if y > 0:
            number = ""
            temp_x = x + 1
            while temp_x <= len(raw[y - 1]) - 1 and raw[y - 1][temp_x].isdigit():
                number += raw[y - 1][temp_x]
                temp_x += 1

            if raw[y - 1][x].isdigit():
                number = raw[y - 1][x] + number
            elif len(number) > 0:
                gears.add(x, y, int(number))
                number = ""
            else:
                number = ""

            temp_x = x - 1
            while temp_x >= 0 and raw[y - 1][temp_x].isdigit():
                number = raw[y - 1][temp_x] + number
                temp_x -= 1
            if len(number) > 0:
                gears.add(x, y, int(number))

        if y < len(raw) - 1:
            number = ""
            temp_x = x + 1
            while temp_x <= len(raw[y + 1]) - 1 and raw[y + 1][temp_x].isdigit():
                number += raw[y + 1][temp_x]
                temp_x += 1

            if raw[y + 1][x].isdigit():
                number = raw[y + 1][x] + number
            elif len(number) > 0:
                gears.add(x, y, int(number))
                number = ""
            else:
                number = ""

            temp_x = x - 1
            while temp_x >= 0 and raw[y + 1][temp_x].isdigit():
                number = raw[y + 1][temp_x] + number
                temp_x -= 1
            if len(number) > 0:
                gears.add(x, y, int(number))

        x += 1
    y += 1


print(total)
print(gears.finish())
