import util

lines = util.get_input_lines()
levels = [[int(x) for x in l.split()] for l in lines]


def check_valid(level):
    prev = level[0]
    diff = level[1] - prev
    for j in range(1, len(level)):
        current_diff = level[j] - prev
        if (
            abs(current_diff) > 3
            or abs(current_diff) < 1
            or (diff != 0 and current_diff * diff < 0)
        ):
            return False
        diff = current_diff
        prev = level[j]
    return True


safe = 0
for l in levels:
    safe += check_valid(l)
print(safe)

safe = 0
for l in levels:
    v = check_valid(l)
    if not v:
        for i in range(len(l)):
            new_l = l[:i] + l[i + 1 :]
            if check_valid(new_l):
                safe += 1
                break
    else:
        safe += 1

print(safe)
