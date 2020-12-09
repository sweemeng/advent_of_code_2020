def process(data, pos, window_size):
    end = pos 
    start = end - window_size
    window = data[start:end]
    for i in window:
        temp = data[pos] - i
        if temp in window:
            return True
    return False


def main():
    data = []
    with open("input") as f:
        data = [int(i) for i in f.readlines()]
    window_size = 25
    ptr = 25
    bad_number = 0
    while ptr <= len(data):
        if not process(data, ptr, window_size):
            bad_number = data[ptr]
            print(f"First not valid number is {data[ptr]}")
            break
        ptr += 1
    
    ptr = 0
    while ptr <= len(data):
        total = data[ptr]
        next_ptr = ptr + 1
        while total < bad_number:
            total = total + data[next_ptr]
            next_ptr += 1
        if total == bad_number:
            # the above loop will always go one step ahead
            print(f"value found at between {ptr} and {next_ptr-1}")
            sublist = data[ptr:next_ptr]
            print(sublist)
            print(f"checking {sum(sublist)}")
            min_item = min(sublist)
            max_item = max(sublist)
            result = max_item + min_item
            print(f"min is {min_item}, max is {max_item}")
            print(f"result is {result}")
            break 
        ptr += 1


if __name__ == "__main__":
    main()
