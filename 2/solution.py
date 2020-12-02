def process(input_str):
    first = 0
    second = 0
    ptr = 0
    check = ""
    buff = ""
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
                yield first, second, check, ptr, item

def main():
    with open("input") as f:
        password_count_1 = 0
        password_count_2 = 0
        for i in f:
            char_count = 0
            check_1 = False
            check_2 = False
            for j in process(i):
                first, second, check, ptr, item = j
                if item == check:
                    char_count = char_count + 1
                if ptr == first:
                    check_1 = check == item
                if ptr == second:
                    check_2 = check == item
            if char_count >= first and char_count <= second:
                password_count_1 = password_count_1 + 1
            if check_1 != check_2:
                password_count_2 = password_count_2 + 1
        print(f"first count: {password_count_1}, second count: {password_count_2}")

if __name__ == "__main__":
    main()
