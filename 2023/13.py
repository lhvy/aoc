patterns = open("input.txt", "r", encoding="utf-8").read().strip().split("\n\n")

part_one = 0

for pattern in patterns:
    lines = pattern.splitlines()
    left = 0
    mirror = False
    while left < len(lines[0]) - 1 and not mirror:
        left += 1
        mirror = True
        for line in lines:
            if (
                line[max(0, left - (len(line) - left)) : left]
                != line[left : (left + left)][::-1]
            ):
                mirror = False
                break
    if mirror:
        part_one += left
        continue
    up = 0
    while up < len(lines) - 1 and not mirror:
        up += 1
        mirror = True
        for i in range(0, min(up, len(lines) - up)):
            if lines[up - 1 - i] != lines[up + i]:
                mirror = False
                break
    if mirror:
        part_one += 100 * up
        continue
    print("No mirror found!")

print(part_one)

# Part two is very similar, could probably combine it, but didn't have time during comp
# also would require some yucky logic since I can't early return once the smudged mirror is found
part_two = 0

for pattern in patterns:
    lines = pattern.splitlines()
    left = 0
    diff = 0
    while left < len(lines[0]) - 1 and diff != 1:
        left += 1
        diff = 0
        for line in lines:
            for a, b in zip(
                line[max(0, left - (len(line) - left)) : left],
                line[left : (left + left)][::-1],
            ):
                if a != b:
                    diff += 1
                    if diff > 1:
                        break
    if diff == 1:
        part_two += left
        continue
    up = 0
    while up < len(lines) - 1 and diff != 1:
        up += 1
        diff = 0
        for i in range(0, min(up, len(lines) - up)):
            for a, b in zip(lines[up - 1 - i], lines[up + i]):
                if a != b:
                    diff += 1
                    if diff > 1:
                        break
    if diff == 1:
        part_two += 100 * up
        continue
    print("No mirror found!")

print(part_two)
