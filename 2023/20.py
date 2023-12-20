raw_lines = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()


class Pulse:
    def __init__(self, high: bool, dest: str):
        self.high = high
        self.dest = dest


class Module:
    def __init__(self, t: str, dest: list[str]):
        self.t = t
        self.on = False
        self.memory: dict[str, bool] = {}
        self.dest = dest

    def add_input(self, src: str):
        self.memory[src] = False

    def handle(self, high: bool, src: str):
        match self.t:
            case "%":
                if high:
                    return [], False
                self.on = not self.on
                return self.dest, self.on
            case "&":
                self.memory[src] = high
                if len(set(self.memory.values())) == 1:
                    return self.dest, not high
                else:
                    return self.dest, True

    def reset(self):
        self.on = False
        for key in self.memory:
            self.memory[key] = False


modules: dict[str, Module] = {}
for module in raw_lines:
    if module.startswith("broadcaster"):
        broadcast = module.split(" -> ")[1].split(", ")
        continue
    name, raw_dest = module.split(" -> ")
    dest = raw_dest.split(", ")
    modules[name[1:]] = Module(name[0], dest)

for module in raw_lines:
    if module.startswith("broadcaster"):
        for d in module.split(" -> ")[1].split(", "):
            modules[d].add_input("broadcaster")
        continue
    name, raw_dest = module.split(" -> ")
    dest = raw_dest.split(", ")
    for d in dest:
        if d == "output" or d == "rx":
            continue
        modules[d].add_input(name[1:])

part_one = [0, 0]

for _ in range(1000):
    pulses = [(dest, False, "broadcaster") for dest in broadcast]
    part_one[0] += len(pulses) + 1
    while len(pulses) > 0:
        p = pulses.pop(0)
        dest, high = modules[p[0]].handle(p[1], p[2])
        if high:
            part_one[1] += len(dest)
        else:
            part_one[0] += len(dest)
        for d in dest:
            if d == "output" or d == "rx":
                continue
            # print(p[0], high, "->", d)
            pulses.append((d, high, p[0]))
print(part_one)
print(part_one[0] * part_one[1])

for m in modules:
    modules[m].reset()
presses = 0
lcm = 0
rx = True
while rx and lcm < 4:
    presses += 1
    pulses = [(dest, False, "broadcaster") for dest in broadcast]
    part_one[0] += len(pulses) + 1
    while len(pulses) > 0:
        p = pulses.pop(0)
        dest, high = modules[p[0]].handle(p[1], p[2])
        if high:
            part_one[1] += len(dest)
        else:
            part_one[0] += len(dest)
        for d in dest:
            if d == "output":
                continue
            elif d == "dn" and high:
                print(presses, p[0], "dn")
                lcm += 1
            elif d == "rx":
                rx = high
                continue
            # print(p[0], high, "->", d)
            pulses.append((d, high, p[0]))
    # print(presses)
if rx:
    print("Multiply the 4 numbers together.")
    print("Note, my input has 'dn' as the source for 'rx'. This may differ for you.")
else:
    print("Presses required for 'rx' to be low:", presses)
