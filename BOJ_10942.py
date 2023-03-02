
def dp(N, arr, memo):
    for i in range(N):
        memo[i][i] = 1
        for j in range(i-1, -1, -1):
            if memo[j+1][i-1] or (i+1==j):
               memo[j][i] = 1 
    # print(memo)
    return memo

def main(N, arr):
    memo = [[0] * N for _ in range(N)]
    memo = dp(N, arr, memo)    

    T = int(input())
    for _ in range(T):
        s, e = map(int, input().split())
        print(memo[s-1][e-1])

if __name__ == '__main__':
    N = int(input())
    arr = map(int, input().split())
    main(N, arr)
