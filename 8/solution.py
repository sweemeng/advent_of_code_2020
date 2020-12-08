class Machine(object):
    def __init__(self, data=[]):
        self.accumulator = 0
        self.ptr = 0
        self.data = data

    def acc(self, amount):
        self.accumulator += amount
        self.ptr += 1

    def jmp(self, amount):
        self.ptr = self.ptr + amount

    def nop(self, amount):
        self.ptr += 1

    def load_code(self, codes):
        for code in codes:
            code = code.rstrip()
            ops, amt = code.split(" ")
            amt = int(amt)
            self.data.append((ops, amt))


def runner(codes):
    logs = []
    # on my computer, when not set data=[]. data attribute will not be empty. 
    machine = Machine(data=[])
    machine.load_code(codes)

    ptr = machine.ptr
    while ptr < len(machine.data):
        ops, amount = machine.data[ptr]

        if (ptr, ops, amount) in logs:
            break
        logs.append((ptr, ops, amount))
        getattr(machine, ops)(amount)
        ptr = machine.ptr

    return logs, machine


def main():
    codes = []
    with open("input") as f:
        codes = f.readlines()

    logs, machine = runner(codes)
    print(f"Solution 1, {machine.accumulator}")

    for i in range(len(logs) -1, -1, -1):
        ptr, ops, amount = logs[i]
        if ops == "nop":
            new_ops = "jmp"
        elif ops == "jmp":
            new_ops = "nop"
        else:
            continue
        editted_codes = codes
        editted_codes[ptr] = editted_codes[ptr].replace(ops, new_ops)
        _, new_machine = runner(editted_codes)
        if new_machine.ptr >= len(new_machine.data):
            print(f"Solution 2, {new_machine.accumulator}")
            break


if __name__ == "__main__":
    main()
