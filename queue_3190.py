from collections import deque

N = int(input())
board = [ [0 for _ in range(N)] for _ in range(N) ]

K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    board[i-1][j-1] = 2

L = int(input())
query = []
for _ in range(L):
    query.append(input())

answer = 0
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
snake = deque()

x, y, d = 0, 0, 0 # (0, 1, 2, 3) = (right, down, left, up)
snake.append((x, y))

q_idx = 0
last = False
while True:
    time, dir = query[q_idx].split()
    time = int(time)

    answer += 1

    tx, ty = x + directions[d][0], y + directions[d][1]
    if tx < 0 or ty < 0 or tx >= N or ty >= N:
        print(answer)
        exit()

    if board[tx][ty] == 0:
        board[tx][ty] = 1
        px, py = snake.popleft()
        board[px][py] = 0
    elif board[tx][ty] == 1:
        print(answer)
        exit()
    elif board[tx][ty] == 2:
        board[tx][ty] = 1
        pass

    board[tx][ty] = 1
    snake.append((tx, ty))

    x, y = tx, ty

    if answer == time and (not last):
        # direction
        if dir == "L":
            d = (d - 1) % 4
        elif dir == "D":
            d = (d + 1) % 4

        q_idx = q_idx+1
        if q_idx > len(query)-1:
            last = True
            q_idx = q_idx-1


print(answer)

