from collections import deque

N, M = map(int, input().split())
x, y, d = map(int, input().split())

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
board = [ list(map(int, input().split())) for _ in range(N) ]
visited = [ [0 for _ in range(M)] for _ in range(N) ]

answer = 0
q = deque()
q.append((x, y, d, 0))
while(q):
    x, y, d, c = q.popleft()

    if not visited[x][y]:
        visited[x][y] = 1
        answer += 1

    if c > 3:
        td = (d + 2)%4
        tx, ty = x+dir[td][0], y+dir[td][1]
        if board[tx][ty] == 1: #4
            print(answer)
            exit()
        q.append((tx, ty, d, 0)) #3
    else:
        td = (d - 1) % 4
        tx, ty = x+dir[td][0], y+dir[td][1]
        if board[tx][ty] == 1 or visited[tx][ty]:
            q.append((x, y, td, c+1)) #2
        else:
            q.append((tx, ty, td, 0)) #1
