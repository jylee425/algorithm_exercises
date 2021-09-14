from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def find(x, y, color):
    block_cnt, rainbow_cnt = 1, 0
    blocks, rainbows = [[x, y]], []

    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            tx, ty = x+dx, y+dy
            if tx<0 or tx>=N or ty <0 or ty>= N: continue
            if visited[tx][ty]: continue

            if board[tx][ty] == color :
                visited[tx][ty] = 1
                queue.append([tx, ty])
                block_cnt += 1
                blocks.append([tx, ty])
            elif board[tx][ty] == 0:
                visited[tx][ty] = 1
                queue.append([tx, ty])
                block_cnt += 1
                rainbow_cnt += 1
                rainbows.append([tx, ty])

    # issue
    for x, y in rainbows:
        visited[x][y] = 0

    return [block_cnt, rainbow_cnt, blocks + rainbows]

def erase(group):
    for x, y in group:
        board[x][y] = -2
    return

def gravity(b):
    for y in range(N):
        for x in range(N-1, -1, -1):
            if b[x][y] == -2:

                for xx in range(x-1, -1, -1):
                    if b[xx][y] >= -1:
                        if b[xx][y] >= 0:
                            b[x][y] = b[xx][y]
                            b[xx][y] = -2
                        break

    return b

def rotate(board):
    res = [ [-2 for _ in range(N)] for _ in range(N)]

    for x in range(N):
        for y in range(N):
            res[x][y] = board[y][(-1-x)%N]

    return res

result = 0
while(True):
    #print(board)

    groups = []
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and not visited[i][j]:
                visited[i][j] = 1
                tmp = find(i, j, board[i][j])
                if tmp[0] >= 2: groups.append(tmp)

    if len(groups) < 1: break

    groups.sort(reverse=True)
    erase(groups[0][2])
    result += (groups[0][0]) ** 2
    #print(groups)
    #print(board)

    board = gravity(board)
    #print(board)
    board = rotate(board)
    #print(board)
    board = gravity(board)
    #print(board)

    #print(result)
    #print()

print(result)
