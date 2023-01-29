
def dp(N):
    '''
    dp[n] = dp[n//2]+1 or dp[n//3]+1 or dp[n-1]+1
    '''
    memo = [1e10] * (N+3)
    memo[1] = 0
    memo[2] = 1
    memo[3] = 1

    for i in range(4, N+1):
        if i % 3 == 0:
            memo[i] = min(memo[i], memo[i//3] + 1)
        if i % 2 == 0:
            memo[i] = min(memo[i], memo[i//2] + 1)

        memo[i] = min(memo[i], memo[i-1] + 1)
    
    print(memo[N])
    return


if __name__ == '__main__':
    N = int(input())
    dp(N)
