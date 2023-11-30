from enum import Enum


class Choice(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

    def points(self):
        if self.name == "ROCK":
            return 1
        elif self.name == "PAPER":
            return 2
        else:
            return 3

    def win(self):
        if self.name == "ROCK":
            return Choice.PAPER
        elif self.name == "PAPER":
            return Choice.SCISSORS
        else:
            return Choice.ROCK

    def tie(self):
        return self

    def lose(self):
        return self.win().win()


def run(them: Choice, us: Choice):
    if (
        us.name == "PAPER"
        and them.name == "ROCK"
        or us.name == "ROCK"
        and them.name == "SCISSORS"
        or us.name == "SCISSORS"
        and them.name == "PAPER"
    ):
        return 6
    elif us == them:
        return 3
    else:
        return 0


rounds = open("input.txt", "r", encoding="utf-8").read().strip().split("\n")


def part_one():
    total = 0

    for r in rounds:
        them = Choice(r.split()[0])
        us = Choice(r.split()[1].replace("X", "A").replace("Y", "B").replace("Z", "C"))
        total += us.points()
        total += run(them, us)

    print(total)


def part_two():
    total = 0

    for r in rounds:
        them = Choice(r.split()[0])
        move = r.split()[1]
        if move == "X":
            us = them.lose()
        elif move == "Y":
            us = them.tie()
        elif move == "Z":
            us = them.win()
        total += us.points()
        total += run(them, us)

    print(total)


part_one()
part_two()
