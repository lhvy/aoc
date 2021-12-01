def get_input_lines():
    return open("input.txt", "r").read().strip().split("\n")


def get_input_ints():
    lines = get_input_lines()
    ints = []
    for line in lines:
        ints.append(int(line))
    return ints


def get_input_double_newline():
    return open("input.txt", "r").read().strip().split("\n\n")
