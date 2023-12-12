from functools import lru_cache

raw_lines = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()


@lru_cache(maxsize=None)
def validate(row: str, damaged: tuple[int], cont: int):
    for i, state in enumerate(row):
        if state == "#":
            cont += 1
        elif state == ".":
            if cont > 0:
                if len(damaged) < 1 or cont != damaged[0]:
                    return 0
                damaged = damaged[1:]
                cont = 0
        elif state == "?":
            valid = validate("." + row[(i + 1) :], damaged, cont)
            if len(damaged) > 0 and cont < damaged[0]:
                valid += validate("#" + row[(i + 1) :], damaged, cont)
            return valid

    if (cont > 0 and (len(damaged) != 1 or cont != damaged[0])) or (
        len(damaged) > 0 and cont == 0
    ):
        return 0
    return 1


part_one = 0
part_two = 0
for line in raw_lines:
    a = line.split()[0]
    b = [int(n) for n in line.split()[1].split(",")]
    part_one += validate(a, tuple(b), 0)
    part_two += validate(a + "?" + a + "?" + a + "?" + a + "?" + a, tuple(b * 5), 0)
    # print(validate(a, b, 0))
print(part_one)
print(part_two)
