from collections import deque

def bfs(S):
    q = deque()
    visited = [[-1] * (S+1) for _ in range(S+1)]

    # initial state
    q.append((1, 0)) # S, clipboard
    visited[1][0] = 0

    while True:
        if len(q) < 1: break

        (n, c) = q.popleft()
        if n == S:
            print(visited[n][c])
            return

        # 1. copy to clipboard
        if visited[n][n] == -1:
            visited[n][n] = visited[n][c] + 1
            q.append((n, n))

        # 2. paste from clipboard
        if n+c <= S and visited[n+c][c] == -1:
            visited[n+c][c] = visited[n][c] + 1
            q.append((n+c, c))

        # 3. delete one
        if n-1 >= 0 and visited[n-1][c] == -1:
            visited[n-1][c] = visited[n][c] + 1
            q.append((n-1, c))

    return

if __name__ == '__main__':
    S = int(input())
    bfs(S)
