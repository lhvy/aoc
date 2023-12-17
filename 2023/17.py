from enum import Enum
import bisect

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

    def __lt__(self, other):
        if self.e < other.e:
            return True
        elif self.e > other.e:
            return False
        else:
            return self.n < other.n


class Tile:
    def __init__(self):
        self.up = [float("inf") for _ in range(10)]
        self.down = [float("inf") for _ in range(10)]
        self.left = [float("inf") for _ in range(10)]
        self.right = [float("inf") for _ in range(10)]
        self.x = -1
        self.y = -1

    def cheaper(self, d, n, e, x=-1, y=-1):
        if d == Direction.UP:
            for i in range(n):
                if self.up[i] <= e:
                    return False
            for i in range(n - 1, 10):
                self.up[i] = e
        elif d == Direction.DOWN:
            for i in range(n):
                if self.down[i] <= e:
                    return False
            for i in range(n - 1, 10):
                self.down[i] = e
        elif d == Direction.LEFT:
            for i in range(n):
                if self.left[i] <= e:
                    return False
            for i in range(n - 1, 10):
                self.left[i] = e
        elif d == Direction.RIGHT:
            for i in range(n):
                if self.right[i] <= e:
                    return False
            for i in range(n - 1, 10):
                self.right[i] = e
        self.x = x
        self.y = y
        return True


# Part 1
queue = [Path(0, 0, None, 0, 0)]
exhaustion = [[Tile() for _ in range(len(grid[i]))] for i in range(len(grid))]
exhaustion[0][0].up = [0 for _ in range(10)]
exhaustion[0][0].down = [0 for _ in range(10)]
exhaustion[0][0].left = [0 for _ in range(10)]
exhaustion[0][0].right = [0 for _ in range(10)]
while len(queue) > 0:
    p = queue.pop(0)
    if p.y == len(grid) - 1 and p.x == len(grid[0]) - 1:
        break
    if p.y > 0 and (p.d != Direction.UP or p.n < 3) and p.d != Direction.DOWN:
        if p.d == Direction.UP:
            n = p.n + 1
        else:
            n = 1
        e = p.e + grid[p.y - 1][p.x]
        if exhaustion[p.y - 1][p.x].cheaper(Direction.UP, n, e):
            bisect.insort(queue, Path(p.x, p.y - 1, Direction.UP, n, e))
    if p.x > 0 and (p.d != Direction.LEFT or p.n < 3) and p.d != Direction.RIGHT:
        if p.d == Direction.LEFT:
            n = p.n + 1
        else:
            n = 1
        e = p.e + grid[p.y][p.x - 1]
        if exhaustion[p.y][p.x - 1].cheaper(Direction.LEFT, n, e):
            bisect.insort(queue, Path(p.x - 1, p.y, Direction.LEFT, n, e))
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
            bisect.insort(queue, Path(p.x, p.y + 1, Direction.DOWN, n, e))
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
            bisect.insort(queue, Path(p.x + 1, p.y, Direction.RIGHT, n, e))

print(
    min(
        [
            min(exhaustion[-1][-1].down),
            min(exhaustion[-1][-1].right),
        ]
    )
)

# Part 2
queue = [Path(0, 0, None, 11, 0)]
exhaustion = [[Tile() for _ in range(len(grid[i]))] for i in range(len(grid))]
exhaustion[0][0].up = [0 for _ in range(10)]
exhaustion[0][0].down = [0 for _ in range(10)]
exhaustion[0][0].left = [0 for _ in range(10)]
exhaustion[0][0].right = [0 for _ in range(10)]
while len(queue) > 0:
    p = queue.pop(0)
    # print(p.x, p.y, p.n)
    if p.y == len(grid) - 1 and p.x == len(grid[0]) - 1:
        break
    if (
        p.y > 0
        and (
            # Not previously up, have gone 4+ in prev dir and minimum 4 room left to go up
            (p.d != Direction.UP and p.n >= 4 and p.y >= 4)
            # Previously up for less than 10
            or (p.d == Direction.UP and p.n < 10)
        )
        and p.d != Direction.DOWN
    ):
        # Calculate new number of previous steps up
        if p.d == Direction.UP:
            n = p.n + 1
        else:
            n = 1
        # Calculate new exhaustion
        e = p.e + grid[p.y - 1][p.x]
        # If cheaper, push to sorted queue (new exhaustion value is stored)
        if exhaustion[p.y - 1][p.x].cheaper(Direction.UP, n, e, p.x, p.y):
            bisect.insort(queue, Path(p.x, p.y - 1, Direction.UP, n, e))
    if (
        p.x > 0
        and (
            # Not previously left, have gone 4+ in prev dir, and min 4 space to go left
            (p.d != Direction.LEFT and p.n >= 4 and p.x >= 4)
            # Previously left for less than 10
            or (p.d == Direction.LEFT and p.n < 10)
        )
        and p.d != Direction.RIGHT
    ):
        if p.d == Direction.LEFT:
            n = p.n + 1
        else:
            n = 1
        e = p.e + grid[p.y][p.x - 1]
        if exhaustion[p.y][p.x - 1].cheaper(Direction.LEFT, n, e, p.x, p.y):
            bisect.insort(queue, Path(p.x - 1, p.y, Direction.LEFT, n, e))
    if (
        p.y < len(grid) - 1
        and (
            # Not previously down, have gone 4+ in prev dir, and min 4 spaces to go down
            (p.d != Direction.DOWN and p.n >= 4 and len(grid) - 1 - p.y >= 4)
            # Previously down less than 10 and (end Y can be reached before 10 turns
            # or at least 5 moves left to reach Y, guaranteeing can be reached even if we turn away next)
            or (
                p.d == Direction.DOWN
                and p.n < 10
                and (len(grid) - 1 - p.y <= 10 - p.n or len(grid) - 1 - p.y >= 5)
            )
        )
        and p.d != Direction.UP
    ):
        if p.d == Direction.DOWN:
            n = p.n + 1
        else:
            n = 1
        e = p.e + grid[p.y + 1][p.x]
        if exhaustion[p.y + 1][p.x].cheaper(Direction.DOWN, n, e, p.x, p.y):
            bisect.insort(queue, Path(p.x, p.y + 1, Direction.DOWN, n, e))
    if (
        p.x < len(grid[p.y]) - 1
        and (
            # Not previously right, have gone 4+ in prev dir, and min 4 spaces to go right
            (p.d != Direction.RIGHT and p.n >= 4 and len(grid[p.y]) - 1 - p.x >= 4)
            # Previously right less than 10 and (end X can be reached before 10 turns
            # or at least 5 moves left to reach X, guaranteeing can be reached even if we turn away next)
            or (
                p.d == Direction.RIGHT
                and p.n < 10
                and (
                    len(grid[p.y]) - 1 - p.x <= 10 - p.n
                    or len(grid[p.y]) - 1 - p.x >= 5
                )
            )
        )
        and p.d != Direction.LEFT
    ):
        if p.d == Direction.RIGHT:
            n = p.n + 1
        else:
            n = 1
        e = p.e + grid[p.y][p.x + 1]
        if exhaustion[p.y][p.x + 1].cheaper(Direction.RIGHT, n, e, p.x, p.y):
            bisect.insort(queue, Path(p.x + 1, p.y, Direction.RIGHT, n, e))

print(
    min(
        [
            min(exhaustion[-1][-1].down),
            min(exhaustion[-1][-1].right),
        ]
    )
)

# current = exhaustion[-1][-1]
# while current.x != -1 and current.y != -1:
#     print(current.x, current.y)
#     input()
#     grid[current.y][current.x] = "#"
#     current = exhaustion[current.y][current.x]
