def dfs(map, x, y):
  if (x >= 0 and x < n) and (y >= 0 and y < n):
    if map[x][y] == 1:
      dfs(x-1, y)
      dfs(x+1, y)
      dfs(x, y-1)
      dfs(x, y+1)
      return True
    else:
      return False
  return False

n = int(input())

map = []
for i in range(n):
  map.append(list(map(int,input().strip())))
