from dataclasses import dataclass
import util
import functools

lines = util.get_input_lines()


@dataclass
class Node:
    def __init__(self, name: str, paths: list[str]):
        self.name = name
        self.paths = paths


nodes: dict[str, Node] = {}

you = None

for l in lines:
    idx, items = l.split(": ")
    items = items.split()
    n = Node(idx, items)
    nodes[idx] = n
    if idx == "you":
        you = n

assert you is not None


@functools.lru_cache(maxsize=None)
def count_paths(from_node: str) -> int:
    if from_node == "out":
        return 1

    total = 0
    for s in nodes[from_node].paths:
        total += count_paths(s)

    return total


@functools.lru_cache(maxsize=None)
def count_paths_b(from_node: str, fft: bool, dac: bool) -> int:
    if from_node == "out":
        return int(fft and dac)

    total = 0
    for s in nodes[from_node].paths:
        total += count_paths_b(s, fft or from_node == "fft", dac or from_node == "dac")

    return total


print("Part A: ", count_paths("you"))
print("Part B: ", count_paths_b("svr", False, False))
