
def dp(N, arr):
    """
    Longest Bitonic Sequence

    LIS in forward & LIS in backward => sum of each i-th will be length of LBS
    """
    memo_fw, memo_bw =\
            [1 for _ in range(N)], [1 for _ in range(N)]
    # print(arr)

    for i in range(1,N):
        for j in range(i+1):
            # forward
            if arr[j] < arr[i]:
                memo_fw[i] = max(memo_fw[i], memo_fw[j] + 1)

            # backward
            if arr[-j-1] < arr[-i-1]:
                memo_bw[-i-1] = max(memo_bw[-i-1], memo_bw[-j-1] + 1)
        # print(arr[i], memo_fw, arr[-i], memo_bw)


    res = 0
    for i in range(N):
        res = max(res, memo_fw[i]+memo_bw[i]-1)
    print(res)

    return


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))

    dp(N, arr)
