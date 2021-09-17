import copy

ds = [[-1,0], [-1,-1], [0,-1], [1,-1], [1,0], [1,1], [0,1], [-1,1]]

def find_fish(board, index):
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == index:
                return (i, j)
    return None


def move_fish(board, sx, sy):  # 물고기 이동
    for i in range(1, 17):
        position = find_fish(board, i)
        if position is None: continue

        x, y = position[0], position[1]
        d = board[x][y][1]

        for j in range(8):
            tx, ty = x + ds[d][0], y + ds[d][1]
            if tx < 0 or tx >= 4 or ty < 0 or ty >= 4 or (tx == sx and ty == sy):
                d = (d + 1) % 8
                continue
            board[x][y][0], board[tx][ty][0] = board[tx][ty][0], board[x][y][0]
            board[x][y][1], board[tx][ty][1] = board[tx][ty][1], d
            break


def route(board, x, y):
    positions = []
    d = board[x][y][1]
    for i in range(1, 4):
        x, y = x + ds[d][0], y + ds[d][1]
        if x < 0 or x >= 4 or y < 0 or y >= 4: continue
        if board[x][y][0] < 0: continue
        positions.append([x, y])
    return positions


def dfs(board, x, y, score):
    global answer
    board = copy.deepcopy(board)

    # shark eat
    score += board[x][y][0]
    board[x][y][0] = -1

    # fish move
    move_fish(board, x, y)

    # shark move
    routes = route(board, x, y)
    answer = max(answer, score)
    for next_x, next_y in routes:
        dfs(board, next_x, next_y, score)


query = [list(map(int, input().split())) for _ in range(4)]
board = [[None] * 4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        board[i][j] = [query[i][j * 2], query[i][j * 2 + 1] - 1]

answer = 0
dfs(board, 0, 0, 0)
print(answer)
