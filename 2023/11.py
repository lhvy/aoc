raw_lines = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()

rows = []
cols = list(range(0, len(raw_lines[0])))
for i, line in enumerate(raw_lines):
    if "#" not in line:
        rows.append(i)
    else:
        indices = [i for i, x in enumerate(line) if x == "#"]
        for index in indices:
            try:
                cols.remove(index)
            except:
                "do nothing"

# added = 0
# for row in rows:
#     raw_lines.insert(row + added, raw_lines[row + added])
#     added += 1

# added = 0
# for col in cols:
#     for i, line in enumerate(raw_lines):
#         raw_lines[i] = line[0 : (col + added)] + "." + line[(col + added) :]
#     added += 1


class Galaxy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other, gap=1):
        dist = 0

        low, high = sorted([other.x, self.x])
        for x in range(low, high):
            if x in cols:
                dist += gap
            else:
                dist += 1

        low, high = sorted([other.y, self.y])
        for y in range(low, high):
            if y in rows:
                dist += gap
            else:
                dist += 1

        return dist


galaxies: list[Galaxy] = []
for y, line in enumerate(raw_lines):
    indices = [i for i, x in enumerate(line) if x == "#"]
    for x in indices:
        galaxies.append(Galaxy(x, y))

part_one = 0
part_two = 0
for i, a in enumerate(galaxies):
    for b in galaxies[(i + 1) :]:
        part_one += a.distance(b, 2)
        part_two += a.distance(b, 1000000)
print(part_one)
print(part_two)
