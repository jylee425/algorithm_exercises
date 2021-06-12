N = int(input())
M = int(input())

vs = [0 for _ in range(N)]
hs = [0 for _ in range(N)]
es = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    src, dst = map(int, input().split())
    src, dst = src-1, dst-1
    es[src][dst] = 1
    es[dst][src] = 1

def dfs(vs, es, v):
    hs[v] = 1
    global count
    for u in range(len(vs)): 
       if (es[v][u]) == 1 and hs[u] == 0:
            count += 1
            dfs(vs, es, u)

count = 0
vs[0] = 1
dfs(vs, es, 0)
print(count)