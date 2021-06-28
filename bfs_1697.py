from collections import deque
n, k = map(int, input().split())
visited  = [0] * 200001
queue = deque()

def bfs():
    while(queue):
        s = queue.popleft()

        if s == k:
            print(visited[s])
            break

        for x in [s-1, s+1, 2*s]:
            if 0 <= x <= 20001 and visited[x] == 0:
                queue.append(x)
                visited[x] = visited[s]+1

queue.append(n)
bfs()
