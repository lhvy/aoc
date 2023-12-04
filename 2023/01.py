import re

raw = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()


def main():
    total = 0
    for l in raw:
        n = re.sub(r"\D", "", l)
        total += int(n[0] + n[-1])
    print(total)

    total = 0
    for l in raw:
        start = (
            re.findall(r"(one|two|three|four|five|six|seven|eight|nine|[0-9])", l)[0]
            .replace("one", "1")
            .replace("two", "2")
            .replace("three", "3")
            .replace("four", "4")
            .replace("five", "5")
            .replace("six", "6")
            .replace("seven", "7")
            .replace("eight", "8")
            .replace("nine", "9")
        )
        end = (
            re.findall(
                r"(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|[0-9])", l[::-1]
            )[0]
            .replace("eno", "1")
            .replace("owt", "2")
            .replace("eerht", "3")
            .replace("ruof", "4")
            .replace("evif", "5")
            .replace("xis", "6")
            .replace("neves", "7")
            .replace("thgie", "8")
            .replace("enin", "9")
        )
        print(int(start + end))
        total += int(start + end)
    print(total)


main()
