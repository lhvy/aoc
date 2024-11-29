import copy

data = [
    int(x)
    for x in open("input.txt", mode="r", encoding="utf-8").read().strip().split(",")
]

nums = copy.deepcopy(data)
nums[1] = 12
nums[2] = 2

position = 0
while nums[position] != 99:
    if nums[position] == 1:
        posA = nums[position + 1]
        posB = nums[position + 2]
        posC = nums[position + 3]
        nums[posC] = nums[posA] + nums[posB]
    elif nums[position] == 2:
        posA = nums[position + 1]
        posB = nums[position + 2]
        posC = nums[position + 3]
        nums[posC] = nums[posA] * nums[posB]
    else:
        raise ValueError("Bad opcode")
    position += 4
print(nums[0])

noun = -1
nums = [0]

while nums[0] != 19690720 and noun < 100:
    noun += 1
    verb = -1
    while nums[0] != 19690720 and verb < 100:
        verb += 1
        nums = copy.deepcopy(data)
        nums[1] = noun
        nums[2] = verb
        position = 0
        while nums[position] != 99:
            if nums[position] == 1:
                posA = nums[position + 1]
                posB = nums[position + 2]
                posC = nums[position + 3]
                nums[posC] = nums[posA] + nums[posB]
            elif nums[position] == 2:
                posA = nums[position + 1]
                posB = nums[position + 2]
                posC = nums[position + 3]
                nums[posC] = nums[posA] * nums[posB]
            else:
                raise ValueError("Bad opcode")
            position += 4
if nums[0] == 19690720:
    print(100 * noun + verb)
else:
    print("Not found")
