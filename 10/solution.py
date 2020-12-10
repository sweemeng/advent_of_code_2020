from collections import Counter, defaultdict


jolt_ranges = set([1,2,3])


def jolt_diff_dist(data):
    counts = []
    jolt_rate = 0
    data = sorted(data)
    internal_jolt = data[-1] + 3
    data.append(internal_jolt)
    adapters = []
    
    for jolt in data:
        diff = jolt - jolt_rate
        if diff in jolt_ranges:
            adapters.append(jolt)
            counts.append(diff)
            jolt_rate = jolt
        
    return Counter(counts), adapters


def i_stole_this_solution(data):
    jolts = data[:]
    ways = defaultdict(lambda:0)
    ways[0] = 1
    for i in range(1, len(jolts)):
        ways[jolts[i]] = ways[jolts[i]-1] + ways[jolts[i]-2] + ways[jolts[i]-3]
    return ways[jolts[-1]]



def main():
    with open("input") as f:
        data = [int(i) for i in f.readlines()]
    counter, adapters = jolt_diff_dist(data)
    print(f"answer for one is: {counter[3] * counter[1]}")

    new_data = data[:]
    new_data = [0] + new_data
    new_data.append(max(new_data)+3)
    new_data.sort()
    arrangements = i_stole_this_solution(new_data)
    print(f"arrangement is: {arrangements}")


if __name__ == "__main__":
    main()
