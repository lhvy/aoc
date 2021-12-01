from util import *

input = get_input_double_newline()


class Questions:
    def __init__(self):
        self.answers = {
            "a": False,
            "b": False,
            "c": False,
            "d": False,
            "e": False,
            "f": False,
            "g": False,
            "h": False,
            "i": False,
            "j": False,
            "k": False,
            "l": False,
            "m": False,
            "n": False,
            "o": False,
            "p": False,
            "q": False,
            "r": False,
            "s": False,
            "t": False,
            "u": False,
            "v": False,
            "w": False,
            "x": False,
            "y": False,
            "z": False,
        }

    def answer(self, letter):
        if letter in self.answers:
            self.answers[letter] = True

    def sum_answers(self):
        return sum(self.answers.values())


# Part 1
s = 0

for group in input:
    questions = Questions()
    for person in group.split("\n"):
        for letter in person:
            questions.answer(letter)
    s += questions.sum_answers()

print(s)

# Part 2
s = 0

for group in input:
    people = group.split("\n")
    for char in people[0]:
        everyone = True
        for person in people[1:]:
            if char not in person:
                everyone = False
                break
        if everyone:
            s += 1

print(s)
