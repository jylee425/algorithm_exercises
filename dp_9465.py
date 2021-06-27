t = int(input())

for _ in range(t):
    n = int(input())
    
    dp = [ [0 for _ in range(n)] for _ in range(2)]
    
    arr = []
    for __ in range(2):
        arr.append(list(map(int,input().split())))
    
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    for i in range(1, n):
        dp[0][i] = max(arr[0][i] + dp[1][i-1], dp[0][i-1])
        dp[1][i] = max(arr[1][i] + dp[0][i-1], dp[1][i-1])
    
    print(max(dp[0][-1], dp[1][-1]))