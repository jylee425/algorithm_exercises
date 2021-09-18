from collections import deque
import copy

N, M = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N) ]

def calculate(board):
    res = 0
    for x in range(N):
        for y in range(N):
            c = 0

            if board[x][y] == 1:
                visited = [ [0 for _ in range(N)] for _ in range(N) ]
                queue = deque()

                queue.append((x, y, c))
                while(queue):
                    (nx, ny, nc) = queue.popleft()
                    visited[nx][ny] = 1

                    if board[nx][ny] == 3: # alive chicken
                        res += nc
                        break

                    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        tx, ty, tc = nx+dx, ny+dy, nc+1
                        if tx < 0 or tx >= N or ty < 0 or ty >= N: continue
                        if visited[tx][ty]: continue
                        queue.append( (tx, ty, tc) )

    return res

def simulate(board, alive):
    answer = float("inf")

    if alive == M:
        return calculate(board)

    else:
        for x in range(N):
            for y in range(N):
                if board[x][y] == 2:
                    board_ = copy.deepcopy(board)

                    board_[x][y] = 3
                    pred = simulate(board_, alive+1)
                    answer = min(answer, pred)

                    board = copy.deepcopy(board)
        return answer

print(simulate(board, 0))
