def exchange(n:int, bucket:list):
    '''
    Extract the smallest element
    and put n in the coressponding index
    '''
    k, m = 0, bucket[0]
    for i, li in enumerate(bucket):
        if m > li:
            k, m = i, li
    bucket[k] = n
    return m, bucket, min(bucket)

if __name__ == "__main__":
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    res = []
    bucket, s = [], 1111111111
    for n in numbers:
        # bucket with size of K
        if len(bucket) < K:
            bucket.append(n)
            if s > n: s = n
            continue

        # with full bucket
        if s > n:
            res.append(n)
        else:
            m, bucket, s = exchange(n, bucket)
            res.append(m)
    res += sorted(bucket)

    for i in res:
        print(i, end=" ")