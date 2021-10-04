import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
board = [list(map(int, input().split())) for i in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    if visited[x][y]: return visited[x][y]
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[x][y] < board[nx][ny]:
                visited[x][y] = max(visited[x][y], dfs(nx, ny) + 1)
    return visited[x][y]

visited = [[0] * n for i in range(n)]
result = 0
for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))
print(result)
