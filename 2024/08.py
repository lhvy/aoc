import util
from itertools import combinations

rows = util.get_input_lines()
rows = [list(row) for row in rows]

antennas: dict[str, list[list[int]]] = {}
for y, row in enumerate(rows):
    for x, col in enumerate(row):
        if col != ".":
            if col in antennas:
                antennas[col].append([x, y])
            else:
                antennas[col] = [[x, y]]

antinodes = set()
for freq in antennas:
    for a, b in combinations(antennas[freq], 2):
        diff_x = b[0] - a[0]
        diff_y = b[1] - a[1]
        if (
            a[1] - diff_y >= 0
            and a[1] - diff_y < len(rows)
            and a[0] - diff_x >= 0
            and a[0] - diff_x < len(rows[0])
        ):
            antinodes.add(tuple([a[0] - diff_x, a[1] - diff_y]))
        if (
            b[1] + diff_y >= 0
            and b[1] + diff_y < len(rows)
            and b[0] + diff_x >= 0
            and b[0] + diff_x < len(rows[0])
        ):
            antinodes.add(tuple([b[0] + diff_x, b[1] + diff_y]))
print(len(antinodes))

antinodes = set()
for freq in antennas:
    for a, b in combinations(antennas[freq], 2):
        antinodes.add(tuple(a))
        antinodes.add(tuple(b))
        diff_x = b[0] - a[0]
        diff_y = b[1] - a[1]
        a_x = a[0] - diff_x
        a_y = a[1] - diff_y
        while a_y >= 0 and a_y < len(rows) and a_x >= 0 and a_x < len(rows[0]):
            antinodes.add(tuple([a_x, a_y]))
            a_x -= diff_x
            a_y -= diff_y
        b_x = b[0] + diff_x
        b_y = b[1] + diff_y
        while b_y >= 0 and b_y < len(rows) and b_x >= 0 and b_x < len(rows[0]):
            antinodes.add(tuple([b_x, b_y]))
            b_x += diff_x
            b_y += diff_y
print(len(antinodes))
