def compute_convolution(input_matrix, kernel):
    """
    output[i][j] = sum_{u=0}^{K-1} sum_{v=0}^{K-1} input[i+u][j+v] * kernel[u][v]
    """
    H, W = len(input_matrix), len(input_matrix[0])
    K, L = len(kernel), len(kernel[0])

    out_h, out_w = H - K + 1, W - L + 1
    output = [[0 for _ in range(out_w)] for _ in range(out_h)]

    for i in range(out_h):
        for j in range(out_w):
            for u in range(K):
                for v in range(L):
                    output[i][j] += input_matrix[i + u][j + v] * kernel[u][v]

    return output


input_matrix = [
    [1, 2, 3, 4, 5],
    [5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
]
kernel = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]

res = compute_convolution(input_matrix, kernel)
assert res[0][0] == 26
assert res[0][1] == 27
assert res[0][2] == 28
assert res[1][0] == 28
assert res[1][1] == 27
assert res[1][2] == 26
assert res[2][0] == 24
assert res[2][1] == 23
assert res[2][2] == 22

print("PASSED ALL TESTS")
