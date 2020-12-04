import re
from functools import partial


def extract_passports(data):
    datas = []
    buff_data = {}
    for line in data.readlines():
        line = line.rstrip()
        if not line:
            datas.append(buff_data)
            buff_data = {}
        tokens = line.split()
        for token in tokens:
            key, value = token.split(":")
            buff_data[key] = value
    if buff_data:
        datas.append(buff_data)
    return datas


def validate_passport(data, strict=False, debug=False):
    validators = {
        'ecl': validate_ecl, 
        'pid': validate_pid, 
        'eyr': partial(validate_number, low=2020, high=2030), 
        'hcl': validate_hcl,
        'byr': partial(validate_number, low=1920, high=2002),
        'iyr': partial(validate_number, low=2010, high=2020),
        'hgt': validate_hgt
    }
    for key in validators:
        value = data.get(key)
        if not value:
            return False
        if strict:
            if not validators[key](value):
                if debug:
                    print(key, value)
                return False

    return True


def valid_count(data, strict=False):
    results = extract_passports(data)
    count = 0
    for result in results:
        if validate_passport(result, strict=strict):
            count = count + 1
    return count


def validate_hgt(value):
    unit = value[-2:]
    try:
        amount = int(value[:-2])
    except ValueError:
        return False
    if unit not in ["in", "cm"]:
        return False
    if unit == "in":
        if amount >= 59 and amount <=76:
            return True
        return False
    if unit == "cm":
        if amount >=150 and amount <=193:
            return True
        return False
    return False


def validate_number(value, low, high):
    try:
        value = int(value)
        if value >= low and value <= high:
            return True
        return False
    except ValueError:
        return False


def validate_ecl(value):
    valid_value = set(['amb','blu','brn','gry','grn','hzl','oth'])
    if value in valid_value:
        return True
    return False


def validate_hcl(value):
    if re.match("^#[a-f0-9]{6}", value):
        return True
    return False


def validate_pid(value):
    if re.match(r"^\d{9}$", value):
        return True
    return False


if __name__ == "__main__":
    f = open("input")
    count = valid_count(f)
    print(f"solution 1: {count}")
    f = open("input")
    count_strict = valid_count(f, strict=True)
    print(f"solution 2: {count_strict}")
