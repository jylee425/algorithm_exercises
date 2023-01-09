
def dp(N):
    """
    dp[n][0] = dp[n-1][3]
    dp[n][1] = dp[n-1][0] + dp[n-1][2]
    dp[n][2] = dp[n-1][0] + dp[n-1][1]

    dp[n][3] = sum over dp[n][i] (i \in {0,1,2})
    """
    
    memo = [[0] * 4 for _ in range(N+1)]
    
    memo[0][3] = 1
    memo[1][0], memo[1][1], memo[1][2], memo[1][3] = 1, 1, 1, 3
    # memo[2][0], memo[2][0], memo[2][2], memo[2][3] = 3, 2, 2, 7
    for i in range(2, N+1):
        memo[i][0] = memo[i-1][3]
        memo[i][1] = memo[i-1][0] + memo[i-1][2]
        memo[i][2] = memo[i-1][0] + memo[i-1][1]
        memo[i][3] = memo[i][0] + memo[i][1] + memo[i][2]
    print(memo[N][3])

if __name__ == '__main__':
    N = int(input())
    dp(N)
