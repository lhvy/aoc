from enum import Enum

raw_lines = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()


class Floor(Enum):
    EMPTY = 0
    MIRROR_SLASH = 1
    MIRROR_SLOSH = 2
    VERTICAL = 3
    HORIZONTAL = 4


class Tile:
    def __init__(self, c):
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        if c == ".":
            self.floor = Floor.EMPTY
        elif c == "|":
            self.floor = Floor.VERTICAL
        elif c == "-":
            self.floor = Floor.HORIZONTAL
        elif c == "/":
            self.floor = Floor.MIRROR_SLASH
        elif c == "\\":
            self.floor = Floor.MIRROR_SLOSH

    def check(self, direction):
        match direction:
            case Heading.LEFT:
                if self.left:
                    return True
                else:
                    self.left = True
                    return False
            case Heading.RIGHT:
                if self.right:
                    return True
                else:
                    self.right = True
                    return False
            case Heading.UP:
                if self.up:
                    return True
                else:
                    self.up = True
                    return False
            case Heading.DOWN:
                if self.down:
                    return True
                else:
                    self.down = True
                    return False

    def reset(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False


class Heading(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3


class Coordinate:
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading


tiles: list[list[Tile]] = []
for line in raw_lines:
    row = []
    for c in line:
        row.append(Tile(c))
    tiles.append(row)


def process_beams():
    while len(beams) > 0:
        b = beams.pop(0)
        match b.heading:
            case Heading.LEFT:
                if not b.x > 0 or tiles[b.y][b.x - 1].check(b.heading):
                    continue
                t = tiles[b.y][b.x - 1]
                match t.floor:
                    case Floor.EMPTY:
                        beams.append(Coordinate(b.x - 1, b.y, b.heading))
                    case Floor.VERTICAL:
                        beams.append(Coordinate(b.x - 1, b.y, Heading.UP))
                        beams.append(Coordinate(b.x - 1, b.y, Heading.DOWN))
                    case Floor.HORIZONTAL:
                        beams.append(Coordinate(b.x - 1, b.y, b.heading))
                    case Floor.MIRROR_SLASH:
                        beams.append(Coordinate(b.x - 1, b.y, Heading.DOWN))
                    case Floor.MIRROR_SLOSH:
                        beams.append(Coordinate(b.x - 1, b.y, Heading.UP))
            case Heading.RIGHT:
                if not b.x < len(tiles[b.y]) - 1 or tiles[b.y][b.x + 1].check(
                    b.heading
                ):
                    continue
                t = tiles[b.y][b.x + 1]
                match t.floor:
                    case Floor.EMPTY:
                        beams.append(Coordinate(b.x + 1, b.y, b.heading))
                    case Floor.VERTICAL:
                        beams.append(Coordinate(b.x + 1, b.y, Heading.UP))
                        beams.append(Coordinate(b.x + 1, b.y, Heading.DOWN))
                    case Floor.HORIZONTAL:
                        beams.append(Coordinate(b.x + 1, b.y, b.heading))
                    case Floor.MIRROR_SLASH:
                        beams.append(Coordinate(b.x + 1, b.y, Heading.UP))
                    case Floor.MIRROR_SLOSH:
                        beams.append(Coordinate(b.x + 1, b.y, Heading.DOWN))
            case Heading.UP:
                if not b.y > 0 or tiles[b.y - 1][b.x].check(b.heading):
                    continue
                t = tiles[b.y - 1][b.x]
                match t.floor:
                    case Floor.EMPTY:
                        beams.append(Coordinate(b.x, b.y - 1, b.heading))
                    case Floor.VERTICAL:
                        beams.append(Coordinate(b.x, b.y - 1, b.heading))
                    case Floor.HORIZONTAL:
                        beams.append(Coordinate(b.x, b.y - 1, Heading.LEFT))
                        beams.append(Coordinate(b.x, b.y - 1, Heading.RIGHT))
                    case Floor.MIRROR_SLASH:
                        beams.append(Coordinate(b.x, b.y - 1, Heading.RIGHT))
                    case Floor.MIRROR_SLOSH:
                        beams.append(Coordinate(b.x, b.y - 1, Heading.LEFT))
            case Heading.DOWN:
                if not b.y < len(tiles) - 1 or tiles[b.y + 1][b.x].check(b.heading):
                    continue
                t = tiles[b.y + 1][b.x]
                match t.floor:
                    case Floor.EMPTY:
                        beams.append(Coordinate(b.x, b.y + 1, b.heading))
                    case Floor.VERTICAL:
                        beams.append(Coordinate(b.x, b.y + 1, b.heading))
                    case Floor.HORIZONTAL:
                        beams.append(Coordinate(b.x, b.y + 1, Heading.LEFT))
                        beams.append(Coordinate(b.x, b.y + 1, Heading.RIGHT))
                    case Floor.MIRROR_SLASH:
                        beams.append(Coordinate(b.x, b.y + 1, Heading.LEFT))
                    case Floor.MIRROR_SLOSH:
                        beams.append(Coordinate(b.x, b.y + 1, Heading.RIGHT))


def sum_tiles():
    total = 0
    for row in tiles:
        for t in row:
            if t.left or t.right or t.up or t.down:
                total += 1
                t.reset()
            #     print("#", end="")
            # else:
            #     print(".", end="")
        # print("")
    return total


beams = [Coordinate(-1, 0, Heading.RIGHT)]
process_beams()
print(sum_tiles())

up = [0 for _ in range(len(tiles[0]))]
down = [0 for _ in range(len(tiles[0]))]
left = [0 for _ in range(len(tiles))]
right = [0 for _ in range(len(tiles))]

for i in range(len(tiles[0])):
    beams = [Coordinate(i, -1, Heading.DOWN)]
    process_beams()
    up[i] = sum_tiles()

    beams = [Coordinate(i, len(tiles), Heading.UP)]
    process_beams()
    down[i] = sum_tiles()

for i in range(len(tiles)):
    beams = [Coordinate(-1, i, Heading.RIGHT)]
    process_beams()
    left[i] = sum_tiles()

    beams = [Coordinate(len(tiles[0]), i, Heading.LEFT)]
    process_beams()
    right[i] = sum_tiles()

print(max([max(up), max(down), max(left), max(right)]))
