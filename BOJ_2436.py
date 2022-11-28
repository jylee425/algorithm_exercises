
def has_common_divisor(A, B):
    sqrt_M = int(min(A, B) ** 0.5)
    for i in range(2, sqrt_M + 1):
        if A % i == 0 and B % i == 0:
            return True
    return False

def dp(M):
    """
    Return:
        A pair of numbers making M,
        multiplication of them are M
        and they don't have common divisor
        and their sum should be minimum
    """
    possible = []

    sqrt_M = int(M ** 0.5)
    for i in range(2, sqrt_M+1):
        if M % i == 0 and not has_common_divisor(i, M//i):
            possible.append((i, M//i))

    if len(possible) == 0:
        return (1, M)

    sum_max = M+1
    res = (-1, -1)
    for (A, B) in possible:
        if sum_max > A + B:
            res = (A, B)
    return res

if __name__ == "__main__":
    gcd, lcd = map(int, input().split())
    (A, B) = dp(lcd // gcd)

    print(gcd * A, gcd * B)
    
