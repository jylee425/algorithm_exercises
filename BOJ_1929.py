
def greedy(N, M):
    """
    Return:
        array of prime numbers < M
    """
    dp = [1] + [0] * M

    maximum = int((M+1) ** 0.5)
    for i in range(2, maximum*2):
        if dp[i] == 0:
            for j in range(i**2, M+1):
                if j % i == 0:
                    dp[j] = 1
   
    res = []
    for i in range(N, M+1):
        if i > 1 and dp[i] == 0:
            res.append(i)
        
    return res

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = greedy(N, M)

    # print(len(arr))
    for a in arr:
        print(a)
