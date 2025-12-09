import util
from shapely import Polygon

lines = util.get_input_lines()

part_a = 0

coords: list[tuple[int, int]] = []
for l in lines:
    x, y = [int(n) for n in l.split(",")]
    coords.append((x, y))

rects: list[tuple[tuple[int, int], tuple[int, int]]] = []

for i, (x_i, y_i) in enumerate(coords):
    for j, (x_j, y_j) in enumerate(coords):
        if i >= j:
            continue

        rects.append(((x_i, y_i), (x_j, y_j)))

rects.sort(
    reverse=True,
    key=lambda r: (abs(r[0][0] - r[1][0]) + 1) * (abs(r[0][1] - r[1][1]) + 1),
)

part_a = (abs(rects[0][0][0] - rects[0][1][0]) + 1) * (
    abs(rects[0][0][1] - rects[0][1][1]) + 1
)

print("Part A: ", part_a)

part_b = 0

polygon = Polygon(coords)
for (x_i, y_i), (x_j, y_j) in rects:
    x_l = min(x_i, x_j)
    x_r = max(x_i, x_j)
    y_t = min(y_i, y_j)
    y_b = max(y_i, y_j)

    box = Polygon([(x_l, y_t), (x_r, y_t), (x_r, y_b), (x_l, y_b)])

    if not polygon.contains(box):
        continue

    width = abs(x_i - x_j) + 1
    height = abs(y_i - y_j) + 1
    part_b = width * height
    break

print("Part B: ", part_b)
