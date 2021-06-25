N = int(input())

memo = [0 for _ in range(N+3)]
memo[0] = 1
memo[1] = 2
for n in range(2, N+1):
    memo[n] = memo[n-1] + memo[n-2]
print(memo[N-1] % 10007)