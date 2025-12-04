import util

lines = util.get_input_lines()
lines = [list(l) for l in lines]

part_a = 0
part_b = 0

for y, l in enumerate(lines):
    for x, char in enumerate(l):
        if char != "@":
            continue
        c = 0

        if x > 0 and y > 0 and lines[y - 1][x - 1] == "@":
            c += 1
        if y > 0 and lines[y - 1][x] == "@":
            c += 1
        if x + 1 < len(l) and y > 0 and lines[y - 1][x + 1] == "@":
            c += 1
        if x > 0 and l[x - 1] == "@":
            c += 1
        if x + 1 < len(l) and l[x + 1] == "@":
            c += 1
        if x > 0 and y + 1 < len(lines) and lines[y + 1][x - 1] == "@":
            c += 1
        if y + 1 < len(lines) and lines[y + 1][x] == "@":
            c += 1
        if x + 1 < len(l) and y + 1 < len(lines) and lines[y + 1][x + 1] == "@":
            c += 1

        # print(x, y, char)
        part_a += 1 if c < 4 else 0

print("Part A: ", part_a)

stack: list[tuple[int, int]] = []
for y in range(len(lines)):
    for x in range(len(lines[0])):
        stack.append((x, y))

while len(stack) > 0:
    x, y = stack.pop()
    char = lines[y][x]

    if char != "@":
        continue
    c = 0
    recheck: list[tuple[int, int]] = []

    if x > 0 and y > 0 and lines[y - 1][x - 1] == "@":
        c += 1
        recheck.append((x - 1, y - 1))
    if y > 0 and lines[y - 1][x] == "@":
        c += 1
        recheck.append((x, y - 1))
    if x + 1 < len(lines[y]) and y > 0 and lines[y - 1][x + 1] == "@":
        c += 1
        recheck.append((x + 1, y - 1))
    if x > 0 and lines[y][x - 1] == "@":
        c += 1
        recheck.append((x - 1, y))
    if x + 1 < len(lines[y]) and lines[y][x + 1] == "@":
        c += 1
        recheck.append((x + 1, y))
    if x > 0 and y + 1 < len(lines) and lines[y + 1][x - 1] == "@":
        c += 1
        recheck.append((x - 1, y + 1))
    if y + 1 < len(lines) and lines[y + 1][x] == "@":
        c += 1
        recheck.append((x, y + 1))
    if x + 1 < len(lines[y]) and y + 1 < len(lines) and lines[y + 1][x + 1] == "@":
        c += 1
        recheck.append((x + 1, y + 1))

    if c < 4:
        lines[y][x] = "."
        part_b += 1
        stack.extend(recheck)

print("Part B: ", part_b)
