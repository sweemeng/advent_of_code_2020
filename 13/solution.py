def main():
    
    with open("input") as f:
        curr_time = int(f.readline())
        busses = f.read().split(",")
    pbusses = [i for i in busses if i != 'x']
    pbusses = [int(i) for i in pbusses]
    next_time = []
    for i in pbusses:
        mod = curr_time % i
        temp = curr_time - mod
        n_time = temp + i
        next_time.append(n_time)
    min_time = min(next_time)
    print(pbusses, next_time, min_time)
    result = pbusses[next_time.index(min_time)] * (min_time - curr_time)
    print(f"result {result}")

    # Stole this solution too
    earliest = 0
    running = 1
    for i in range(len(busses)):
        if busses[i] == "x":
            continue
        # How this work is, we are creating earliest time where the condition is meet. 
        # we know that the mod of time zero, and the time is i minute since the first bus
        # Why do by running, the number move at least at the amount at a time
        while ((earliest + i) % int(busses[i]) != 0):
            earliest += running
        running *= int(busses[i])
    print(earliest)



if __name__ == "__main__":
    main()
    
