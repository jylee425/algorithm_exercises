r, c, n = map(int, input().split())
board = [ [(0, 0, 0) for _ in range(c)] for _ in range(r) ]
for _ in range(n):
    x, y, s, d, z = map(int, input().split())
    board[x-1][y-1] = (s, d-1, z)

dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def move():
    result = [ [(0, 0, 0) for _ in range(c)] for _ in range(r) ]
    for i in range(r):
        for j in range(c):
            if board[i][j] != 0:
                x, y, s, d, z = i, j, board[i][j][0], board[i][j][1], board[i][j][2]
                while s > 0:
                    x += dir[d][0]
                    y += dir[d][1]
                    if 0 <= x < r and 0 <= y < c:
                        s -= 1
                    else:
                        x -= dir[d][0]
                        y -= dir[d][1]
                        if d == 0: d = 1
                        elif d == 1: d = 0
                        elif d == 2: d = 3
                        elif d == 3: d = 2
                if result[x][y] == 0:
                    result[x][y] = [board[i][j][0], d, z]
                else:
                    if result[x][y][2] < z:
                        result[x][y] = [board[i][j][0], d, z]
    return result

answer = 0
for cc in range(c):
    # 1 move to next column

    # 2 catch shark
    for rr in range(r):
        shark = board[rr][cc]
        if shark[2] != 0:
            answer += shark[2]
            board[rr][cc] = (0, 0, 0)
            break
    
    # 3 move shark
    board = move()

print(answer)
