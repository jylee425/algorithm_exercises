import heapq

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# init on baby shark
queue = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            heapq.heappush(queue,(0, i, j))
            board[i][j] = 0

# bfs
answer  = 0
size    = 2
eat     = 0
visited = [[0 for _ in range(N)] for _ in range(N)]

while queue:
    d, x, y = heapq.heappop(queue)

    if 0 < board[x][y] < size:
        eat += 1
        board[x][y] = 0

        if eat == size:
            size += 1
            eat = 0

        answer += d
        d = 0
        queue.clear()
        visited = [[0 for _ in range(N)] for _ in range(N)]

    for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        td, tx, ty = d+1, x+dx, y+dy
        if tx < 0 or tx >= N or ty < 0 or ty >= N: continue
        if board[tx][ty] > size : continue
        if visited[tx][ty] : continue

        heapq.heappush(queue, (td, tx, ty))
        visited[tx][ty] = 1

print(answer)
