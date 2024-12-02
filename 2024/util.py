def get_input_lines(filename="input.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def get_input_lines_of_ints(filename="input.txt"):
    return [[int(x) for x in l.split()] for l in get_input_lines(filename)]


def get_input_lines_int(filename="input.txt"):
    return [int(l) for l in get_input_lines(filename)]


def get_input_csv(filename="input.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().strip().split(",")


def get_input_csv_int(filename="input.txt"):
    return [int(l) for l in get_input_csv(filename)]
