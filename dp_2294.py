n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

inf = 100001
dp = [inf for _ in range(k+1)]

for i in range(n):
    if (coin[i] > k):
        continue
    dp[coin[i]] = 1

    for j in range(coin[i], k+1):
        dp[j] = min(dp[j], dp[j - coin[i]] + 1)

if dp[k] == inf:
    print(-1)
else:
    print(dp[k])
    