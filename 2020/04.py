import string
from util import *

# Custom read file code due to wacky format
passports_raw = get_input_double_newline()

pasports = []
for passport_raw in passports_raw:
    passport_raw = passport_raw.replace("\n", " ").split(" ")
    passport = {}
    for field in passport_raw:
        passport[field.split(":")[0]] = field.split(":")[1]
    pasports.append(passport)


class Passport:
    def __init__(self, passport):
        self.byr = passport.get("byr")
        self.iyr = passport.get("iyr")
        self.eyr = passport.get("eyr")
        self.hgt = passport.get("hgt")
        self.hcl = passport.get("hcl")
        self.ecl = passport.get("ecl")
        self.pid = passport.get("pid")
        self.cid = passport.get("cid")

    def correct_fields(self):
        return (
            self.byr
            and self.iyr
            and self.eyr
            and self.hgt
            and self.hcl
            and self.ecl
            and self.pid != None
        )

    def valid_fields(self):
        if not self.correct_fields():
            return False

        valid_byr = 1920 <= int(self.byr) <= 2002
        valid_iyr = 2010 <= int(self.iyr) <= 2020
        valid_eyr = 2020 <= int(self.eyr) <= 2030
        valid_hgt = (self.hgt[-2:] == "cm" and 150 <= int(self.hgt[:-2]) <= 193) or (
            self.hgt[-2:] == "in" and 59 <= int(self.hgt[:-2]) <= 76
        )
        valid_hcl = (
            self.hcl[0] == "#"
            and len(self.hcl) == 7
            and all(char in string.hexdigits for char in self.hcl[1:])
        )
        valid_ecl = self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        valid_pid = len(self.pid) == 9 and self.pid.isdigit()
        return (
            valid_byr
            and valid_iyr
            and valid_eyr
            and valid_hgt
            and valid_hcl
            and valid_ecl
            and valid_pid
        )


# Part 1
valid_passports = 0

for passport in pasports:
    p = Passport(passport)
    if p.correct_fields():
        valid_passports += 1

print(valid_passports)

# Part 2
valid_passports = 0

for passport in pasports:
    p = Passport(passport)
    if p.valid_fields():
        valid_passports += 1

print(valid_passports)
