import util

lines = util.get_input_lines()


def check(target, current, values):
    if current > target:
        return False

    if len(values) == 1:
        return (
            current + values[0] == target
            or current * values[0] == target
            or int(str(current) + str(values[0])) == target
        )
    else:
        return (
            check(target, current + values[0], values[1:])
            or check(target, current * values[0], values[1:])
            or check(target, int(str(current) + str(values[0])), values[1:])
        )


total = 0
for line in lines:
    raw_target, rest = line.split(": ")
    target = int(raw_target)
    values = [int(x) for x in rest.split()]
    if check(target, 0, tuple(values)):
        total += target
print(total)
