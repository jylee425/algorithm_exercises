
def dp(N):
    """
    memo[i] = max of { memo[i-1], memo[i-2] + arr[i], memo[i-3] + arr[i-1] + arr[i] }
    """
    res = 0
    arr = [0] + [int(input()) for _ in range(N)]

    if N == 1:
        res = arr[1]
    elif N == 2:
        res = arr[1] + arr[2]
    else:
        memo = [0] + [arr[1]] + [arr[1] + arr[2]] + [0] * (N-2)
        for i in range(3, N+1):
            memo[i] = max(memo[i-1], max(memo[i-2]+arr[i], memo[i-3]+arr[i-1]+arr[i]))
            # print(i, memo)
        res = memo[N] 
    print(res)

    return

if __name__ == '__main__':
    N = int(input())
    dp(N)
