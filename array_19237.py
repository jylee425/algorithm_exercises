import copy

N, M, K = map(int, input().split())
board = [ [(0, 0, 0) for _ in range(N)] for _ in range(N) ]
# (상어idx, 냄새idx, 냄새time)

for j in range(N):
    for i, s in enumerate(list(map(int, input().split()))):
        if s != 0:
            board[j][i] = (s, s, K)

shark_dir = list(map(int, input().split()))

# (위, 아래, 왼쪽, 오른쪽)
shark_ord = [ {} for _ in range(M) ]
for s in range(M):
    for i in range(4):
        shark_ord[s][i] = list(map(int, input().split()))

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def find(s, x, y):
    no_smell = []
    my_smell = []
    for d in dir:
        tx, ty = x+d[0], y+d[1]
        if tx < 0 or tx >= N or ty < 0 or ty >= N: continue
        if board[tx][ty][1] == 0:
            no_smell.append((tx, ty))
        elif board[tx][ty][1] == s:
            my_smell.append((tx, ty))
    return no_smell, my_smell

def move(board):
    eat = 0
    result = copy.deepcopy(board)
    for x in range(N):
        for y in range(N):
            shark, smell, time = board[x][y]
            if shark != 0:
                no_smell, my_smell = find(shark, x, y)
                now_dir = shark_dir[shark-1]
                now_ord = shark_ord[shark-1][now_dir-1]

                if len(no_smell) > 0:
                    for d in now_ord:
                        tx, ty, td = x+dir[d-1][0], y+dir[d-1][1], d
                        if (tx, ty) in no_smell:
                            break
                else:
                    for d in now_ord:
                        tx, ty, td = x+dir[d-1][0], y+dir[d-1][1], d
                        if (tx, ty) in my_smell:
                            break

                # move shark
                shark_dir[shark - 1] = td
                result[x][y] = (0, shark, K)
                if result[tx][ty][0] != 0:
                    eat += 1
                    if result[tx][ty][0] > shark:
                        result[tx][ty] = (shark, shark, K)
                else:
                    result[tx][ty] = (shark, shark, K)
    return eat, result

def time(board):
    for x in range(N):
        for y in range(N):
            if board[x][y][0] == 0 and board[x][y][1] != 0:
                if board[x][y][2] - 1 > 0:
                    board[x][y] = (board[x][y][0], board[x][y][1], board[x][y][2]-1)
                else:
                    board[x][y] = (0, 0, 0)
    return 1

answer = 0
eaten = 0
while(True):
    e, board = move(board)
    eaten += e
    answer += time(board)

    if M - eaten == 1:
        print(answer)
        break
    elif answer >= 1000:
        print(-1)
        break

