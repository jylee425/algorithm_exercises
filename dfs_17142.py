from copy import deepcopy
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N)]
virus = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append((i, j))

def spread(virus):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()

    for x, y in virus:
        queue.append((x, y, 0))

    result = 0
    while (queue):
        x, y, t = queue.popleft()

        if visited[x][y]: continue
        visited[x][y] = t

        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            tx, ty, tt = x+dx, y+dy, t+1
            if 0 <= tx < N and 0 <= ty < N and board[tx][ty] != 1:
                queue.append((tx, ty, tt))

    # should have spread to all boards
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                if visited[i][j] == 0:
                    return float("inf")
                result = max(result, visited[i][j])
    return result

visited = [0 for _ in range(len(virus))]
answer = float("inf")
def simulate(cnt, cur):
    global answer
    if cnt == M:
        selected = [ virus[i] for i in range(len(virus)) if visited[i] ]
        answer = min(answer, spread(selected))
        return
    for i in range(cur, len(virus)):
        if visited[i] == 0:
            visited[i] = 1
            simulate(cnt+1, i)
            visited[i] = 0
simulate(0, 0)

if answer == float('inf'):
    print(-1)
else:
    print(answer)
