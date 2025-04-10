if __name__ == "__main__":
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]
    times.sort(key=lambda x: (x[1], x[0]))
    # print(times)

    # Greedy
    res = []
    res.append(times[0])
    cur = times[0][1]
    for time in times[1:]:
        if time[0] < cur:
            continue
        res.append(time)
        cur = time[1]

    print(len(res))
