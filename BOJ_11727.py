
def dp(N):
    '''
    dp[n] = dp[n-2] * 2 + dp[n-1]
    '''
    memo = [0] * (N+1)
    memo[0] = 1
    memo[1] = 3

    for i in range(2, N):
        memo[i] = memo[i-2] * 2 + memo[i-1]
        memo[i] = memo[i] % 10007
    print(memo[N-1])
    return

if __name__ == '__main__':
    N = int(input())
    dp(N)
