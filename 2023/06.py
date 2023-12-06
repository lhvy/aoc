times, distances = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()
times = [int(t) for t in times.strip("Time:").split()]
distances = [int(d) for d in distances.strip("Distance:").split()]


def product(array):
    prod = 1
    for n in array:
        prod *= n
    return prod


def process(times, distances):
    solutions = []
    for i in range(0, len(times)):
        start = 0
        while start * (times[i] - start) <= distances[i]:
            start += 1
        end = times[i]
        while end * (times[i] - end) <= distances[i]:
            end -= 1
        solutions.append(end - start + 1)
    return product(solutions)


print(process(times, distances))

time, distance = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()
times = [int(time.strip("Time:").replace(" ", ""))]
distances = [int(distance.strip("Distance:").replace(" ", ""))]
print(process(times, distances))
