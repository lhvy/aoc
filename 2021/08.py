from util import *
from copy import deepcopy

input = get_input_lines()

digits = [
    ["a", "b", "c", "e", "f", "g"],  # 6
    ["c", "f"],  # 2
    ["a", "c", "d", "e", "g"],  # 5
    ["a", "c", "d", "f", "g"],  # 5
    ["b", "c", "d", "f"],  # 4
    ["a", "b", "d", "f", "g"],  # 5
    ["a", "b", "d", "e", "f", "g"],  # 6
    ["a", "c", "f"],  # 3
    ["a", "b", "c", "d", "e", "f", "g"],  # 7
    ["a", "b", "c", "d", "f", "g"],  # 6
]


def subtract(a, b):
    return [x for x in a if x not in b]


d1_4_7_8 = 0
total = 0

for line in input:
    mapping = {}
    signals, output = line.split(" | ")
    signals = signals.split()
    output = output.split()
    for s in signals:
        if len(s) == 2:
            possible_c = list(s)
            possible_f = list(s)
            break
    for s in signals:
        if len(s) == 3:  # 7
            possible_a = subtract(list(s), possible_c)
            break
    for s in signals:
        if len(s) == 4:  # 4
            possible_b = subtract(list(s), possible_c)
            possible_d = subtract(list(s), possible_f)
            break
    for s in signals:
        if len(s) == 5 and all(i in list(s) for i in possible_c):  # 2 or 3
            for i in deepcopy(possible_d):
                if i not in list(s):
                    possible_d.remove(i)
                else:
                    possible_b.remove(i)
            code = deepcopy(list(s))
            code.remove(possible_a[0])
            code.remove(possible_d[0])
            result = subtract(code, possible_c)
            possible_g = result
            if len(result) == 2:
                possible_e = result
                possible_f = subtract(possible_f, list(s))
            # else:
            #     print(len(result))
    for s in signals:
        if len(s) == 5 and not all(i in list(s) for i in possible_c):
            possible_c = subtract(possible_c, list(s))
            possible_f = subtract(possible_f, possible_c)
    for s in signals:
        if len(s) == 7:
            possible_e = subtract(
                list(s),
                possible_a
                + possible_b
                + possible_c
                + possible_d
                + possible_f
                + possible_g,
            )

    signal_map = {
        possible_a[0]: "a",
        possible_b[0]: "b",
        possible_c[0]: "c",
        possible_d[0]: "d",
        possible_e[0]: "e",
        possible_f[0]: "f",
        possible_g[0]: "g",
    }

    # Getting a weird issue where some outputs work if c and f are flipped
    alt_signal_map = {
        possible_a[0]: "a",
        possible_b[0]: "b",
        possible_f[0]: "c",
        possible_d[0]: "d",
        possible_e[0]: "e",
        possible_c[0]: "f",
        possible_g[0]: "g",
    }

    d = []
    for o in output:
        segments = []
        for c in o:
            segments.append(signal_map[c])
        for i in range(len(digits)):
            if set(segments) == set(digits[i]):
                d.append(i)
                if i == 1 or i == 4 or i == 7 or i == 8:
                    d1_4_7_8 += 1
                break

    if len(d) == 4:
        num = int("".join(map(str, d)))
        print(num)
        total += num
    else:  # If the output is not 4, try the other mapping
        d = []
        for o in output:
            segments = []
            for c in o:
                segments.append(alt_signal_map[c])
            for i in range(len(digits)):
                if set(segments) == set(digits[i]):
                    d.append(i)
                    if i == 1 or i == 4 or i == 7 or i == 8:
                        d1_4_7_8 += 1
                    break
        num = int("".join(map(str, d)))
        print(num)
        total += num

print(d1_4_7_8)
print(total)
