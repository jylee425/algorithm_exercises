import sys
from collections import deque

input = sys.stdin.readline

def dfs(N, M, V, edges, src, visited):
    print(src+1, end=' ')
    for dst, e in enumerate(edges[src]):
        if visited[dst]: continue
        if e == 0: continue

        visited[dst] = 1
        dfs(N, M, V, edges, dst, visited)
    return

def bfs(N, M, V, edges, src, visited):
    deq = deque()

    deq.append(src)
    while(True):
        if len(deq) <= 0: break

        now = deq.popleft()
        print(now+1, end=' ')

        for dst, e in enumerate(edges[now]):
            if visited[dst]: continue
            if e == 0: continue

            visited[dst] = 1
            deq.append(dst)

    return

def main(N, M, V, edges):
    # dfs
    now = V-1
    visited = [0] * N
    visited[now] = 1
    dfs(N, M, V, edges, now, visited)

    print()

    # bfs
    now = V-1
    visited = [0] * N
    visited[now] = 1
    bfs(N, M, V, edges, now, visited)

    return

if __name__ == '__main__':
    N, M, V = map(int, input().split())
    edges = [[0] * N for _ in range(N)]

    for _ in range(M):
        src, dst = map(int, input().split())
        edges[src-1][dst-1] = edges[dst-1][src-1] = 1

    main(N, M, V, edges)

