import util

lines = util.get_input_lines()

presents: list[int] = []
c = 0
i = 0
for l in lines:
    i += 1
    if l == "" or (l[0] != "." and l[0] != "#"):
        if c != 0:
            presents.append(c)
        c = 0
        if len(presents) == 6:
            break
        continue

    c += sum(int(x == "#") for x in l)

part_a = 0

# This is so cooked, why do I not need to consider packing?
for l in lines[i:]:
    dim, ns = l.split(": ")
    width, height = [int(x) for x in dim.split("x")]
    ns = [int(x) for x in ns.split()]

    if sum(x * presents[i] for i, x in enumerate(ns)) < width * height:
        part_a += 1

print("Part A: ", part_a)
