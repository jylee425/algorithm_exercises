import copy

def build_left(board):
    left = {} # row * 9 + col: possibles
    board_row, board_col, board_box = {}, {}, {}
    for i in range(9): board_row[i], board_col[i], board_box[i] = [], [], []

    for i in range(9):
        for j in range(9):
            board_row[i].append(board[i][j])
            board_col[i].append(board[j][i])
            board_box[(i//3)*3+(j//3)].append(board[i][j])

    for i in range(9):
        for j in range(9):
            idx = i * 9 + j
            if board[i][j] == 0:
                left[idx] = set([1,2,3,4,5,6,7,8,9])
                left[idx] -= set(board_row[i])
                left[idx] -= set(board_col[j])
                left[idx] -= set(board_box[(i//3)*3+(j//3)])
            else:
                left[idx] = set()

    return left

def check(now):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True

def bruteforce(board, left, now, visited):
    sum_visited = sum([sum(visited[i]) for i in range(9)])
    print('\n', now, sum_visited, left, '\n')
    if sum_visited == 81:
        for b in now:
            print(' '.join(map(str, b)))
        exit(0)
    
    for i in range(9):
        for j in range(9):
            if visited[i][j]: continue
             
            candidate = list(left[i * 9 + j])
            if len(candidate) == 0: return

            number = candidate[0] # pick one

            now[i][j] = number
            new_left = build_left(now)
            visited[i][j] = 1
            ret = bruteforce(board, new_left, now, visited)
            now[i][j] = 0
            visited[i][j] = 0
            left = build_left(now)
    return


def main(board):
    left = build_left(board)
    # print(left)

    visited = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0: visited[i][j] = 1
    now = copy.deepcopy(board)
    bruteforce(board, left, now, visited)

    # for b in board:
    #     print(' '.join(map(str, b)))
    return

if __name__ == '__main__':
    board = [list(map(int, input().split())) for _ in range(9)]
    main(board)
