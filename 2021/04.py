from util import *

input = get_input_double_newline()


class Game:
    def __init__(self, calls, boards):
        self.calls = calls
        self.boards = boards

    def play(self):
        for call in self.calls:
            for b in range(len(self.boards)):
                for row in self.boards[b].rows:
                    for col in row:
                        if col.number == call:
                            col.is_called = True
                for row in self.boards[b].rows:
                    horiz = True
                    for col in row:
                        if not col.is_called:
                            horiz = False
                            continue
                    if horiz:
                        s = 0
                        for r in self.boards[b].rows:
                            for c in r:
                                if not c.is_called:
                                    s += c.number
                        print(b)
                        for c in row:
                            print(c.number, end=" ")
                        print("")
                        print(s, call)
                        return s * call
                for i in range(5):
                    vert = True
                    for row in self.boards[b].rows:
                        if not row[i].is_called:
                            vert = False
                    if vert:
                        s = 0
                        for r in self.boards[b].rows:
                            for c in r:
                                s += c.number
                        print(b)
                        for c in row:
                            print(c.number, end=" ")
                        print("")
                        print(s, call)
                        return s * call


class Board:
    def __init__(self, input):
        self.rows = []
        for line in input.split("\n"):
            line = line.strip().replace("  ", " ")
            row = []
            for i in line.split(" "):
                row.append(Number(int(i)))
            self.rows.append(row)


class Number:
    def __init__(self, number):
        self.number = number
        self.is_called = False


boards = []
for board in input[1:]:
    boards.append(Board(board))

calls = []
for c in input[0].split(","):
    calls.append(int(c))

game = Game(calls, boards)

# for board in game.boards:
#     for row in board.rows:
#         for col in row:
#             print(col.number, end=" ")
#         print("\n")

print(game.play())
