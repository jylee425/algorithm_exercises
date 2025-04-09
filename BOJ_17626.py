if __name__ == "__main__":
    N = int(input())

    dp = [0 for _ in range(N + 1)]
    dp[1], dp[2], dp[3], dp[4] = 1, 2, 3, 1
    for i in range(5, N + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(2, int(i**0.5) + 1):
            dp[i] = min(dp[i], dp[i - j * j] + 1)

    print(dp[N])
