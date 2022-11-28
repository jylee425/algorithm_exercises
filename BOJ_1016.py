

def greedy(N, M):
    """
    Args:
        numbers are in between [N, M]
    Return:
        Number of numbers that can't be divided by squared number
    """
    cnt = M + 1 - N
    dp = [0] * cnt # divisble by squared number

    sqrt_M = int(M ** 0.5)
    for i in range(2, sqrt_M + 1):
        sq_i = i * i # i * i is faster than i ** 2 

        # The quotient of first divisble number is (N-1)//sq_i + 1
        quotient = ((N-1)//sq_i + 1)
        for j in range(quotient * sq_i, M+1, sq_i):
            if dp[j-N] == 0:
                dp[j-N] = 1
                cnt -= 1
    return cnt 

if __name__ == "__main__":
    N, M = map(int, input().split()) 
    print(greedy(N, M))
