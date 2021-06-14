import sys
sys.setrecursionlimit(10000)

            
N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(v):
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)

count = 0
for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)