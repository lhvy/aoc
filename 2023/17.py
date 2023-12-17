from enum import Enum
import functools

raw_lines = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()
grid = [[int(c) for c in line] for line in raw_lines]


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Path:
    def __init__(self, x: int, y: int, d: Direction, n: int, e: int):
        self.x = x
        self.y = y
        self.d = d
        self.n = n
        self.e = e


class Tile:
    def __init__(self):
        self.up = [float("inf"), float("inf"), float("inf")]
        self.down = [float("inf"), float("inf"), float("inf")]
        self.left = [float("inf"), float("inf"), float("inf")]
        self.right = [float("inf"), float("inf"), float("inf")]

    @functools.lru_cache(maxsize=None)
    def cheaper(self, d, n, e):
        if d == Direction.UP:
            for i in range(n):
                if self.up[i] <= e:
                    return False
            for i in range(n - 1, 3):
                self.up[i] = e
        elif d == Direction.DOWN:
            for i in range(n):
                if self.down[i] <= e:
                    return False
            for i in range(n - 1, 3):
                self.down[i] = e
        elif d == Direction.LEFT:
            for i in range(n):
                if self.left[i] <= e:
                    return False
            for i in range(n - 1, 3):
                self.left[i] = e
        elif d == Direction.RIGHT:
            for i in range(n):
                if self.right[i] <= e:
                    return False
            for i in range(n - 1, 3):
                self.right[i] = e
        return True


queue = [Path(0, 0, None, 0, 0)]
exhaustion = [[Tile() for _ in range(len(grid[i]))] for i in range(len(grid))]
exhaustion[0][0].up = [0, 0, 0]
exhaustion[0][0].down = [0, 0, 0]
exhaustion[0][0].left = [0, 0, 0]
exhaustion[0][0].right = [0, 0, 0]
while len(queue) > 0:
    p = queue.pop()
    if p.y > 0 and (p.d != Direction.UP or p.n < 3) and p.d != Direction.DOWN:
        if p.d == Direction.UP:
            n = p.n + 1
        else:
            n = 1
        e = p.e + grid[p.y - 1][p.x]
        if exhaustion[p.y - 1][p.x].cheaper(Direction.UP, n, e):
            queue.append(Path(p.x, p.y - 1, Direction.UP, n, e))
    if p.x > 0 and (p.d != Direction.LEFT or p.n < 3) and p.d != Direction.RIGHT:
        if p.d == Direction.LEFT:
            n = p.n + 1
        else:
            n = 1
        e = p.e + grid[p.y][p.x - 1]
        if exhaustion[p.y][p.x - 1].cheaper(Direction.LEFT, n, e):
            queue.append(Path(p.x - 1, p.y, Direction.LEFT, n, e))
    if (
        p.y < len(grid) - 1
        and (p.d != Direction.DOWN or p.n < 3)
        and p.d != Direction.UP
    ):
        if p.d == Direction.DOWN:
            n = p.n + 1
        else:
            n = 1
        e = p.e + grid[p.y + 1][p.x]
        if exhaustion[p.y + 1][p.x].cheaper(Direction.DOWN, n, e):
            queue.append(Path(p.x, p.y + 1, Direction.DOWN, n, e))
    if (
        p.x < len(grid[p.y]) - 1
        and (p.d != Direction.RIGHT or p.n < 3)
        and p.d != Direction.LEFT
    ):
        if p.d == Direction.RIGHT:
            n = p.n + 1
        else:
            n = 1
        e = p.e + grid[p.y][p.x + 1]
        if exhaustion[p.y][p.x + 1].cheaper(Direction.RIGHT, n, e):
            queue.append(Path(p.x + 1, p.y, Direction.RIGHT, n, e))

print(min(exhaustion[-1][-1].up))
print(min(exhaustion[-1][-1].down))
print(min(exhaustion[-1][-1].left))
print(min(exhaustion[-1][-1].right))
