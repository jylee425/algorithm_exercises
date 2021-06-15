import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(N+1)]
adj[0] = [0,0]
visited = [False for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    adj[start].append(end)
    adj[end].append(start)
    adj[start].sort()
    adj[end].sort()

def dfs(adj, start, visited):
    visited[start] = True

    for i in adj[start]:
        if not visited[i]:
            dfs(adj, i, visited)

count = 0
for i in range(1, len(visited)):
    if visited[i] == False:
        count += 1
        dfs(adj, i, visited)
print(count)