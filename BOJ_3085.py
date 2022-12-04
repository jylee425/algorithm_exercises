

def helper(board, res):
    """
    Args:
        board: give board
    Return:
        max cnt the number of same colors adjacent, given board
    """
    N = len(board)
    
    # row-wise search 
    for r in range(N):
        cnt = 1 
        for c in range(N - 1):
            if board[r][c] == board[r][c + 1]: 
                cnt += 1
                res = max(res, cnt)
            else: 
                cnt = 1
    
    # column-wise search 
    for c in range(N):
        cnt = 1
        for r in range(N - 1):
            if board[r][c] == board[r + 1][c]:
                cnt += 1
                res = max(res, cnt)
            else: 
                cnt = 1
    
    return res

def brute_force(board):
    """
    search for the same color by swapping every row/column
    """
    N = len(board)

    res = 0
    for i in range(N):
        for j in range(N-1):
            # swap column (i,j) & (i,j+1)
            if board[i][j] != board[i][j+1]:
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                res = max(res, helper(board, res))
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

            # swap row (j,i) & (j+1,i)
            if board[j][i] != board[j+1][i]:
                board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
                res = max(res, helper(board, res))
                board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

    return res

if __name__ == "__main__":
    N = int(input())
    board = [list(map(str, input())) for _ in range(N)]

    print(brute_force(board))
