import util
from intervaltree import IntervalTree

lines = util.get_input_lines()

part_a = 0
part_b = 0

t = IntervalTree()

i = 0
min_id = 0
max_id = 0
while i < len(lines):
    if lines[i] == "":
        i += 1
        break

    start, end = lines[i].split("-")
    start = int(start)
    end = int(end) + 1

    min_id = min(min_id, start)
    max_id = max(max_id, end)

    t[start:end] = True

    i += 1

t.merge_overlaps()

while i < len(lines):
    c = int(lines[i])

    if t[c]:
        part_a += 1

    i += 1

for interval in t.items():
    part_b += interval[1] - interval[0]

print("Part A: ", part_a)
print("Part B: ", part_b)
