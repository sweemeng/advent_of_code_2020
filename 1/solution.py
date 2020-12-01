def main():
    f = open("input")
    l = f.readlines()
    l = [int(i) for i in l]
    l = sorted(l)
    solution(l)
    for idx in range(len(l)):
        result = solution(l, idx+1, l[idx])
        if result:
            break


def solution(l, s=0, f=0):
    for i in range(s, len(l)):
        t = 2020 - l[i] - f
        if t < 0:
            break
        if t in l:
            if not f:
                ans = l[i] * t
                print(f"pair is {l[i]}, {t} answer is {ans}")
                return l[i], t, ans
            else:
                ans = l[i] * f * t 
                print(f"triplet is {l[i]}, {f}, {t} answer is {ans}")
                return l[i], t, ans
    return None


if __name__ == "__main__":
    main()
