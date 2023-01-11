
def dp(N, arr):
    """
    dp[j][i] = max { dp[j-1][i-1] + now, dp[j-1][i] + now }
    """
    res = arr[0][0]
    memo = [[0] * N for _ in range(N)]

    memo[0][0] = arr[0][0]
    for j in range(1,N):
        for i in range(j+1):
            memo[j][i] = arr[j][i]

            if i > 0:
                memo[j][i] += max(memo[j-1][i-1], memo[j-1][i])
            else:
                memo[j][i] += memo[j-1][i]

            if j == N-1:
                res = max(res, memo[j][i])

    # for j in range(N):
    #     print(memo[j])

    print(res)
    return

if __name__ == '__main__':
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dp(N, arr)
