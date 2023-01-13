
def main(N, arr):
    """
    memo[0][i]: no deletion
    memo[1][i]: deleting certain element 
    """
    dp = [[0] * N for _ in range(2)]

    dp[0][0] = arr[0]
    
    if N == 1:
        return dp[0][0]

    res = -1e9
    for i in range(1, N):
        dp[0][i] = max(dp[0][i-1]+arr[i], arr[i])
        dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])

        res = max(res, dp[0][i], dp[1][i])
    return res


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))

    print(main(N, arr))
