
def dp(N, Pi):
    memo = [0 for _ in range(N+1)]
    
    for i in range(1, N+1):
        for j in range(0, i):
            # print(j, i-j, memo[j], Pi[i-j], memo[i])
            memo[i] = max(memo[j] + Pi[i-j], memo[i])
        # print('**', i, memo[i])
            
    print(memo[N])
    return

if __name__ == '__main__':
    N = int(input())
    Pi = [0] + list(map(int, input().split()))

    dp(N, Pi)
