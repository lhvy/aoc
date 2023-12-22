import functools

raw_lines = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.x == other.x and self.y == other.y


tiles = set()
for y, line in enumerate(raw_lines):
    if "S" in line:
        tiles.add(Coordinate(line.index("S"), y))

for i in range():
    prev = tiles
    tiles = set()
    for c in prev:
        if raw_lines[(c.y - 1) % len(raw_lines)][c.x % len(raw_lines[0])] != "#":
            tiles.add(Coordinate(c.x, c.y - 1))
        if raw_lines[c.y % len(raw_lines)][(c.x - 1) % len(raw_lines[0])] != "#":
            tiles.add(Coordinate(c.x - 1, c.y))
        if raw_lines[(c.y + 1) % len(raw_lines)][c.x % len(raw_lines[0])] != "#":
            tiles.add(Coordinate(c.x, c.y + 1))
        if raw_lines[c.y % len(raw_lines)][(c.x + 1) % len(raw_lines[0])] != "#":
            tiles.add(Coordinate(c.x + 1, c.y))
    print(i / 5000)
print(len(tiles))


@functools.lru_cache(maxsize=None)
def count_tiles(c: Coordinate, steps: int):
    tiles = set()
    if steps == 0:
        tiles.add(c)
        return tiles
    if raw_lines[(c.y - 1) % len(raw_lines)][c.x % len(raw_lines[0])] != "#":
        tiles.update(count_tiles(Coordinate(c.x, c.y - 1), steps - 1))
    if raw_lines[c.y % len(raw_lines)][(c.x - 1) % len(raw_lines[0])] != "#":
        tiles.update(count_tiles(Coordinate(c.x - 1, c.y), steps - 1))
    if raw_lines[(c.y + 1) % len(raw_lines)][c.x % len(raw_lines[0])] != "#":
        tiles.update(count_tiles(Coordinate(c.x, c.y + 1), steps - 1))
    if raw_lines[c.y % len(raw_lines)][(c.x + 1) % len(raw_lines[0])] != "#":
        tiles.update(count_tiles(Coordinate(c.x + 1, c.y), steps - 1))
    return tiles


# for y, line in enumerate(raw_lines):
#     if "S" in line:
#         print(len(count_tiles(Coordinate(line.index("S"), y), 500)))
