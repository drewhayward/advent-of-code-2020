import re

def get_passports():
    passports = []
    with open('day4/input','r') as f:
        passport = {}
        for line in f.readlines():
            line = line.strip()
            if line:
                passport.update({pair.split(':')[0]:pair.split(':')[1] for pair in line.split(' ')})
            else:
                passports.append(passport)
                passport = {}
        if passport:
            passports.append(passport)
    return passports

def validate(passport):
    # Ensure the right keys are present
    required_keys = {'byr','iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    if required_keys.difference(passport.keys()):
        return False, 'key'

    # Validate the keys
    for key, field in passport.items():
        try:
            if key == 'byr':
                year = int(field)
                if not (1920 <= year <= 2002):
                    return False, key
            elif key == 'iyr':
                year = int(field)
                if not (2010 <= year <= 2020):
                    return False, key
            elif key == 'eyr':
                year = int(field)
                if not (2020 <= year <= 2030):
                    return False, key
            elif key == 'hgt':
                unit = field[-2:]
                num = int(field[:-2])
                if unit == 'cm':
                    if not (150 <= num <= 193):
                        return False, key
                elif unit == 'in':
                    if not (59 <= num <= 76):
                        return False, key
                else:
                    return False, key
            elif key == 'hcl':
                if not re.match(r'^#[0-9a-f]{6}$', field):
                    return False, key
            elif key == 'ecl':
                if not re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', field):
                    return False, key
            elif key == 'pid':

                int(field)
                if not len(field) == 9:
                    return False, key
            

        except Exception as e:
            print(e)
            return False, key

    return True, 'good'

def part_1():
    required_keys = {'byr','iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    total = 0
    for passport in get_passports():
        # Normal passport
        diff = required_keys.difference(passport.keys())
        if not diff:
            total += 1

    return total

def part_2():
    total = 0
    for passport in get_passports():
        if validate(passport)[0]:
            total += 1
    return total

if __name__ == "__main__":
    #print(part_1())
    print(part_2())
    # for passport in get_passports():
    #     pair = validate(passport)
    #     if pair[0]:
    #         print(passport['byr'])