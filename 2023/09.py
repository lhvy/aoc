lines = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()

total = 0
for line in lines:
    diff = [[int(v) for v in line.split()]]
    while not (len(set(diff[-1])) == 1 and 0 in diff[-1]):
        new = []
        i = 1
        while i < len(diff[-1]):
            new.append(diff[-1][i] - diff[-1][i - 1])
            i += 1
        diff.append(new)

    i = len(diff) - 1 - 1
    diff[-1].append(0)
    while i >= 0:
        diff[i].append(diff[i][-1] + diff[i + 1][-1])
        i -= 1

    total += diff[0][-1]
print(total)

total = 0
for line in lines:
    diff = [[int(v) for v in line.split()]]
    while not (len(set(diff[-1])) == 1 and 0 in diff[-1]):
        new = []
        i = 1
        while i < len(diff[-1]):
            new.append(diff[-1][i] - diff[-1][i - 1])
            i += 1
        diff.append(new)

    i = len(diff) - 1 - 1
    diff[-1].insert(0, 0)
    while i >= 0:
        diff[i].insert(0, diff[i][0] - diff[i + 1][0])
        i -= 1

    total += diff[0][0]
print(total)
