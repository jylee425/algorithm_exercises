def helper(N, M, board, target_height, B):
    target_dig, target_fill = 0, 0

    for y in range(N):
        for x in range(M):
            remaining = target_height - board[y][x]

            if remaining < 0:
                target_dig -= remaining
            else:
                target_fill += remaining

    if target_fill > B + target_dig:
        return -1
    else:
        return target_dig * 2 + target_fill


if __name__ == "__main__":
    N, M, B = map(int, input().split())

    board, max_height = [], 0
    for _ in range(N):
        row = list(map(int, input().split()))
        board.append(row)

        row_max_height = max(row)
        if max_height < row_max_height:
            max_height = row_max_height

    res_time, res_height = 999999999, -1
    for target_height in range(max_height, -1, -1):
        time_consumption = helper(N, M, board, target_height, B)

        if time_consumption == -1:
            continue

        if res_time > time_consumption:
            res_time, res_height = time_consumption, target_height

    print(res_time, res_height)
