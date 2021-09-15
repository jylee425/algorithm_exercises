import copy

def move(dir):
    if dir == 0: # up
        for j in range(N):
            idx = 0
            for i in range(1, N):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0

                    if board[idx][j] == 0:
                        board[idx][j] = tmp
                        idx += 0 # may get merged
                    elif board[idx][j] == tmp:
                        board[idx][j] = tmp * 2
                        idx += 1 # merged
                    else:
                        idx += 1 # moved
                        board[idx][j] = tmp
    elif dir == 1: # down
        for j in range(N):
            idx = N-1
            for i in range(N-2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0

                    if board[idx][j] == 0:
                        board[idx][j] = tmp
                        idx += 0
                    elif board[idx][j] == tmp:
                        board[idx][j] = tmp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        board[idx][j] = tmp
    elif dir == 2: # left
        for i in range(N):
            idx = 0
            for j in range(1, N):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0

                    if board[i][idx] == 0:
                        board[i][idx] = tmp
                        idx += 0
                    elif board[i][idx] == tmp:
                        board[i][idx] = tmp * 2
                        idx += 1
                    else:
                        idx += 1
                        board[i][idx] = tmp
    elif dir == 3:  # right
        for i in range(N):
            idx = N-1
            for j in range(N-2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0

                    if board[i][idx] == 0:
                        board[i][idx] = tmp
                        idx += 0
                    elif board[i][idx] == tmp:
                        board[i][idx] = tmp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        board[i][idx] = tmp

# dfs
def play(cnt):
    global board, answer
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                answer = max(answer, board[i][j])
        return

    board_ = copy.deepcopy(board) # save
    for dir in [0,1,2,3]:
        move(dir)
        play(cnt + 1)
        board = copy.deepcopy(board_) # load

N = int(input())
board = [ list(map(int, input().split())) for _ in range(N) ]

answer = 0
play(0)
print(answer)
