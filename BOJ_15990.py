import sys

input = sys.stdin.readline

def dp(memo):
    """
        memo[N] = [case ending with 1, case ending with 2, case ending with 3]

        memo[i][0] = memo[i-1][1] + memo[i-1][2]
        memo[i][1] = memo[i-2][0] + memo[i-2][2]
        memo[i][2] = memo[i-3][0] + memo[i-3][1] 
    """
    memo[1] = [1, 0, 0]
    memo[2] = [0, 1, 0]
    memo[3] = [1, 1, 1]

    for i in range(4, 100001):
        memo[i][0] = (memo[i-1][1] + memo[i-1][2])%1000000009
        memo[i][1] = (memo[i-2][0] + memo[i-2][2])%1000000009
        memo[i][2] = (memo[i-3][0] + memo[i-3][1])%1000000009

    return

def main(K):
    memo=[ [0] * 3 for _ in range(100001) ]
    dp(memo)

    for _ in range(K):
        N = int(input())
        print(sum(memo[N]) % 1000000009)
    return

if __name__ == '__main__':
    K = int(input())
    main(K)

