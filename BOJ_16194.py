
def dp(N, Pi):
    memo = [False for _ in range(N+1)]

    for i in range(1, N+1):
        for k in range(1, i+1):
            tmp = memo[i-k] + Pi[k]
            if memo[i] == False: memo[i] = tmp
            else: memo[i] = min(memo[i], tmp)

    print(memo[N])
    return

if __name__ == '__main__':
    N = int(input())
    Pi = [0] + list(map(int,input().split()))
    dp(N, Pi)
    
