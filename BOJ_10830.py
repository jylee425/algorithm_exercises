import copy

def apply_1000(a):
    return a % 1000

def matmul(A, B):
    """
        c_ij = sum_k (a_ik * b_kj)
    """
    C = []

    N = len(A)
    for i in range(N):
        c_i = []
        for j in range(N):
            c_ij = 0
            for k in range(N):
                c_ij += A[i][k] * B[k][j]
            c_ij %= 1000
            c_i.append(c_ij)
        C.append(c_i) 
    return C

def divide(matrix, B):
    """
        B // 2
    """
    if B == 1:
        return matrix
    
    tmp = divide(matrix, B//2)
    if B % 2 == 0:
        return matmul(tmp, tmp)
    else:
        return matmul(matmul(tmp, tmp), matrix)

if __name__ == "__main__":
    matrix = []
    N, B = list(map(int, input().split()))
    for _ in range(N):
        matrix.append(list(map(apply_1000, map(int, input().split()))))

    # res = [[1, 0], [0, 1]]
    # for _ in range(B):
    #     print(res)
    #     res = copy.deepcopy(matmul(res, matrix))
    # print(res)

    matrix = divide(matrix, B)
    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=" ")
        print()
    exit()
