add = lambda x,y: x+y
mul = lambda x,y: x*y 
ops_func = {"+": add, "*": mul}
ops_tokens = ["*","+"]


# equal_ops can be just a dict of operation with precedent score
def stack_generator(formula, equal_ops=False):
    ops = []
    nums = []
    for c in formula:
        if c.isdigit():
            nums.append(int(c))
        elif c in ops_tokens:
            if ops:
                if c == ops[0]:
                    # because there is only * and + dont need to pop from ops
                    nums.append(c)
                elif ops[0] == "(":
                    ops.insert(0,c)
                else:
                    if not equal_ops:
                        pres_1 = ops_tokens.index(c)
                        pres_2 = ops_tokens.index(ops[0])
                        if pres_1 > pres_2:
                            ops.insert(0, c)
                        else:
                            temp = ops.pop(0)
                            nums.append(temp)
                            ops.insert(0, c)
                    else:
                        temp = ops.pop(0)
                        nums.append(temp)
                        ops.insert(0,c)
            else:
                ops.insert(0, c)
        elif c == "(":
            ops.insert(0,c)
        elif c == ")":
            if ops:
                head = ops[0]
                while head != "(":
                    temp = ops.pop(0)
                    nums.append(temp)
                    head = ops[0]
                ops.pop(0)

    return nums + ops
            

def stack_calculator(stack):
    result_stack = []
    for i in stack:
        if i in ops_tokens:
            x = result_stack.pop(0)
            y = result_stack.pop(0)
            v = ops_func[i](x, y)
            result_stack.insert(0, v)
        else:
            result_stack.insert(0,i)
    return result_stack[0]
             

def main():
    with open("input") as f:
        data = f.readlines()

    count = 0
    for i in data:
        stack = stack_generator(i, equal_ops=True)
        count += stack_calculator(stack)
    print(f"result one: {count}")

    count_2 = 0
    for i in data:
        stack = stack_generator(i)
        count_2 += stack_calculator(stack)
    print(f"result two: {count_2}")


if __name__ == "__main__":
    main()
