
def dp(N, arr):
    memo = [0 for _ in range(21)]

    for i in range(N):
        for j in range(i+arr[i][0], N+1):
            memo[j] = max(memo[j], memo[i]+arr[i][1])

    print(memo[N])
    return

if __name__ == '__main__':
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dp(N, arr)
