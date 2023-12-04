raw = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()


class Ticket:
    def __init__(self, winners: list[int], numbers: list[int], ticket_id):
        self.ticket_id = ticket_id
        self.winners = winners
        self.numbers = numbers
        self.count = 1

    def part_one(self):
        total = 0
        for number in self.numbers:
            if number in self.winners:
                if total == 0:
                    total = 1
                else:
                    total *= 2
        return total

    def part_two(self):
        winning = 0
        for number in self.numbers:
            if number in self.winners:
                winning += 1

        new = []
        for i in range(1, winning + 1):
            new.append(self.ticket_id + i)
        return new


tickets: list[Ticket] = []

for ticket in raw:
    ticket_id, values = ticket.split(": ")
    winners, numbers = values.split(" | ")
    winners = [int(w) for w in winners.split()]
    numbers = [int(n) for n in numbers.split()]
    tickets.append(Ticket(winners, numbers, int(ticket_id.strip("Card "))))

points = 0
for ticket in tickets:
    points += ticket.part_one()
print(points)

for ticket in tickets:
    new = ticket.part_two()
    for n in new:
        tickets[n - 1].count += ticket.count

total = 0
for ticket in tickets:
    total += ticket.count
print(total)
