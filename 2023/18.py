raw_lines = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_points(instructions):
    points = [Coordinate(0, 0)]
    perimeter = 0
    for direction, steps in instructions:
        perimeter += steps
        prev = points[-1]
        # print(direction, steps)
        if direction == "U":
            points.append(Coordinate(prev.x, prev.y - steps))
        elif direction == "D":
            points.append(Coordinate(prev.x, prev.y + steps))
        elif direction == "L":
            points.append(Coordinate(prev.x - steps, prev.y))
        elif direction == "R":
            points.append(Coordinate(prev.x + steps, prev.y))
    return points, perimeter


def count_space(points: list[Coordinate], perimeter: int):
    # Shoelace Formula
    area = 0
    # Need starting point at the end for shoelace
    points.append(points[0])
    for i in range(len(points) - 1):
        area += points[i].x * points[i + 1].y
        area -= points[i].y * points[i + 1].x
    area /= 2
    # Remove bonus point from shoelace
    points.pop()

    # Pick's Theorem
    return area + 1 + perimeter / 2


# Part 1
instructions = []
for instruction in raw_lines:
    d, s, _ = instruction.split()
    instructions.append(tuple([d, int(s)]))
pts, per = get_points(instructions)
print(count_space(pts, per))

# Part 2
instructions = []
for instruction in raw_lines:
    _, _, color = instruction.split()
    color = color[2:-1]
    s = int(color[0:5], 16)
    if color[-1] == "0":
        d = "R"
    elif color[-1] == "1":
        d = "D"
    elif color[-1] == "2":
        d = "L"
    elif color[-1] == "3":
        d = "U"
    instructions.append(tuple([d, int(s)]))
pts, per = get_points(instructions)
print(count_space(pts, per))
