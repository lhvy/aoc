import util

lines = util.get_input_lines()

part_a = 0
part_b = 0

for l in lines:
    best = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            best = max(int(l[i] + l[j]), best)
    part_a += best

for l in lines:
    stack: list[str] = []
    safe_to_bin = len(l) - 12
    for idx, digit in enumerate(l):
        while len(stack) > 0 and stack[-1] < digit and safe_to_bin > 0:
            stack.pop()
            safe_to_bin -= 1

        stack.append(digit)  # append regardless so safe_to_bin works

    part_b += int("".join(stack[:12]))

print("Part A: ", part_a)
print("Part B: ", part_b)
