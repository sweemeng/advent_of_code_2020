def process(collections, down, right):
    ptr = 0
    row = 0
    tree_count = 0
    for item in collections:
        
        if row % down:
            row = row + 1
            continue
            
        item = item.rstrip()
        if ptr >= len(item):
            ptr = ptr - len(item)
        if item[ptr] == "#":
            tree_count = tree_count + 1
        ptr = ptr + right
        row = row + 1
    return tree_count


def main():
    
    with open("input") as f:
        inputs = f.readlines()
    
    result_2 = process(inputs, 1, 3)
    print(f"First result: {result_2}")
    result_1 = process(inputs, 1, 1)
    result_3 = process(inputs, 1, 5)
    result_4 = process(inputs, 1, 7)
    result_5 = process(inputs, 2, 1)
    final = result_1 * result_2 * result_3 * result_4 * result_5
    print(f"second result: {final}")
    

if __name__ == "__main__":
    main()
