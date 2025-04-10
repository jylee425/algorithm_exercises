if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # Find the starting point (2) and the destination point (1)
    start = None
    destination = None
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                start = (i, j)
            elif arr[i][j] == 1:
                destination = (i, j)

    # BFS
    distance = [[-1] * M for _ in range(N)]
    distance[start[0]][start[1]] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * M for _ in range(N)]

    queue = [start]
    distance[start[0]][start[1]] = 0
    visited[start[0]][start[1]] = True
    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

    # print
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                print(0, end=" ")
            elif distance[i][j] == -1:
                print(-1, end=" ")
            else:
                print(distance[i][j], end=" ")
        print()
