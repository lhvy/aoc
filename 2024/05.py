from graphlib import TopologicalSorter


raw_rules, raw_updates = (
    open("input.txt", "r", encoding="utf-8").read().strip().split("\n\n")
)

rules = [[int(x) for x in line.split("|")] for line in raw_rules.splitlines()]
updates = [[int(x) for x in line.split(",")] for line in raw_updates.splitlines()]

rule_dict: dict[int, list[int]] = {}
rule_graph: dict[int, list[int]] = {}
for rule in rules:
    if rule[0] not in rule_dict:
        rule_dict[rule[0]] = [rule[1]]
    else:
        rule_dict[rule[0]].append(rule[1])
    if rule[1] not in rule_graph:
        rule_graph[rule[1]] = [rule[0]]
    else:
        rule_graph[rule[1]].append(rule[0])


def check_valid(update: list[int]):
    seen = {}
    valid = True
    for i, page in enumerate(update):
        if page in rule_dict and any(n in seen for n in rule_dict[page]):
            n = update.pop(i)
            update.insert(next(n in seen for n in rule_dict[page]), n)
            valid = False
            break
        seen[page] = i
    return valid


total = 0
invalid = []
for update in updates:
    v = check_valid(update)
    if v:
        total += update[len(update) // 2]
    else:
        invalid.append(update)
print(total)

total = 0
for update in invalid:
    needed_rules = {
        key: [val for val in rule_graph[key] if val in update]
        for key in update
        if key in rule_graph
    }
    ts = TopologicalSorter(needed_rules)
    total += tuple(ts.static_order())[len(update) // 2]
print(total)
