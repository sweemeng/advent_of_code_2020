def solution(items, operation="union"):
    result = set()
    answers = [] 
    new_set = True
    for item in items:
        item = item.rstrip()
        if not item:
            group = []
            answers.append(result)
            result = set()
            new_set = True
        else:
            if new_set:
                result = set(item)
            else:
                result = getattr(result, operation)(set(item))
            new_set = False
    answers.append(result)
    return answers


def main():
    f = open("input")
    data = f.readlines()
    outputs = solution(data)
    total = sum([len(i) for i in outputs])
    print(f"Solution for 1 is {total}")
    outputs = solution(data, operation='intersection')
    total = sum([len(i) for i in outputs])
    print(f"solution for 2 is {total}")

    

if __name__ == "__main__":
    main()
