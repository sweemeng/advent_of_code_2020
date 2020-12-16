from functools import partial
import re


note_pattern = r"(?P<key>^\w+\s?\w+)\:\s(?P<range_1>\d+\-\d+)\sor\s(?P<range_2>\d+\-\d+)"
own_ticket_pattern = r"^your ticket\:"
nearby_ticket_pattern = r"^nearby tickets\:"


def process_data(data):
    notes = {}
    process_own = False
    process_nearby = False
    own_ticket = []
    nearby_ticket = []
    for entry in data:
        match = re.match(note_pattern, entry)
        if match:
            key = match.group("key")
            temp_1 = match.group("range_1").split("-")
            range_1 = range(int(temp_1[0]), int(temp_1[1])+1)
            temp_2 = match.group("range_2").split("-")
            range_2 = range(int(temp_2[0]), int(temp_2[1])+1)
            notes[key] = [range_1, range_2]
            continue
        
        match = re.match(own_ticket_pattern, entry)
        if match:
            process_own = True
            continue

        match = re.match(nearby_ticket_pattern, entry)
        if match:
            process_nearby = True
            continue
        if not entry:
            continue
        if process_own:
            own_ticket = [int(i) for i in entry.split(",")]
            process_own = False
        if process_nearby:
            ticket = [int(i) for i in entry.split(",")]
            nearby_ticket.append(ticket)
    return notes, own_ticket, nearby_ticket


def validate_data(notes, ticket):
    values = []
    for i in ticket:
        results = []
        for key, ranges in notes.items():
            result = [
                i in ranges[0],
                i in ranges[1]
            ]
            results.append(any(result))
        if not any(results):
            values.append(i)
    return values


def validate_value(value, key, notes):
    rules = notes[key]
    result = [
        value in rules[0],
        value in rules[1],
    ]
    
    return any(result)


def generate_keys(columns, valid_keys, notes):
    candidates = []
    for key in valid_keys:
        validator = partial(validate_value, key=key, notes=notes)
        result = list(filter(validator, columns))
        if len(result) == len(columns):
            candidates.append(key)
    return candidates


def generate_solution_one(nearby_ticket, notes):
    rates = 0
    valid_nearby = []
    for i in nearby_ticket:
        values = validate_data(notes, i)
        if values:
            rates += sum(values)
        else:
            valid_nearby.append(i)
    return rates, valid_nearby
    

def main():
    with open("input") as f:
        data = f.readlines()
    notes, own_ticket, nearby_ticket = process_data(data)
    rates, valid_nearby = generate_solution_one(nearby_ticket, notes)
    print(f"result 1: {rates}")
    valid_keys = list(notes.keys())
    ordered_keys = {}
    indexes = list(range(len(own_ticket)))
    
    while True:
        candidates = {}
        if not indexes:
            break
        for index in indexes:
            columns = [i[index] for i in valid_nearby]
            keys = generate_keys(columns, valid_keys, notes)
            
            candidates[index] = keys
        for index, keys in candidates.items():
            if not keys:
                continue
            if len(keys) == 1:
                ordered_keys[keys[0]] = index
                valid_keys.remove(keys[0])
                indexes.remove(index)
    result2 = 1
    for key,value in ordered_keys.items():
        if "departure" in key:
            result2 *= own_ticket[value]
    print(f"result 2 is {result2}")


if __name__ == "__main__":
    main()
