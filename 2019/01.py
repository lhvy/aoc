nums = [int(x) for x in open("input.txt", mode="r", encoding="utf-8").read().split()]

total = 0
for n in nums:
    total += n // 3 - 2
print(total)

total = 0
for n in nums:
    mass = n // 3 - 2
    while mass > 0:
        total += mass
        mass = mass // 3 - 2
print(total)
