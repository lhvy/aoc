from multiprocessing.pool import ThreadPool


lines = open("input.txt", "r").read().strip().split("\n\n")


class Convert:
    def __init__(self):
        self.conversions = {}

    def add_range(self, start_out, start_in, length):
        self.conversions[start_in] = (start_out, length)

    def do(self, value):
        for start_in in self.conversions:
            if (
                value >= start_in
                and value <= start_in + self.conversions[start_in][1] - 1
            ):
                return self.conversions[start_in][0] + (value - start_in)

        return value


def process_map(values_in, map_lines):
    convert = Convert()

    for m in map_lines:
        nums = [int(v) for v in m.split()]
        convert.add_range(nums[0], nums[1], nums[2])
    out = [convert.do(s) for s in values_in]
    return out


values = [int(s) for s in lines[0].strip("seeds: ").split()]
maps = lines[1].strip("seed-to-soil map:\n").splitlines()
values = process_map(values, maps)
maps = lines[2].strip("soil-to-fertilizer map:\n").splitlines()
values = process_map(values, maps)
maps = lines[3].strip("fertilizer-to-water map:\n").splitlines()
values = process_map(values, maps)
maps = lines[4].strip("water-to-light map:\n").splitlines()
values = process_map(values, maps)
maps = lines[5].strip("light-to-temperature map:\n").splitlines()
values = process_map(values, maps)
maps = lines[6].strip("temperature-to-humidity map:\n").splitlines()
values = process_map(values, maps)
maps = lines[7].strip("humidity-to-location map:\n").splitlines()
values = process_map(values, maps)
print(min(values))


# All code below here is for part 2. This took 1 full hour to run with my input. Yikes
def make_map(map_lines):
    convert = Convert()

    for m in map_lines:
        nums = [int(v) for v in m.split()]
        convert.add_range(nums[0], nums[1], nums[2])

    return convert


maps = lines[1].strip("seed-to-soil map:\n").splitlines()
seed_map = make_map(maps)
maps = lines[2].strip("soil-to-fertilizer map:\n").splitlines()
soil_map = make_map(maps)
maps = lines[3].strip("fertilizer-to-water map:\n").splitlines()
fertilizer_map = make_map(maps)
maps = lines[4].strip("water-to-light map:\n").splitlines()
water_map = make_map(maps)
maps = lines[5].strip("light-to-temperature map:\n").splitlines()
light_map = make_map(maps)
maps = lines[6].strip("temperature-to-humidity map:\n").splitlines()
temperature_map = make_map(maps)
maps = lines[7].strip("humidity-to-location map:\n").splitlines()
humidity_map = make_map(maps)

values = [int(s) for s in lines[0].strip("seeds: ").split()]
values = list(zip(*[iter(values)] * 2))


def process_range(r):
    start = r[0]
    length = r[1]
    min_out = start + length
    # percent = 0
    for i in range(0, length):
        # if i * 100 / length > percent:
        #     percent = i * 100 / length
        #     print(start, percent)
        value = seed_map.do(start + i)
        value = soil_map.do(value)
        value = fertilizer_map.do(value)
        value = water_map.do(value)
        value = light_map.do(value)
        value = temperature_map.do(value)
        value = humidity_map.do(value)
        if value < min_out:
            min_out = value
    return min_out


pool = ThreadPool()
print(min(pool.map(process_range, values)))
pool.close()
