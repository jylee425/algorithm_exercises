import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    M = int(input())

    dp = [[float("inf")] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        dp[a][b] = min(dp[a][b], c)

    for _ in range(1, N + 1):
        dp[_][_] = 0

    # floyd-warshall algorithm
    while True:
        update = False

        for k in range(1, N + 1):
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    if dp[i][j] > dp[i][k] + dp[k][j]:
                        dp[i][j] = dp[i][k] + dp[k][j]
                        update = True

        if not update:
            break

    # print
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dp[i][j] == float("inf"):
                print(0, end=" ")
            else:
                print(dp[i][j], end=" ")
        print()
