def generator(starting):
    memory = {}
    
    # because only programmer start from 0
    for i,v in enumerate(starting):
        memory[v] = i + 1
        yield v
    n = i + 2
    v = 0

    while True:
        yield v
        if v in memory:
            next_v = n - memory[v]
        else:
            next_v = 0
        memory[v] = n
        n += 1
        v = next_v


def main():
    series = generator([9,12,1,4,17,0,18])
    
    answer_1 = 0
    for j in range(2020):
        answer_1 = next(series)

    # Reinit the iterator. but reassign problably work well enough
    series.close()
    series = generator([9,12,1,4,17,0,18])
    answer_2 = 0
    for j in range(30000000):
        answer_2 = next(series)

if __name__ == "__main__":
    main()
