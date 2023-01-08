
def dp(arr):
    N = len(arr)
    memo = [1] * N

    res = 0
    for i in range(N):
        for j in range(i):
            if arr[i] < arr[j]:
                memo[i] = max(memo[j]+ 1, memo[i])
        res = max(res, memo[i])

    return res

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))

    print(dp(arr))

