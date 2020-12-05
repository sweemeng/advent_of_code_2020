LOWER = 0
UPPER = 1

DIRECTION = {
    "F": LOWER,
    "B": UPPER,
    "L": LOWER,
    "R": UPPER,
}


def partition(input_pair, direction):
    first, last = input_pair
    mid = (last - first) / 2
    if direction == LOWER:
        last = first + mid - .5
        return (first, int(last))
    first = first + mid + .5
    return (int(first), last)


def get_seat(code):
    row = (0, 127)
    column = (0, 7)
    for item in code:
        direction = DIRECTION[item]
        if item == "F" or item == "B":
            row = partition(row, direction)
        elif item == "L" or item == "R":
            column = partition(column, direction)
    return row[0], column[0]


def get_id(code):
    row, column = get_seat(code)
    return row * 8 + column

def main():
    f = open("input")
    results = []
    for i in f:
        i = i.rstrip()
        current_id = get_id(i)
        results.append(current_id)
    max_id = max(results)
    print(f"Max id is {max(results)}")
    results = sorted(results)
    item = results[0]
    while item < max_id:
        item = item + 1
        if item not in results:
            print(item)
        

if __name__ == "__main__":
    main()

