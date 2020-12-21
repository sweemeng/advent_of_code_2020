import re
import copy
import functools

TOP = 0
BOTTOM = 1
LEFT = 2
RIGHT = 3

HORIZONTAL = 1
VERTICLE = 2


OPPOSITE = {
      TOP: BOTTOM,
      LEFT: RIGHT,
      BOTTOM: TOP,
      RIGHT: LEFT,
    }


def get_image_corners(vectors):
    xes = [x for x,_ in vectors.keys()]
    yes = [y for _,y in vectors.keys()]
    max_x = max(xes)
    max_y = max(yes)
    min_x = min(xes)
    min_y = min(yes)
    return {
        TOP: [(min_x, max_y), (max_x, max_y)],
        BOTTOM: [(min_x,min_y), (max_x, min_y)],
        LEFT: [(min_x, min_y), (min_x, max_y)],
        RIGHT: [(max_x, min_y), (max_x, max_y)],
    }


def get_edge(vectors, direction):
    corners = get_image_corners(vectors)
    corner = corners[direction]
    result = []
    x1,y1 = corner[0]
    x2,y2 = corner[1]
    if x1 == x2 and y1 != y2:
        points = [(x1,y) for y in range(y1,y2+1)]
    elif x1 != x2 and y1 == y2:
        points = [(x,y1) for x in range(x1,x2+1)]
    else:
        points = list(zip(range(x1,x2+1),range(y1,y2+1)))
    edges = [vectors[(x,y)] for x,y in points]
    return edges


def match_edge(source, target, direction):
    match_with = {
      TOP: BOTTOM,
      LEFT: RIGHT,
      BOTTOM: TOP,
      RIGHT: LEFT,
    }
    source_edges = get_edge(source, direction)
    target_edges = get_edge(target, match_with[direction])

    return source_edges == target_edges


class ImageMaps:
    def __init__(self):
        self.parent_shape = [] # assume multiple orientation
        self.child_shapes = {TOP: [], BOTTOM: [], LEFT: [], RIGHT: []}
        self.parent_id = None
        self.child_ids = {TOP: [], BOTTOM: [], LEFT: [], RIGHT: []}

def connect_vectors(vectors):
    cache = {}
    result = {}
    tiles = {}
    count = 0
    for src_key in vectors:       
        for tgt_key in vectors:
            count += 1
            if src_key == tgt_key:
                continue
            found = False
            for src in get_vector_permutations(vectors, src_key, cache):
                for tgt in get_vector_permutations(vectors, tgt_key, cache):
                    match, direction = match_all(src, tgt)
                    if match:
                        #cache[src_key] = src
                        #cache[tgt_key] = tgt
                        if src_key not in result:
                            result[src_key] = set()
                        if tgt_key not in result:
                            result[tgt_key] = set()
                        result[src_key].add(tgt_key)
                        result[tgt_key].add(src_key)
                        found = True
                        if src_key not in tiles:
                            tiles[src_key] = ImageMaps()
                            tiles[src_key].parent_id = src_key
                        parent_shape = tiles[src_key].parent_shape
                        if not in_vector_list(parent_shape, src):
                            parent_shape.append(src)
                        
                        child_shapes = tiles[src_key].child_shapes[direction]
                        if not in_vector_list(child_shapes, tgt):
                            tiles[src_key].child_ids[direction].append(tgt_key)
                            child_shapes.append(tgt)
    return result, tiles


def in_vector_list(source, target):
    result = False
    for item in source:
        if vector_equal(item, target):
            result = True
            break
    return result
        

def vector_equal(source, target):
    
    source_key = source.keys()
    target_key = target.keys()
    if len(source_key) != len(target_key):
        print("not equal length")
        return False
    source_key = list(source_key)
    target_key = list(target_key)
    for ptr in range(len(source_key)):
        if source[source_key[ptr]] != target[target_key[ptr]]:
            return False
    return True


def get_vector_permutations(vectors, key, cache):
    if key in cache:
        yield cache[key]

    else:
        yield from manipulate_vector(vectors[key])


def match_all(source, target):
    found = False
    direction = None
    for direction in (TOP, BOTTOM, LEFT, RIGHT):
        match = match_edge(source, target, direction)
        if match:
            found = True
            break
    return found, direction
        

def manipulate_vector(vector):
    hflip = functools.partial(flip, direction=HORIZONTAL)
    vflip = functools.partial(flip, direction=VERTICLE)
    ops = [None, rotate_vectors, rotate_vectors, rotate_vectors]
    subops = [None, hflip, vflip]
    cp = copy.deepcopy(vector)
    for op in ops:
        for subop in subops:
            if op:
                cp = op(vector)
            if subop:
                cp = subop(vector)
            yield cp



def vectorize_image(image):
    results = {}
    # image is square
    mid = int(len(image) / 2)
    
    for y, row in enumerate(image):
        for x, pixel in enumerate(row):
            # because vector maths is easier if midpoint is 0,0
            results[x-mid, mid-y] = pixel

    return results


def rotate_vectors(vectors):
    # it turn 90 degree
    rotation = [0,-1,1,0]
    change = {}
    for x,y in vectors:
        # The formula for this is https://en.wikipedia.org/wiki/Rotation_matrix#Common_rotations
        dx = y * -1
        dy = x * 1 
        change[(dx,dy)] = vectors[(x,y)]
    return change


def flip(vectors,direction):
    change = {}
    if direction == HORIZONTAL:
        dx, dy = -1, 1
    elif direction == VERTICLE:
        dx, dy = 1, -1
    for x,y in vectors:
        change[(x*dx, y*dy)] = vectors[(x,y)]
    return change


def vectorize_tiles(tiles):
    results = {}
    for tile, image in tiles.items():
        results[tile] = vectorize_image(image)
    return results


def generate_tiles(raw):
    tiles = {}
    current_key = 0
    for line in raw:
        line = line.rstrip()
        if not line:
            continue

        if re.match(r"^Tile", line):
            temp = line[:-1].split(" ")
            current_key = int(temp[1])
            tiles[current_key] = []
        else:
            tiles[current_key].append(line)
    return tiles


def print_vector(vectors):
    temp = {}
    result = []
    for x,y in vectors:
        if y not in temp:
            temp[y] = {}
        temp[y][x] = vectors[(x,y)]
    for y in sorted(temp.keys()):
        row_keys = sorted(temp[y].keys())

        result.insert(0,"".join([temp[y][key] for key in row_keys]))
    for i in result:
        print(i)
    return result
        
    


def main():
    with open("input") as f:
        raw = f.readlines()
    tiles = generate_tiles(raw)
    vectors = vectorize_tiles(tiles)
    result_1, image_tiles = connect_vectors(vectors)
    for k in result_1:
        if len(result_1[k]) == 2:
            print(k)

    for tile_id in image_tiles:
        tile = image_tiles[tile_id]
        if not tile.child[TOP] and not tile.child[LEFT]:
            pass

  
    

if __name__ == "__main__":
    main()
