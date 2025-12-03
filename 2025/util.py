def get_input_lines(filename: str = "input.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def get_input_lines_of_ints(filename: str = "input.txt"):
    return [[int(x) for x in l.split()] for l in get_input_lines(filename)]


def get_input_lines_int(filename: str = "input.txt"):
    return [int(l) for l in get_input_lines(filename)]


def get_input_csv(filename: str = "input.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().strip().split(",")


def get_input_csv_int(filename: str = "input.txt"):
    return [int(l) for l in get_input_csv(filename)]
