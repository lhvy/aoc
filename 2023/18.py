raw_lines = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_plan(instructions):
    # plan = [["#"]]
    digger = Coordinate(0, 0)
    for direction, steps in instructions:
        print(direction, steps)
        if direction == "U":
            for _ in range(0, steps - digger.y):
                plan.insert(0, ["." for _ in range(len(plan[0]))])
                digger.y += 1
            for _ in range(steps):
                digger.y -= 1
                plan[digger.y][digger.x] = "#"
        elif direction == "D":
            # print(direction, steps, color)
            # print(digger.x, len(plan[0]), len(plan[digger.y]))
            for _ in range(0, digger.y + steps - (len(plan) - 1)):
                plan.append(["." for _ in range(len(plan[0]))])
            for _ in range(steps):
                digger.y += 1
                # print(digger.x, len(plan[0]), len(plan[digger.y]))
                plan[digger.y][digger.x] = "#"
        elif direction == "L":
            if steps - digger.x > 0:
                for i, line in enumerate(plan):
                    plan[i] = ["." for _ in range(0, steps - digger.x)] + line
                digger.x += steps - digger.x
            for _ in range(steps):
                digger.x -= 1
                plan[digger.y][digger.x] = "#"
        elif direction == "R":
            missing = digger.x + steps - (len(plan[digger.y]) - 1)
            if missing > 0:
                for i, line in enumerate(plan):
                    plan[i] = line + ["." for _ in range(0, missing)]
            for _ in range(steps):
                digger.x += 1
                plan[digger.y][digger.x] = "#"


def count_space():
    queue = []
    for i in range(len(plan[0])):
        queue.append(Coordinate(i, 0))
        queue.append(Coordinate(i, len(plan) - 1))
    for i in range(len(plan)):
        queue.append(Coordinate(0, i))
        queue.append(Coordinate(len(plan[i]) - 1, i))

    while len(queue) > 0:
        c = queue.pop(0)
        if plan[c.y][c.x] != ".":
            continue
        plan[c.y][c.x] = "%"
        if c.y > 0:
            queue.append(Coordinate(c.x, c.y - 1))
        if c.y < len(plan) - 1:
            queue.append(Coordinate(c.x, c.y + 1))
        if c.x > 0:
            queue.append(Coordinate(c.x - 1, c.y))
        if c.x < len(plan[c.y]) - 1:
            queue.append(Coordinate(c.x + 1, c.y))

    total = len(plan) * len(plan[0])
    for line in plan:
        total -= line.count("%")
        # print("".join(line))
    return total


instructions = []
for instruction in raw_lines:
    d, s, _ = instruction.split()
    instructions.append(tuple([d, int(s)]))
plan = [["#"]]
make_plan(instructions)
print(count_space())

# Note: This is too slow :(
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
plan = [["#"]]
make_plan(instructions)
print(count_space())
