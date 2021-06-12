import sys 
sys.setrecursionlimit(10000)


N = int(input())

def dfs(land, visited, r, c, x, y):
    if x>=0 and x<r and y>=0 and y<c:
        if land[x][y] == 1 and visited[x][y] == 0:
            visited[x][y] = 1
            dfs(land, visited, r, c, x-1, y)
            dfs(land, visited, r, c, x+1, y)
            dfs(land, visited, r, c, x, y-1)
            dfs(land, visited, r, c, x, y+1)
            return True
        else: return False
    else: return False

answer = []
for _ in range(N):
    r, c, n = map(int, input().split())
    land = [[0] * c for _ in range(r)]
    visited = [[0] * c for _ in range(r)]
    
    for _ in range(n):
        x, y = map(int, input().split())
        land[x][y] = 1

    count = 0
    for xx in range(r):
        for yy in range(c):
            if dfs(land, visited, r, c, xx, yy) == True:
                count+=1
    answer.append(count)
for aa in answer:
    print(aa)