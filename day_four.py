import re


def validate_passwords(passport_document):
    passports = passport_document.split("\n\n")
    count = 0
    for passport in passports:
        passport = passport.replace("\n", " ")
        if check_passport_valid(passport):
            count += 1
    return count


def check_passport_valid(passport):
    passport_lines = passport.split(" ")

    for passport_line in passport_lines:
        splitted_pass_line = passport_line.split(":")
        if len(splitted_pass_line) == 2 and splitted_pass_line[0] != "cid":
            if not check_line(splitted_pass_line[0], splitted_pass_line[1]):
                return False
    if len(passport_lines) == 7 and not (0 in list(map(lambda x: x.find("cid", 0), passport_lines))):
        return True
    else:
        return len(passport_lines) == 8


def check_line(prefix, value):
    if prefix == "byr":
        return (1920 <= int(value) <= 2002) and len(value) == 4

    elif prefix == "iyr":
        return (2010 <= int(value) <= 2020) and len(value) == 4

    elif prefix == "eyr":
        return (2020 <= int(value) <= 2030) and len(value) == 4

    elif prefix == "hgt" and value[-2:] == "cm":
        return 150 <= int(value[:-2]) <= 193

    elif prefix == "hgt" and value[-2:] == "in":
        return 59 <= int(value[:-2]) <= 76

    elif prefix == "hcl":
        return bool(re.search("^#[0-9a-f]{6}$", value))

    elif prefix == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    elif prefix == "pid":
        return bool(re.search("^[0-9]{9}$", value))
