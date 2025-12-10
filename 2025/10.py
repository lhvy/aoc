import numpy as np
import pulp


class Machine:
    def __init__(self, line: str):
        parts = line.split()

        # Construct binary string
        lights: list[str] = []
        for c in parts[0][1:]:
            if c == "]":
                break

            if c == ".":
                lights.append("0")
            elif c == "#":
                lights.append("1")
            else:
                print(c)
                assert False

        # Bit mask of required lights
        self.lights = int("".join(lights), base=2)

        # Construct button masks
        # Also construct as list of 0s and 1s for linear alg solver
        self.buttons_mask: list[int] = []
        self.buttons: list[list[int]] = []
        for button in parts[1:-1]:
            toggle = [int(x) for x in button[1:-1].split(",")]
            b_mask = ["0"] * len(lights)
            b = [0] * len(lights)
            for t in toggle:
                b_mask[t] = "1"
                b[t] = 1
            self.buttons_mask.append(int("".join(b_mask), base=2))
            self.buttons.append(b)

        self.joltage = [int(x) for x in parts[-1][1:-1].split(",")]

    def part_a(self) -> int:
        presses = len(self.buttons) + 1
        for i in range(2 ** len(self.buttons)):
            # Bit indexes of buttons to press
            press: list[int] = []
            for j in range(len(self.buttons)):
                if (i >> j) & 1:
                    press.append(j)

            state = 0
            for p in press:
                state ^= self.buttons_mask[p]

            if state == self.lights:
                presses = min(presses, len(press))

        assert presses <= len(self.buttons)
        return presses

    # Solve linear combination of buttons to match joltage requirements
    # (LpMinimize will find the lowest coefficient sum)
    def part_b(self):
        rows = np.array(self.buttons, dtype=int)
        target = np.array(self.joltage, dtype=int)

        n_rows, n_cols = rows.shape

        problem = pulp.LpProblem("AoC", pulp.LpMinimize)
        x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(n_rows)]
        problem += pulp.lpSum(x)

        for j in range(n_cols):
            problem += pulp.lpSum(rows[i][j] * x[i] for i in range(n_rows)) == target[j]

        status = problem.solve(pulp.PULP_CBC_CMD(msg=False))
        assert pulp.LpStatus[status] == "Optimal"

        # varValue can be float or None, ignore since we just asserted solution found
        values = [int(var.varValue) for var in x]  # type: ignore
        return sum(values)


part_a = 0
part_b = 0

lines = open("input.txt", "r", encoding="utf-8").read().splitlines()
for line in lines:
    machine = Machine(line)
    part_a += machine.part_a()
    part_b += machine.part_b()

print("Part A: ", part_a)
print("Part B: ", part_b)
