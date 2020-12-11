import copy


def get_adjecent_long(seats, x, y):
    directions = [
        (-1, -1), (-1, 0), (-1, +1),
        (0, -1), (0, +1),
        (+1, -1), (+1, 0), (+1, +1),
    ]
    min_x = 0
    min_y = 0
    max_x = len(seats)
    max_y = len(seats[0])
    results = []
    value = "."
    for d_x, d_y in directions:
        next_x = x + d_x
        next_y = y + d_y
        while True:
            if next_x < min_x or next_x >= max_x:
                break
            if next_y < min_y or next_y >= max_y:
                break
            if seats[next_x][next_y] in ('L', '#'):
                value = seats[next_x][next_y]
                break
            next_x += d_x
            next_y += d_y
        results.append(value)
        value = "."
    return results        


def get_adjecent(seats, x, y):
    adjecent = [
        (x-1, y-1), (x-1, y), (x-1, y+1),
        (x, y-1), (x, y+1),
        (x+1, y-1), (x+1, y), (x+1, y+1),
    ]
    adjecent = [(x, y) for x, y in adjecent if x >= 0 and y >= 0]
    row_length = len(seats)
    col_length = len(seats[x])
    adjecent = [(x, y) for x, y in adjecent if x < row_length and y < col_length]
    adjecent_seat = [ seats[x][y] for x, y in adjecent]
    return adjecent_seat


def get_next_state(seats, x, y, func=get_adjecent, seated_count=4):
    '''
    seats: list
    x: int row of seats
    y: int col of seats
    '''
    status = seats[x][y]

    adjecent_seat = func(seats, x, y)
    seated = list(filter((lambda x: x=="#"), adjecent_seat))
    if status == "L":
        if not seated:
            return "#"
        
    elif status == "#":
        if len(seated) >= seated_count:
            return "L"
    return status


def move_world(data, func=get_adjecent, seated_count=4):
    # x is row y is column
    seats = copy.deepcopy(data) # python list pass by ref, it sucks
    for x in range(len(seats)):
        for y in range(len(seats[0])):
            seats[x][y] = get_next_state(data, x, y, func, seated_count)
    return seats


def main():
    with open("input") as f:
        seats = f.readlines()
        seats = [ list(i) for i in seats ]

    next_seats = []
    curr_seats = copy.deepcopy(seats)

    while True:
        next_seats = move_world(curr_seats)
        if curr_seats != next_seats:
            curr_seats = copy.deepcopy(next_seats)
        else:
            break

    count = 0
    for row in curr_seats:
        empty_seats = list(filter(lambda x: x=='#', row))
        count += len(empty_seats)
    print(f"Empty seats: {count}")


    next_seats = []
    curr_seats = copy.deepcopy(seats)

    while True:
        next_seats = move_world(curr_seats, get_adjecent_long, seated_count=5)
        if curr_seats != next_seats:
            curr_seats = copy.deepcopy(next_seats)
        else:
            break

    count = 0
    for row in curr_seats:
        empty_seats = list(filter(lambda x: x=='#', row))
        count += len(empty_seats)
    print(f"Empty seats: {count}")


if __name__ == "__main__":
    main()

