raw_lines = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()


def my_hash(string):
    h = 0
    for c in string:
        h += ord(c)
        h *= 17
        h %= 256
    return h


def part_one():
    total = 0
    for line in raw_lines:
        for step in line.split(","):
            h = my_hash(step)
            total += h
    return total


class Box:
    def __init__(self):
        self.slots: list[str] = []
        self.lenses: dict[str, int] = {}

    def add(self, label, length):
        if label not in self.slots:
            self.slots.append(label)
        self.lenses[label] = length

    def remove(self, label):
        if label in self.slots:
            self.slots.remove(label)
            self.lenses.pop(label)

    def power(self):
        p = 0
        for i, lens in enumerate(self.slots):
            p += (i + 1) * self.lenses[lens]
        return p

    def len(self):
        return len(self.slots)


def part_two():
    boxes = [Box() for _ in range(0, 256)]
    for line in raw_lines:
        for step in line.split(","):
            if step.endswith("-"):
                h = my_hash(step[:-1])
                boxes[h].remove(step[:-1])
            else:
                label, length = step.split("=")
                h = my_hash(label)
                boxes[h].add(label, int(length))

    total = 0
    for i, box in enumerate(boxes):
        if box.len() > 0:
            total += (i + 1) * box.power()
    return total


print(part_one())
print(part_two())
