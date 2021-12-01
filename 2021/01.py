from util import *

input = get_input_ints()


def count_greater(d):
    greater = 0
    for i in range(len(d)):
        if i == 0:
            continue
        if d[i] > d[i - 1]:
            greater += 1
    return greater


class Data:
    def __init__(self):
        self.data = [[]]
        self.first_unfilled = 0

    def process_measurement(self, measurement):
        l = len(self.data[self.first_unfilled])
        if l == 0:
            self.data[self.first_unfilled].append(measurement)
        elif l == 1:
            self.data[self.first_unfilled].append(measurement)
            self.data.append([measurement])
        elif l == 2:
            self.data[self.first_unfilled].append(measurement)
            self.data[self.first_unfilled + 1].append(measurement)
            self.data.append([measurement])
            self.first_unfilled += 1

    def finish(self):
        while len(self.data[-1]) < 3:
            self.data.pop()
        for i in range(len(self.data)):
            self.data[i] = sum(self.data[i])


# Part 1
print(count_greater(input))

# Part 2
data = Data()
for i in input:
    data.process_measurement(i)
data.finish()

print(count_greater(data.data))
