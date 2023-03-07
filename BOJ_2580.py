import copy

def possible(board, x, y, n):
    # row
    for i in range(9):
        if board[x][i] == n:
            return False

    # col
    for i in range(9):
        if board[i][y] == n:
            return False

    # box
    box_x, box_y = x // 3, y //3 
    for i in range(3):
        for j in range(3):
            if board[box_x * 3 + i][box_y * 3 + j] == n:
                return False

    return True 


def bruteforce(board, empty, cnt):
    if cnt == len(empty):
        for b in board:
            print(' '.join(map(str, b)))
        exit(0)

    x, y = empty[cnt]
    for n in range(1, 10):
        if possible(board, x, y, n):
            board[x][y] = n
            bruteforce(board, empty, cnt+1)
            board[x][y] = 0
    return


def main(board):
    empty = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0: empty.append((i,j))
    bruteforce(board, empty, 0)
    
    return

if __name__ == '__main__':
    board = [list(map(int, input().split())) for _ in range(9)]
    main(board)
