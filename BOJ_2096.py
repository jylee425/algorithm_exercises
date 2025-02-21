import copy

if __name__ == "__main__":
    N = int(input())
    board = list(map(int, input().split()))

    DP_max, DP_min = copy.deepcopy(board), copy.deepcopy(board)
    for i in range(1, N, 1):
        board = list(map(int, input().split()))

        # max
        max_01 = max(DP_max[0], DP_max[1])
        max_12 = max(DP_max[1], DP_max[2])
        max_012 = max(max_01, max_12)

        DP_max[0] = board[0] + max_01
        DP_max[1] = board[1] + max_012
        DP_max[2] = board[2] + max_12

        # min
        min_01 = min(DP_min[0], DP_min[1])
        min_12 = min(DP_min[1], DP_min[2])
        min_012 = min(min_01, min_12)

        DP_min[0] = board[0] + min_01
        DP_min[1] = board[1] + min_012
        DP_min[2] = board[2] + min_12

    max_01 = max(DP_max[0], DP_max[1])
    max_12 = max(DP_max[1], DP_max[2])
    max_012 = max(max_01, max_12)
    min_01 = min(DP_min[0], DP_min[1])
    min_12 = min(DP_min[1], DP_min[2])
    min_012 = min(min_01, min_12)

    print(max_012, min_012)
