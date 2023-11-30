from util import *

input = get_input_lines()


def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i
        elif curr_frequency == counter:
            if i == "1":
                num = i

    return num


b = []

for c in input[0]:
    b.append([])

for bin in input:
    for i in range(len(bin)):
        b[i].append(bin[i])

final = ""
for c in b:
    final += most_frequent(c)

final_dec = int(final, 2)

elipson = final.replace("1", "_").replace("0", "1").replace("_", "0")
elipson_dec = int(elipson, 2)

print(final_dec * elipson_dec)

oxy = 0


def find_match(input, pos, invert):
    b = []
    for bin in input:
        b.append(bin[pos])
    c = most_frequent(b)

    found = False
    match = []
    for j in range(len(input)):
        if (c == input[j][pos]) != invert and not found:
            match.append(input[j])
    if len(match) == 1:
        return int(match[0], 2)
    else:
        return find_match(match, pos + 1, invert)


oxy = find_match(input, 0, False)
co2 = find_match(input, 0, True)

print(oxy * co2)
