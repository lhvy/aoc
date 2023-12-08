import numpy

lines = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()


class Route:
    def __init__(self, left, right):
        self.left = left
        self.right = right


routes: dict[str, Route] = {}

steps = lines[0]
routes_raw = lines[2:]
ghosts = []
for route in routes_raw:
    name, paths_raw = route.split(" = ")
    left, right = paths_raw.removeprefix("(").removesuffix(")").split(", ")
    routes[name] = Route(left, right)
    if name.endswith("A"):
        ghosts.append(name)


def part_one():
    current = "AAA"
    i = 0
    while current != "ZZZ":
        if steps[i % len(steps)] == "L":
            current = routes[current].left
        else:
            current = routes[current].right
        i += 1

    print(i)


def part_two():
    n_steps: list[int] = []
    for g in ghosts:
        i = 0
        while not g.endswith("Z"):
            if steps[i % len(steps)] == "L":
                g = routes[g].left
            else:
                g = routes[g].right
            i += 1
        n_steps.append(i)

    print(numpy.lcm.reduce(n_steps))


part_one()
part_two()
