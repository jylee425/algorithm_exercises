N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(list(input()))

# neighbors
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

# BFS
queue = [(0,0)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
while queue:
    r, c = queue.pop(0)

    if r == N-1 and c == M-1:
        print(visited[r][c])
        break

    # serach neighbors
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if maze[nr][nc] == '1' and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c]+1
                queue.append((nr,nc))