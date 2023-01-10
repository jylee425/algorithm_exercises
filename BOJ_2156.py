
def dp(N):
    res = 0

    if N < 3:
        for i in range(N):
            res += int(input())
    elif N == 3:
        arr = []
        for i in range(N):
            arr.append(int(input()))

        res = max(arr[0]+arr[1], max(arr[0]+arr[2], arr[1]+arr[2]))
    else:
        memo = [[0] * 5 for _ in range(N)]
        
        # i = 0
        n = int(input())
        # memo[0][0], memo[0][1], memo[0][2], memo[0][3], memo[0][4] =\
        #         n, n, 0, n, 0
        
        # i = 1
        m = int(input())
        # memo[1][0], memo[1][1], memo[1][2], memo[1][3], memo[1][4] =\
        #         memo[0][0], memo[0][1]+n, 0, memo[0][3], n

        # i = 2
        k = int(input())
        memo[2][0], memo[2][1], memo[2][2], memo[2][3], memo[2][4] =\
                n, n+m, k, n+k, m+k

        # i >= 3
        for i in range(3, N):
            n = int(input())

            memo[i][0] = memo[i-1][1]
            memo[i][1] = memo[i-1][4]
            memo[i][2] = memo[i-1][0] + n
            memo[i][3] = memo[i-1][1] + n
            memo[i][4] = memo[i-1][2] + memo[i-1][3] + n

        for ii in range(5):
            res = max(res, memo[-1][ii])
    print(res)

    return

if __name__ == '__main__':
    N = int(input())
    dp(N)
