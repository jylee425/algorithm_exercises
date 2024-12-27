result = {-1: 0, 0: 0, 1: 0}


def divide_and_conquer(board, N, starting_x=0, starting_y=0):

    if N == 1:
        return board[starting_x][starting_y]

    left_top = divide_and_conquer(
        board, N // 2, starting_x=starting_x, starting_y=starting_y
    )
    right_top = divide_and_conquer(
        board, N // 2, starting_x=starting_x + N // 2, starting_y=starting_y
    )
    left_bottom = divide_and_conquer(
        board, N // 2, starting_x=starting_x, starting_y=starting_y + N // 2
    )
    right_bottom = divide_and_conquer(
        board, N // 2, starting_x=starting_x + N // 2, starting_y=starting_y + N // 2
    )

    if (left_top, right_top, left_bottom, right_bottom) == (1, 1, 1, 1):
        return 1
    elif (left_top, right_top, left_bottom, right_bottom) == (0, 0, 0, 0):
        return 0
    else:
        result[left_top] += 1
        result[right_top] += 1
        result[left_bottom] += 1
        result[right_bottom] += 1
        return -1


if __name__ == "__main__":
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]
    # print(board)

    whole = divide_and_conquer(board, N, 0, 0)
    result[whole] += 1

    print(result[0])
    print(result[1])
