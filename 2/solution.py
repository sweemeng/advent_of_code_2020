def process(input_str):
    min_count = 0
    max_count = 0
    count = 0
    check = ""
    buffer = ""
    data_mode = False
    for item in input_str:
        if item == "-":
            min_count = int(buffer)
            buffer = ""
        elif item == " ":
            if not data_mode:
                max_count = int(buffer)
                buffer = ""
        elif item == ":":
            data_mode = True
        else:
            if not data_mode:
                check = item
                buffer = buffer + item
            else:
                if item == check:
                    count = count + 1

    if count >= min_count and count <= max_count:
        return True
    return False


def process2(input_str):
    first = 0
    second = 0
    count = 0
    ptr = 0
    check = ""
    buff = ""
    valid = False
    check1 = False
    check2 = False
    data_mode = False
    for item in input_str:
        if item == "-":
            first = int(buff)
            buff = ""
        elif item == " ":
            if not data_mode:
                second = int(buff)
                buff = ""
        elif item == ":":
            data_mode = True
        else:
            if not data_mode:
                check = item
                buff = buff + item
            else:
                ptr = ptr + 1
                if ptr == first:
                    check1 = item == check
                if ptr == second:
                    check2 = item == check
    if check1 != check2:
        return True
    return False

def main():
    f = open("input")
    l = f.readlines()
    count = 0
    for i in l:
        if process(i):
            count = count + 1
    
    print("first count:", count)
    count = 0
    for i in l:
        if process2(i):
            count = count + 1
    print("second count:", count)


if __name__ == "__main__":
    main()
