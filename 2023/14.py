# This code is seriously problematic. I am very pushed for time. Needs refactoring!
import functools

raw_lines = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()
plate = tuple([tuple([c for c in line]) for line in raw_lines])
for p in plate:
    print("".join(p))
print("")


# Part One
@functools.cache
def north(p):
    for y, line in enumerate(p):
        for x, c in enumerate(line):
            if c != "O":
                continue
            temp_y = y
            while temp_y > 0 and p[temp_y - 1][x] not in ["O", "#"]:
                p = (
                    p[: temp_y - 1]
                    + tuple(
                        [
                            p[temp_y - 1][:x] + tuple("O") + p[temp_y - 1][x + 1 :],
                            p[temp_y][:x] + tuple(".") + p[temp_y][x + 1 :],
                        ]
                    )
                    + p[temp_y + 1 :]
                )
                temp_y -= 1
    return p


@functools.cache
def south(p):
    for y, line in reversed(list(enumerate(p))):
        for x, c in enumerate(line):
            if c != "O":
                continue
            temp_y = y
            while temp_y < len(p) - 1 and p[temp_y + 1][x] not in ["O", "#"]:
                p = (
                    p[:temp_y]
                    + tuple(
                        [
                            p[temp_y][:x] + tuple(".") + p[temp_y][x + 1 :],
                            p[temp_y + 1][:x] + tuple("O") + p[temp_y + 1][x + 1 :],
                        ]
                    )
                    + p[temp_y + 2 :]
                )
                temp_y += 1
    return p


@functools.cache
def west(p):
    for y, line in enumerate(p):
        for x, c in list(enumerate(line)):
            if c != "O":
                continue
            temp_x = x
            while temp_x > 0 and p[y][temp_x - 1] not in ["O", "#"]:
                p = (
                    p[:y]
                    + tuple(
                        [p[y][: temp_x - 1] + tuple(["O", "."]) + p[y][temp_x + 1 :]]
                    )
                    + p[y + 1 :]
                )
                temp_x -= 1
    return p


@functools.cache
def east(p):
    for y, line in enumerate(p):
        for x, c in reversed(list(enumerate(line))):
            if c != "O":
                continue
            temp_x = x
            while temp_x < len(p[y]) - 1 and p[y][temp_x + 1] not in ["O", "#"]:
                p = (
                    p[:y]
                    + tuple([p[y][:temp_x] + tuple([".", "O"]) + p[y][temp_x + 2 :]])
                    + p[y + 1 :]
                )
                temp_x += 1
    return p


plate = north(plate)
load = 0
for y, line in enumerate(plate):
    for x, c in enumerate(line):
        if c == "O":
            load += len(plate) - y
print(load)

plate = west(plate)
plate = south(plate)
plate = east(plate)

hashes = [hash(plate)]
cycles = 1

while cycles < 1000000000 - 1:
    plate = north(plate)
    plate = west(plate)
    plate = south(plate)
    plate = east(plate)
    h = hash(plate)
    if h in hashes:
        gap = cycles - hashes.index(h)
        while cycles + gap < 1000000000 - 1:
            cycles += gap
        hashes = []
    else:
        cycles += 1
        hashes.append(h)
load = 0
for y, line in enumerate(plate):
    for x, c in enumerate(line):
        if c == "O":
            load += len(plate) - y
print(load)
