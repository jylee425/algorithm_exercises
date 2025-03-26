if __name__ == "__main__":
    N, K = map(int, input().split())

    items = [(0, 0)]
    for _ in range(N):
        W, V = map(int, input().split())
        items.append((W, V))
    items.sort(key=lambda x: x[0])  # sort by weight

    # dp
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for k in range(1, K + 1):
            weight, value = items[i]

            if k < weight:
                dp[i][k] = dp[i - 1][k]
            else:
                dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - weight] + value)

        # print(dp[i])

    print(dp[N][K])
