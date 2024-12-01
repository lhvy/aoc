import util

lines = util.get_input_lines()

left = []
right = []
for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

t = 0
for i, v in enumerate(left):
    t += abs(right[i] - v)
print(t)

t = 0
for n in left:
    t += n * right.count(n)
print(t)
