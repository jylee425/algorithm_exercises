N,M = map(int,input().split())
adj=[[0]*(N+1)for i in range(N+1)]

for i in range(M):
    u,v=map(int,input().split())
    adj[v][u] = 1
    adj[u][v] = 1
visited=[False]*(N+1)

def bfs(v):
    queue=[v]
    while queue:
        v=queue.pop(0)
        for i in range(1,N+1):
            if adj[i][v]==1 and not visited[i]:
                visited[i]=True
                queue.append(i)

answer=0
for i in range(1,N+1):
    if not visited[i]:
        bfs(i)
        answer+=1