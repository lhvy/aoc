from collections import deque
from functools import lru_cache

import util

lines = util.get_input_lines()
lines = [list(l) for l in lines]

sx = None
sy = 0
for cx, c in enumerate(lines[0]):
    if c == "S":
        sx = cx
assert sx is not None

part_a = 0

queue: deque[tuple[int, int]] = deque()
queue.append((sx, sy))

seen: set[tuple[int, int]] = set()

while len(queue) > 0:
    cx, cy = queue.popleft()
    if (cx, cy) in seen:
        continue
    seen.add((cx, cy))

    if lines[cy][cx] == "^":
        # print(cx, cy)
        if cx > 0:
            queue.append((cx - 1, cy))
        if cx + 1 < len(lines[cy]):
            queue.append((cx + 1, cy))
        part_a += 1
    elif cy + 1 < len(lines):
        queue.append((cx, cy + 1))

print("Part A: ", part_a)


@lru_cache(maxsize=None)
def part_b(x: int, y: int) -> int:
    if y + 1 >= len(lines):
        return 1

    if lines[y + 1][x] == ".":
        return part_b(x, y + 1)

    if lines[y + 1][x] == "^":
        n = 0
        if x > 0:
            n += part_b(x - 1, y + 1)
        if x + 1 < len(lines[y + 1]):
            n += part_b(x + 1, y + 1)
        return n

    assert False


print("Part B: ", part_b(sx, sy))
