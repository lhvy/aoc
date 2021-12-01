from util import *

input = get_input_lines()


class Bag:
    def __init__(self, color, children):
        self.color = color
        self.children = children


class Child:
    def __init__(self, color, amount):
        self.color = color
        self.amount = amount


def parse_bags():
    bags = {}
    for line in input:
        line = line.split(" bags contain ")
        color = line[0]
        children = []
        for bag in line[1].split(", "):
            if bag == "no other bags.":
                break
            bag = bag.replace(".", "").split(" ")
            number = int(bag[0])
            child_color = bag[1] + " " + bag[2]
            children.append(Child(child_color, number))
        bags[color] = Bag(color, children)
    return bags


rules = parse_bags()


def contains_shiny_gold(bag):
    for child in bag.children:
        child = rules[child.color]
        if child.color == "shiny gold" or contains_shiny_gold(child):
            return True


def count_children(bag):
    count = 0
    for child in bag.children:
        count += child.amount + child.amount * count_children(rules[child.color])
    return count


# Part 1
shiny_gold = 0

for bag in rules.values():
    if contains_shiny_gold(bag):
        shiny_gold += 1

print(shiny_gold)

# Part 2
shiny_gold = rules["shiny gold"]
total = count_children(shiny_gold)
print(total)
