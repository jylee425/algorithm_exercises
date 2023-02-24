import sys
input = sys.stdin.readline
MOD = 1000000000
ANSWER = (1 << 10) - 1

def dp(N):
    '''
    memo[i][bitmasking]
        i stands for the last digit
        bitmasking to check 0~9 has been used 
    '''
    memo = [[0] * (ANSWER + 1) for _ in range(10)]

    for i in range(1, 10):
        memo[i][1 << i] = 1

    for _ in range(2, N+1):
        tmp = [[0] * (ANSWER + 1) for _ in range(10)]

        for i in range(10):
            for j in range(ANSWER+1):
                if i > 0:
                    tmp[i][j | (1 << i)] = (tmp[i][j | (1 << i)] + memo[i-1][j]) % MOD
                if i < 9:
                    tmp[i][j | (1 << i)] = (tmp[i][j | (1 << i)] + memo[i+1][j]) % MOD
        memo = tmp

    res = 0
    for i in range(10):
        res += memo[i][ANSWER]
    print(res % MOD)
    return

if __name__ == '__main__':
    N = int(input())
    dp(N)
