import util

rotations = util.get_input_lines()
# print(rotations)

dial = 50
zeros = 0
any_zeros = 0

for r in rotations:
    d = r[0]
    n = int(r[1:])

    any_zeros += n // 100
    n %= 100

    if n == 0:
        if dial == 0:
            zeros += 1
        continue

    prev_dial = dial

    if d == "L":
        dial -= n
    else:
        dial += n

    if dial % 100 != dial:
        dial += 100 if dial < 0 else -100
        if prev_dial != 0 and dial != 0:
            any_zeros += 1
            # print(r)

    if dial == 0:
        # print(r)
        any_zeros += 1
        zeros += 1

print("Part A: ", zeros)
print("Part B: ", any_zeros)
