MAX = 1001

def dp(N, A):
    memo = [MAX for _ in range(N)]

    memo[0] = 0
    for i in range(N):
        Ai = A[i]
        for a in range(1, Ai+1):
            if i + a < N:
                memo[i + a] = min(memo[i + a], memo[i] + 1)

    if memo[N-1] != MAX:
        print(memo[N-1])
    else:
        print(-1)
    return

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    dp(N, A)
