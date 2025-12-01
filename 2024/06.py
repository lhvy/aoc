import util
import copy


def in_map(col, row):
    return col >= 0 and col < len(rows[0]) and row >= 0 and row < len(rows)


def seen_before(rows, row, col, visited):
    guard = rows[row][col]
    if guard == "^":
        if visited[row][col][0]:
            return True
        visited[row][col][0] = True
    elif guard == "v":
        if visited[row][col][1]:
            return True
        visited[row][col][1] = True
    elif guard == "<":
        if visited[row][col][2]:
            return True
        visited[row][col][2] = True
    elif guard == ">":
        if visited[row][col][3]:
            return True
        visited[row][col][3] = True

    return False


rows = [list(line) for line in util.get_input_lines()]
start_guard_row = -1
start_guard_col = -1
start_guard = "?"
for y, row in enumerate(rows):
    for x, col in enumerate(row):
        if col not in [".", "#"]:
            start_guard_row = y
            start_guard_col = x
            start_guard = col


def is_loop(rows, visited):
    rows = copy.deepcopy(rows)
    guard_row = start_guard_row
    guard_col = start_guard_col
    while in_map(guard_col, guard_row) and not seen_before(
        rows, guard_row, guard_col, visited
    ):
        guard = rows[guard_row][guard_col]
        rows[guard_row][guard_col] = "."
        if guard == "^":
            if guard_row > 0:
                if rows[guard_row - 1][guard_col] == "#":
                    rows[guard_row][guard_col] = ">"
                else:
                    guard_row -= 1
                    rows[guard_row][guard_col] = "^"
            else:
                guard_row -= 1
        elif guard == "v":
            if guard_row < len(rows) - 1:
                if rows[guard_row + 1][guard_col] == "#":
                    rows[guard_row][guard_col] = "<"
                else:
                    guard_row += 1
                    rows[guard_row][guard_col] = "v"
            else:
                guard_row += 1
        elif guard == "<":
            if guard_col > 0:
                if rows[guard_row][guard_col - 1] == "#":
                    rows[guard_row][guard_col] = "^"
                else:
                    guard_col -= 1
                    rows[guard_row][guard_col] = "<"
            else:
                guard_col -= 1
        elif guard == ">":
            if guard_col < len(rows[0]) - 1:
                if rows[guard_row][guard_col + 1] == "#":
                    rows[guard_row][guard_col] = "v"
                else:
                    guard_col += 1
                    rows[guard_row][guard_col] = ">"
            else:
                guard_col += 1
        else:
            raise ValueError(guard)
    rows[start_guard_row][start_guard_col] = start_guard
    return in_map(guard_col, guard_row)


visited = [[[False, False, False, False] for c in r] for r in rows]
is_loop(rows, visited)
total = 0
for row in visited:
    for col in row:
        total += any(col)
print(total)

total = 0
for y in range(len(rows)):
    for x in range(len(rows[y])):
        if rows[y][x] != ".":
            continue

        visited = [[[False, False, False, False] for c in r] for r in rows]
        rows[y][x] = "#"
        total += is_loop(rows, visited)
        rows[y][x] = "."
print(total)
