
def dp(N):
    """
    memo[i] = memo[i-2] * 3 + memo[i-4] * 2 + memo[i-6] * 2 + memo[i-8] * 2 + ... (3 for i-2, and 2 for others)
    """
    if N % 2 == 1 or N == 0:
        return 0

    if N == 2:
        return 3

    memo = [0,0,3] + [0 for _ in range(N)]
    helper = 0
    for i in range(4, N+2, 2):
        memo[i] += memo[i-2] * 3
        memo[i] += helper * 2
        memo[i] += 2

        helper += memo[i-2]
    return memo[N]

if __name__ == '__main__':
    N = int(input())

    print(dp(N))
