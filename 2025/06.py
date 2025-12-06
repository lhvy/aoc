import sys
from functools import reduce
from itertools import zip_longest
from operator import add, mul

import util

lines = util.get_input_lines()

part_a = 0
part_b = 0

tasks: list[list[int]] = [[] for _ in range(len(lines[0].split()))]

for l in lines[:-1]:
    ns = [int(x) for x in l.split()]
    for i, n in enumerate(ns):
        tasks[i].append(n)

for i, op in enumerate(lines[-1].split()):
    # print(tasks[i], op)
    if op == "+":
        part_a += reduce(add, tasks[i])
    elif op == "*":
        part_a += reduce(mul, tasks[i])
    else:
        print(i, op)
        sys.exit(1)

print("Part A: ", part_a)


rotated = list(zip_longest(*lines, fillvalue=" "))[::-1]
cur: list[int] = []
for row in rotated:
    n_str = "".join(row)
    if n_str.endswith(("+", "*")):
        cur.append(int(n_str[:-1]))
        if n_str[-1] == "+":
            part_b += reduce(add, cur)
        elif n_str[-1] == "*":
            part_b += reduce(mul, cur)
        cur = []
    elif n_str.strip() == "":
        continue
    else:
        cur.append(int(n_str))


print("Part B: ", part_b)
