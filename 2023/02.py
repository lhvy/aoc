raw = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()


class Game:
    def __init__(self, cubes: dict[str, int]):
        self.cubes = cubes

    def possible(self, cubes: dict[str, int]):
        for color in self.cubes:
            if color not in cubes.keys() or self.cubes[color] > cubes[color]:
                return False
        return True

    def power(self):
        total = 1
        for n in self.cubes.values():
            total *= n
        return total


games: dict[int, Game] = {}

for game in raw:
    game = game.removeprefix("Game ")
    game_id, raw_cubes = game.split(":")
    rounds = raw_cubes.split(";")

    cubes = {}
    for round in rounds:
        colors = round.split(",")
        for color in colors:
            color = color.strip()
            num, color = color.split(" ")
            if color not in cubes.keys() or int(num) > cubes[color]:
                cubes[color] = int(num)

    games[int(game_id)] = Game(cubes)

desired = {"red": 12, "green": 13, "blue": 14}
total = 0
power = 0
for game_id in games:
    power += games[game_id].power()
    if games[game_id].possible(desired):
        total += game_id

print(total)
print(power)
