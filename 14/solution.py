import re
import itertools


def mask_value(value, mask, keep_all=False):
    s=bin(value)[2:]
    s = s.zfill(len(mask))
    result = []
    for i in range(len(mask)):
        if mask[i] == 'X' and not keep_all:
            result.append(s[i])
            continue
        if keep_all:
            if mask[i] == "0":
                result.append(s[i])
                continue
        result.append(mask[i])
    return "".join(result)


def populate_mems(values, version=1):
    mem = {}
    mask_pattern = r"(?P<variable>^mask)(\s\=\s)(?P<mask>\w+)"
    mem_pattern = r"(?P<variable>^mem)\[(?P<address>\d+)\](\s=\s)(?P<value>\d+)"
    mask = ""
    for value in values:
        mask_match = re.search(mask_pattern, value)
        if mask_match:
            mask = mask_match.group("mask")
            continue
        mem_match = re.search(mem_pattern, value)
        if mem_match:
            address = int(mem_match.group("address"))
            value = int(mem_match.group("value"))
            if version == 1:
                mem[address] = int(mask_value(value, mask), base=2)
            else:
                template = mask_value(address, mask, keep_all=True)
                addresses = generate_addresses(template)
                for address in addresses:
                    mem[int(address,base=2)] = value
    return mem


def generate_addresses(template):
    results = []
    pos = [i for i, value in enumerate(template) if value =="X"]
    size = len(pos)
    patterns = [p for p in itertools.product([0,1], repeat=size)]
    for pattern in patterns:
        d = dict(zip(pos, pattern))
        value = list(template)
        for key in d:
            value[key] = str(d[key])
        results.append("".join(value))
    return results

    
def main():
    with open("input") as f:
        inputs = f.readlines()
    mem = populate_mems(inputs)

    print(sum(mem.values())) 
        
    mem_2 = populate_mems(inputs, version=2)
    print(sum(mem_2.values()))

if __name__ == "__main__":
    main()
