from queue import PriorityQueue

if __name__ == "__main__":
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    res = []
    bucket = PriorityQueue(maxsize=K)
    for i, n in enumerate(numbers):
        if i < K:
            bucket.put(n)
            continue

        m = bucket.get()
        if m > n:
            bucket.put(m)
            res.append(n)
        else:
            bucket.put(n)
            res.append(m)
    while(not bucket.empty()):
        res.append(bucket.get())

    for i in res:
        print(i, end=" ")