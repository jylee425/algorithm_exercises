N, M = map(int, input().split())
adj=[[]*(N+1)for i in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs(v):
    queue=[v]
    while queue:
        v=queue.pop(0)
        for u in adj[v]:
            if not visited[u]:
                visited[u]=True
                queue.append(u)

count=0
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        count+=1
print(count)