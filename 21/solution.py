import re
import itertools


def split_data(line):
    patterns = r"(?P<ingredients>\w+\s(\w+\s)+)\(contains(?P<allergens>(\s\w+\,?)+)"
    match = re.match(patterns, line)
    ingredients = match.group("ingredients").strip().split(" ")
    allergens = match.group("allergens").strip().split(", ")

    return ingredients, set(allergens)


def filter_allergen_self(data):
    # use this when have single allergen incredients
    if len(data) == 1:
        return set(data[0])
    if len(data) == 2:
        return set(data[0]).intersection(set(data[1]))

    prods = [p for p in itertools.product(data, repeat=2) if p[0] != p[1]]

    result = set()

    for prod1,prod2 in prods:
        prod1 = set(prod1)
        prod2 = set(prod2)
        inter = prod1.intersection(prod2)
        if not result:
            result = result.union(inter)
        
        else:
            result = result.intersection(inter)

    return result


def driver(f):
    data = []
    raw = f.readlines()
    for line in raw:
        line = line.strip()
        data.append(split_data(line))

    temp_pot = {}
    for ingredients, allergens in data:
        for key in allergens:
            if key not in temp_pot:
                temp_pot[key] = []
            temp_pot[key].append(ingredients)
    potential = {}
    for key in temp_pot:
        if len(temp_pot) > 1:
            
            potential[key] = filter_allergen_self(temp_pot[key])

    for key in potential:
        to_remove = []
        for item in potential[key]:
            for ingredient,allergen in data:
                if key in allergen:
                    if item not in ingredient:
                        to_remove.append(item)
        for r in to_remove:
            potential[key].discard(r)
    not_allergens = []
    for ingredients, allergens in data:
        for item in ingredients:
            is_ok = True
            for key in potential:
                if item in potential[key]:
                    is_ok = False
                    break
            if is_ok:
                not_allergens.append(item)
    all_one = False

    while not all_one:
        to_remove = []
        all_one = True
        for key, value in potential.items():
            if len(value) == 1:
                to_remove.append(list(value)[0])
        for r in to_remove:
            for key in potential:
                value = potential[key]
                if r in value and len(value) > 1:
                    value.discard(r)
                    
        for value in potential.values():
            if len(value) > 1:
                all_one = False

    print(len(not_allergens))
    print(potential)                
    temp = sorted(list(potential.keys()))
    print(",".join(list(potential[key])[0] for key in temp))


def main():
    # For thing that is known to have allergen
    with open("input") as f:
        driver(f)


if __name__ == "__main__":
    main()

