import util
import re
from PIL import Image
import numpy as np


lines = util.get_input_lines()

WIDTH = 101
HEIGHT = 103
SECONDS = 100


def do_moves(seconds, grid):
    for line in lines:
        x, y, vx, vy = map(int, re.findall(r"-?\d+", line))
        x = (x + seconds * vx) % WIDTH
        y = (y + seconds * vy) % HEIGHT
        grid[y][x] += 1


grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
do_moves(SECONDS, grid)

quadrants = [0, 0, 0, 0]
for y, row in enumerate(grid):
    for x, n in enumerate(row):
        if x > WIDTH // 2 and y < HEIGHT // 2:
            quadrants[0] += n
        elif x < WIDTH // 2 and y < HEIGHT // 2:
            quadrants[1] += n
        elif x < WIDTH // 2 and y > HEIGHT // 2:
            quadrants[2] += n
        elif x > WIDTH // 2 and y > HEIGHT // 2:
            quadrants[3] += n

part_one = 1
for q in quadrants:
    # print(q)
    part_one *= q
print(part_one)


def grind_to_image(grid, n):
    pixels = np.array(grid)
    pixels = np.where(pixels > 0, 255, 0).astype(np.uint8)
    image = Image.fromarray(pixels, mode="L")
    image.save(f"day14/second_{n}.png")


for i in range(1, 10000):
    grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    do_moves(i, grid)
    # for row in grid:
    # print("".join(["#" if n > 0 else " " for n in row]))
    grind_to_image(grid, i)
