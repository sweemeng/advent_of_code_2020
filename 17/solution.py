from itertools import product
import copy


def get_next_point(tuples):
    x,dx = tuples
    return x+dx


def get_neighbor(ptr, maps, dimension=3):
    neighbors = []
    prod = product([-1,0,1], repeat=dimension)
    neighbor_const = [p for p in prod if p != tuple([0]*dimension)]
    for tuples  in neighbor_const:
        nptr = tuple(map(get_next_point, zip(ptr,tuples)))
        neighbors.append(maps.get(nptr, "."))
    return neighbors


def make_maps(data,dimension=3):
    z = 0
    w = 0
    padding = dimension - 2 # because 2 is taken by the existing 2 d
    maps = {}
    for x, line in enumerate(data):
        items = list(line)
        mid = int(len(items) / 2) # We will square it better
        for y, value in enumerate(items):
            key = [x-mid, y-mid]
            key = key + [0] * padding
            maps[tuple(key)] = value
            
    return maps


def run(maps, length, iteration=6, dimension=3):
    local_maps = copy.deepcopy(maps)
    # grow the map
    for i in range(iteration):
        local_maps = set_map(local_maps, length, dimension=dimension)
        length += 1
    return local_maps


def set_map(maps, length, dimension=3):
    length += 1
    begin = -1 * length
    end = length + 1
    local_maps = copy.deepcopy(maps)
    count = 0
    for tuples in product(range(begin,end),repeat=dimension):
        count = count+1
        neighbors = get_neighbor(tuples, maps, dimension=dimension)
        status = maps.get(tuples,".")    
        local_maps[tuples] = set_status(status,neighbors)
    return local_maps


def set_status(current, neighbors):
    actives = [i for i in neighbors if i == "#"]
    active_count = len(actives)
    if current == "#":
        if active_count == 2 or active_count == 3:
            return current
        return "."
    if active_count == 3:
        return "#"
    return current


def local_main():
    s = """.#.
..#
###
"""
    data = s.split("\n")
    data = [i for i in data if i]
    length = len(data)
    maps = make_maps(data)
    result = run(maps, length)
        

def main():
    with open("input") as f:
        data=f.read()

    data = data.split("\n")
    data = data[:-1]

    length = len(data) 
    length = int(length / 2) + 1
    maps = make_maps(data)
    output_1 = run(maps, length)
    results = len([i for i in output_1.values() if i == "#"])
    print(f"Result 1: {results}")
    maps_4d = make_maps(data, dimension=4)
    output_2 = run(maps_4d, length, dimension=4)
    results_2 = len([i for i in output_2.values() if i == "#"])
    print(f"Result 2: {results_2}")
    


if __name__ == "__main__":
    main()
