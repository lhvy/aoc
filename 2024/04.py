import util

lines = util.get_input_lines()

total = 0
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "X":
            if x >= 3 and line[x - 3 : x] == "SAM":
                total += 1
            if x + 3 < len(line) and line[x + 1 : x + 4] == "MAS":
                total += 1
            if (
                y >= 3
                and lines[y - 1][x] == "M"
                and lines[y - 2][x] == "A"
                and lines[y - 3][x] == "S"
            ):
                total += 1
            if (
                y + 3 < len(lines)
                and lines[y + 1][x] == "M"
                and lines[y + 2][x] == "A"
                and lines[y + 3][x] == "S"
            ):
                total += 1
            if (
                x >= 3
                and y >= 3
                and lines[y - 1][x - 1] == "M"
                and lines[y - 2][x - 2] == "A"
                and lines[y - 3][x - 3] == "S"
            ):
                total += 1
            if (
                x >= 3
                and y + 3 < len(lines)
                and lines[y + 1][x - 1] == "M"
                and lines[y + 2][x - 2] == "A"
                and lines[y + 3][x - 3] == "S"
            ):
                total += 1
            if (
                x + 3 < len(line)
                and y + 3 < len(lines)
                and lines[y + 1][x + 1] == "M"
                and lines[y + 2][x + 2] == "A"
                and lines[y + 3][x + 3] == "S"
            ):
                total += 1
            if (
                x + 3 < len(line)
                and y >= 3
                and lines[y - 1][x + 1] == "M"
                and lines[y - 2][x + 2] == "A"
                and lines[y - 3][x + 3] == "S"
            ):
                total += 1
print(total)


total = 0
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "A" and x > 0 and x + 1 < len(line) and y > 0 and y + 1 < len(line):
            if (
                (
                    lines[y - 1][x - 1] == "M"
                    and lines[y - 1][x + 1] == "M"
                    and lines[y + 1][x - 1] == "S"
                    and lines[y + 1][x + 1] == "S"
                )
                or (
                    lines[y - 1][x - 1] == "S"
                    and lines[y - 1][x + 1] == "S"
                    and lines[y + 1][x - 1] == "M"
                    and lines[y + 1][x + 1] == "M"
                )
                or (
                    lines[y - 1][x - 1] == "S"
                    and lines[y - 1][x + 1] == "M"
                    and lines[y + 1][x - 1] == "S"
                    and lines[y + 1][x + 1] == "M"
                )
                or (
                    lines[y - 1][x - 1] == "M"
                    and lines[y - 1][x + 1] == "S"
                    and lines[y + 1][x - 1] == "M"
                    and lines[y + 1][x + 1] == "S"
                )
            ):
                total += 1
print(total)
