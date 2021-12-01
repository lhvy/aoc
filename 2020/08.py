from util import *
from enum import Enum
import copy


input = get_input_lines()


class Action(Enum):
    ACC = 0
    JMP = 1
    NOP = 2


class Instruction:
    def __init__(self, action, value):
        self.action = action
        self.value = value

class Program:
    def __init__(self, instructions):
        self.instructions = copy.deepcopy(instructions) # Modifications in pt 2 don't affect the original
        self.position = 0
        self.acc = 0
        self.executed = []

    def execute(self) -> int:
        while self.position < len(self.instructions):
            if self.position in self.executed:
                break
            instruction = self.instructions[self.position]
            self.executed.append(self.position)
            match instruction.action:
                case Action.ACC:
                    self.acc += instruction.value
                    self.position += 1
                case Action.JMP:
                    self.position += instruction.value
                case Action.NOP:
                    self.position += 1
        return self.acc

instructions = []
for line in input:
    action,value = line.split(' ')
    match action:
        case "acc":
            action = Action.ACC
        case "jmp":
            action = Action.JMP
        case "nop":
            action = Action.NOP
    instructions.append(Instruction(action, int(value)))

# Part 1
program = Program(instructions)
print(program.execute())

# Part 2
for i in range(len(instructions)):
    if instructions[i].action == Action.JMP or instructions[i].action == Action.NOP:
        program = Program(instructions)
        if instructions[i].action == Action.JMP:
            program.instructions[i].action = Action.NOP
        else:
            program.instructions[i].action = Action.JMP
        value = program.execute()
        if program.position >= len(instructions): # Has passed final instruction
            print(value)
            break
