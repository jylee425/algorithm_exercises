
def dp(N, arr):
    res = arr[0]
    memo = arr[:] # sum of LIS up to i-th element

    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                memo[i] = max(memo[j]+arr[i], memo[i])
        res = max(res, memo[i])

    return res 

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))

    print(dp(N, arr))
