
def dp(N, K):
    memo = [[0] * 201 for _ in range(201)]

    memo[0][0] = 1
    for i in range(0, N+1):
        for j in range(1, K+1):
            memo[i][j] = memo[i-1][j] + memo[i][j-1]
    print(memo[N][K] % 1000000000)

    return

if __name__ == '__main__':
    N, K = map(int, input().split())
    dp(N, K)
