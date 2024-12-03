import util
import re

lines = util.get_input_lines()
text = "".join(lines)

total = 0
results = re.findall(r"mul\((\d+),(\d+)\)", text)
for a, b in results:
    total += int(a) * int(b)
print(total)

total = 0
enabled = True
results = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", text)
for r in results:
    if r[2] == "do()":
        enabled = True
    elif r[3] == "don't()":
        enabled = False
    elif enabled:
        a, b = r[0], r[1]
        total += int(a) * int(b)
print(total)
