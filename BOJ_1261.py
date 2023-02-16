from collections import deque

ans = 1e5
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def bfs(N, M):
    deq = deque()
    visited = [[-1] * M for _ in range(N)]

    deq.append((0, 0))
    visited[0][0] = 0
    while(True):
        if len(deq) <= 0: break

        x, y = deq.popleft()
        # print(x, y, visited[x][y])
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if visited[nx][ny] != -1: continue
            
            if board[nx][ny] == 0:
                visited[nx][ny] = visited[x][y]
                deq.appendleft((nx, ny))
            elif board[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                deq.append((nx, ny))

    print(visited[N-1][M-1])
    return

if __name__ == '__main__':
    M, N = map(int, input().split())
    board = [list(map(int, input())) for _ in range(N)]
    # print(board)

    bfs(N, M)
