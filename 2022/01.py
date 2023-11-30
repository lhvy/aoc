from dataclasses import dataclass


@dataclass
class elf:
    def __init__(self, calories: list[int]):
        self.calories = calories
        self.total = sum(calories)

    def __lt__(self, obj):
        return self.total < obj.total

    def __gt__(self, obj):
        return self.total > obj.total

    def __le__(self, obj):
        return self.total <= obj.total

    def __ge__(self, obj):
        return self.total >= obj.total

    def __eq__(self, obj):
        return self.total == obj.total


def main():
    elves = []
    raw = open("input.txt", "r", encoding="utf-8").read().strip().split("\n\n")
    for e in raw:
        calories = [int(c) for c in e.split()]
        elves.append(elf(calories))

    # Part 1
    print(max(elves).total)

    # Part 2
    elves.sort()
    print(elves[-1].total + elves[-2].total + elves[-3].total)


main()
