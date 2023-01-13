
def dp(N, arr):
    """
    memo[i] = max(arr[i], memo[i-1] + arr[i])
    """
    res = arr[0]
    memo = [arr[i] for i in range(N)]

    for i in range(1, N):
        memo[i] = max(memo[i], memo[i-1]+memo[i])

        res = max(res, memo[i])
    print(res)

    return

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int,input().split()))

    dp(N, arr)
