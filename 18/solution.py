add = lambda x,y: x+y
mul = lambda x,y: x*y 
ops_func = {"+": add, "*": mul}

def calculator_one(formula):
    ops = []
    nums = []
    ops_token = {"+": add, "*": mul}
    # list have no push now. i decide head is index 0. Pop pop from the end
    for c in formula:
        print(c, nums, ops)
        if c.isdigit():
            if not nums:
                nums.insert(0, c)
            else:
                if nums[0] == "(":
                    nums.insert(0, c)
                else:
                    op = ops.pop(0)
                    x = int(c)
                    y = int(nums.pop(0))
                    v = ops_token[op](x,y)
                    nums.insert(0,v)
        elif c == "(":
            nums.insert(0,c)
        elif c == ")":
            y = int(nums.pop(0))
            nums.pop(0) # remove (
            if ops:
                if nums[0] != "(":
                    op = ops.pop(0) 
                    x = int(nums.pop(0))
                    v = ops_token[op](x,y)
                    nums.insert(0,v)
                else:
                    nums.insert(0, y)
            else:
                nums.insert(0,y)
        elif c in ["+","*"]:
            
            ops.insert(0,c)

    return nums[0]
            

def stack_generator(formula):
    ops = []
    nums = []
    ops_tokens = ["*","+"]
    for c in formula:
        print(c, formula, ops, nums)
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
                    pres_1 = ops_tokens.index(c)
                    pres_2 = ops_tokens.index(ops[0])
                    if pres_1 > pres_2:
                        ops.insert(0, c)
                    else:
                        temp = ops.pop(0)
                        nums.append(temp)
                        ops.insert(0, c)
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
    ops_tokens = ["*","+"]
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
        result = calculator_one(i)
        count += result
    print(f"result one: {count}")

    count_2 = 0
    for i in data:
        stack = stack_generator(i)
        count_2 += stack_calculator(stack)
    print(f"result two: {count_2}")


if __name__ == "__main__":
    main()
