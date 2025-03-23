if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    dp = [0 for _ in range(N)]

    dp_max = 0
    for i, arr_i in enumerate(arr):
        dp_i = 1

        for j, arr_j in enumerate(arr[:i]):
            if arr_i > arr[j] and dp[j] >= dp_i:
                dp_i = dp[j] + 1

        dp[i] = dp_i

        if dp[i] > dp_max:
            dp_max = dp[i]

    print(dp_max)
