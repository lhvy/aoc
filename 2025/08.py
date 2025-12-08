from functools import reduce
from math import sqrt
from operator import mul

import util


# GeeksForGeeks Union Find
class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))

    def find(self, idx: int) -> int:
        if self.parent[idx] == idx:
            return idx

        return self.find(self.parent[idx])

    # Modified to return bool for if groups were merged
    def unite(self, a: int, b: int) -> bool:
        a_rep = self.find(a)
        b_rep = self.find(b)

        if a_rep == b_rep:
            return False

        self.parent[a_rep] = b_rep
        return True


lines = util.get_input_lines()

part_a = 0

# x, y, z
coords: list[tuple[int, int, int]] = []

# d, i, j
dist: list[tuple[float, int, int]] = []

for i, l in enumerate(lines):
    x, y, z = [int(n) for n in l.split(",")]
    coords.append((x, y, z))

for i, (xi, yi, zi) in enumerate(coords):
    for j, (xj, yj, zj) in enumerate(coords):
        if j <= i:
            continue
        dist.append((sqrt((xi - xj) ** 2 + (yi - yj) ** 2 + (zi - zj) ** 2), i, j))

dist.sort()
u = UnionFind(len(coords))

# Part A: Run first 1k
for d, i, j in dist[:1000]:
    # print(coords[i], coords[j])
    u.unite(i, j)

count: dict[int, int] = {}
for i in range(len(coords)):
    n = u.find(i)
    if n not in count:
        count[n] = 1
    else:
        count[n] += 1

v = list(count.values())
v.sort(reverse=True)
# print(v)

part_a = reduce(mul, v[:3])
print("Part A: ", part_a)

last = (-1, -1)

# Part B: Run until no more merges and print last merge
# Cheap way is to just attempt all merges and track if merge actually happened or not
for d, i, j in dist[1000:]:
    # print(coords[i], coords[j])
    needed = u.unite(i, j)
    if needed:
        last = (i, j)

part_b = coords[last[0]][0] * coords[last[1]][0]
print("Part B: ", part_b)
