def dfs(map, x, y):
  global count
  if (x >= 0 and x < N) and (y >= 0 and y < N):
    if map[x][y] == 1:
      map[x][y] = 2
      count += 1
      dfs(map, x-1, y)
      dfs(map, x+1, y)
      dfs(map, x, y-1)
      dfs(map, x, y+1)
      return True
    else:
      return False
  return False

from sys import stdin

N = int(input())

map = []
for i in range(N):
  tmp = []
  line = stdin.readline().strip()
  for j in line:
    tmp.append(int(j))
  map.append(tmp)


result = 0
answer = []
count  = 0
for i in range(N):
  for j in range(N):
    if dfs(map, i, j):
      result += 1
      answer.append(count)
      count = 0
  
print(result)
answer.sort()
for i in answer:
  print(i)
      

