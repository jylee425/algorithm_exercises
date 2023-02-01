
def dp(N):
    '''
    dp[i] = min(dp[i - j]) + 1
    '''
    memo = [100000] * (N+2)
    square = [i * i for i in range(int(100000 ** 0.5))]

    memo[0] = 0
    memo[1] = 1

    for i in range(1, N+1):
        for j in square:
            if j > i: break
            memo[i] = min(memo[i], memo[i-j])
        memo[i] += 1

    print(memo[N])
    return
                


if __name__ == '__main__':
    N = int(input())
    dp(N)
