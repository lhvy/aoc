import re
import copy

raw_workflows, raw_parts = (
    open("input.txt", "r", encoding="utf-8").read().strip().split("\n\n")
)


class Part:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def rating(self):
        return self.x + self.m + self.a + self.s


class Condition:
    def __init__(self, category, value, lt):
        self.category = category
        self.value = value
        self.lt = lt

    def eval(self, part: Part):
        match self.category:
            case "x":
                cmp = part.x
            case "m":
                cmp = part.m
            case "a":
                cmp = part.a
            case "s":
                cmp = part.s

        if self.lt:
            return cmp < self.value
        else:
            return cmp > self.value


workflows: dict[str, list[tuple[Condition, str]]] = {}
for workflow in raw_workflows.splitlines():
    name, raw_steps = workflow.split("{")
    raw_steps = raw_steps[:-1]
    steps = []
    for step in raw_steps.split(","):
        if ":" not in step:
            steps.append((None, step))
            continue
        step, dest = step.split(":")
        c = step[0]
        if step[1] == "<":
            lt = True
        elif step[1] == ">":
            lt = False
        value = int(step[2:])
        steps.append((Condition(c, value, lt), dest))
    workflows[name] = steps

parts = []
for part in raw_parts.splitlines():
    x, m, a, s = re.findall("\d+", part)
    parts.append(Part(int(x), int(m), int(a), int(s)))


def process_part(part):
    w = workflows["in"]
    i = 0
    while i < len(w):
        s = w[i]
        if s[0] == None:
            if s[1] in ["A", "R"]:
                break
            w = workflows[s[1]]
            i = 0
        elif s[0].eval(part):
            if s[1] in ["A", "R"]:
                break
            w = workflows[s[1]]
            i = 0
        else:
            i += 1

    if s[1] == "A":
        return part.rating()
    elif s[1] != "R":
        print("Shouldn't be here...", part.x)
    return 0


part_one = 0
for part in parts:
    part_one += process_part(part)
print(part_one)

x = [False for _ in range(4000)]
m = [False for _ in range(4000)]
a = [False for _ in range(4000)]
s = [False for _ in range(4000)]


def flag_possible(low, high):
    print(low, high)
    for i in range(low[0], high[0] + 1):
        x[i - 1] = True
    for i in range(low[1], high[1] + 1):
        m[i - 1] = True
    for i in range(low[2], high[2] + 1):
        a[i - 1] = True
    for i in range(low[3], high[3] + 1):
        s[i - 1] = True


def combine_ranges(a: list[int], b: list[int]):
    low = []
    high = []
    for i, (aa, bb) in enumerate(zip(a, b)):
        low[i] = high(aa, bb)
        high[i] = low(aa, bb)
    return low, high


def count_possibilities(name, low=[1, 1, 1, 1], high=[4000, 4000, 4000, 4000]):
    # print(name, low, high)
    if name == "R":
        return 0
    elif name == "A":
        return (
            (high[0] - low[0] + 1)
            * (high[1] - low[1] + 1)
            * (high[2] - low[2] + 1)
            * (high[3] - low[3] + 1)
        )

    total = 0
    workflow = workflows[name]
    for step in workflow:
        condition = step[0]
        dest = step[1]
        if condition == None:
            # We have reached the end of the workflow
            return total + count_possibilities(dest, low, high)
        # Convert from xmas letter to index in low/high
        match step[0].category:
            case "x":
                i = 0
            case "m":
                i = 1
            case "a":
                i = 2
            case "s":
                i = 3

        if step[0].lt:
            new_high = high.copy()
            new_high[i] = min(step[0].value - 1, high[i])
            total += count_possibilities(dest, low.copy(), new_high)
            low[i] = max(low[i], step[0].value)
        else:
            new_low = low.copy()
            new_low[i] = max(step[0].value + 1, low[i])
            total += count_possibilities(dest, new_low, high.copy())
            high[i] = min(high[i], step[0].value)

    print("We shouldn't be here...")


print(count_possibilities("in"))
