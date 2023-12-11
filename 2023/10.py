raw_lines = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()
lines = [[c for c in l] for l in raw_lines]

for i, line in enumerate(lines):
    if "S" in line:
        start = {"x": line.index("S"), "y": i}

visited = [[False for _ in range(0, len(lines[0]))] for _ in range(0, len(lines))]
left = start["x"] > 0 and lines[start["y"]][start["x"] - 1] in ["-", "L", "F"]
right = start["x"] < len(lines[0]) and lines[start["y"]][start["x"] + 1] in [
    "-",
    "J",
    "7",
]
up = start["y"] > 0 and lines[start["y"] - 1][start["x"]] in ["|", "7", "F"]
down = start["y"] < len(lines) and lines[start["y"] + 1][start["x"]] in ["|", "L", "J"]

if up:
    if down:
        lines[start["y"]][start["x"]] = "|"
    elif left:
        lines[start["y"]][start["x"]] = "J"
    elif right:
        lines[start["y"]][start["x"]] = "L"
elif down:
    if left:
        lines[start["y"]][start["x"]] = "7"
    elif right:
        lines[start["y"]][start["x"]] = "F"
else:  # must be left + right
    lines[start["y"]][start["x"]] = "-"


def tile(coord):
    return lines[coord["y"]][coord["x"]]


steps = 0
current = start.copy()
done = False
while not done:
    visited[current["y"]][current["x"]] = True
    t = tile(current)
    if t == "|":
        if not visited[current["y"] + 1][current["x"]]:
            current["y"] += 1
        elif not visited[current["y"] - 1][current["x"]]:
            current["y"] -= 1
        else:
            done = True
    elif t == "-":
        if not visited[current["y"]][current["x"] + 1]:
            current["x"] += 1
        elif not visited[current["y"]][current["x"] - 1]:
            current["x"] -= 1
        else:
            done = True
    elif t == "L":
        if not visited[current["y"]][current["x"] + 1]:
            current["x"] += 1
        elif not visited[current["y"] - 1][current["x"]]:
            current["y"] -= 1
        else:
            done = True
    elif t == "J":
        if not visited[current["y"]][current["x"] - 1]:
            current["x"] -= 1
        elif not visited[current["y"] - 1][current["x"]]:
            current["y"] -= 1
        else:
            done = True
    elif t == "7":
        if not visited[current["y"]][current["x"] - 1]:
            current["x"] -= 1
        elif not visited[current["y"] + 1][current["x"]]:
            current["y"] += 1
        else:
            done = True
    elif t == "F":
        if not visited[current["y"]][current["x"] + 1]:
            current["x"] += 1
        elif not visited[current["y"] + 1][current["x"]]:
            current["y"] += 1
        else:
            done = True
    steps += 1

print(round(steps / 2))

total = 0
for y, line in enumerate(lines):
    included = False
    for x, t in enumerate(line):
        if not visited[y][x]:
            if included:
                total += 1
                lines[y][x] = "I"
            else:
                lines[y][x] = "O"
        elif lines[y][x] in ["|", "7", "F"]:
            included = not included
    # print("".join(line))
print(total)
