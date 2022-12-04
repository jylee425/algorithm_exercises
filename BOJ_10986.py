
def prefix_sum(A, M):
    """
    Args:
        A: array of numbers divided by M
        M: divisor
    Return:
        number of pairs making Sij devisible by M
    """
    N = len(A)
    remainder = [0] * M
    cnt = 0

    S = [0]
    for i in range(N):
        tmp = (S[-1] + A[i]) % M
        S.append(tmp)
        remainder[tmp] += 1

    # index from r (index i) to r (index j)
    # is where Sij is divisble by M
    # so, count rC2
    for r in remainder:
        cnt += r * (r-1) // 2 

    # remainder[0] is where the single element is div. by M
    cnt += remainder[0]
    return cnt

if __name__ == "__main__":
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    print(prefix_sum(A, M))

