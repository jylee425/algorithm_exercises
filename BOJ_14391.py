
def brute_force(N, M, arr):
    """
    use bit-masking

    i \in [0, 2^NM - 1],
        (Note that there should always cut in row or col)
        if digit = 0: there exists cut in col
        elif digit = 1: there exists cut in row
    """
    res = 0

    for i in range(1 << (N*M)):
        total = 0

        # numbers in row-wise arrangement
        for row in range(N):
            rowsum = 0
            for col in range(M):
                idx = row * M + col # current digit

                if i & ( 1 << idx ) != 0: # if i's current digit is 1
                    rowsum = rowsum * 10 + arr[row][col]
                else:
                    total += rowsum
                    rowsum = 0
            total += rowsum

        # numbers in col-wise arrangement
        for col in range(M):
            colsum = 0
            for row in range(N):
                idx = row * M + col # current digit

                if i & ( 1 << idx ) == 0: # if i's current digit is 0
                    colsum = colsum * 10 + arr[row][col]
                else:
                    total += colsum
                    colsum = 0
            total += colsum

        res = max(res, total)
    
    print(res)
    return

if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    brute_force(N, M, arr)
