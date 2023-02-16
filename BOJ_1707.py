import sys
from collections import deque
input = sys.stdin.readline

def bfs(V, E, W, now):
    res = []
    deq = deque()
    visited = [0] * V

    deq.append(now)
    visited[now] = 1

    while(True):
        if len(deq) <= 0: break

        src = deq.popleft()
        res.append(src)
        
        for dst in W[src]:
            if visited[dst]: continue

            visited[dst] = 1
            deq.append(dst)

    return res

def main(V, E, W):
    left = bfs(V, E, W, 0)
    if sum(left) == V or sum(left) == 0:
        print('NO')
        return

    right = []
    for i in range(V):
        if i in left: continue 

        right = bfs(V, E, W, i)
        break
    
    # print(left, right)
    for i in range(V):
        if (i in left) or (i in right): continue
        else: 
            print('NO')
            return
    print('YES')
    return

if __name__ == '__main__':
    K = int(input())
    for _ in range(K):
        V, E = map(int, input().split())
        W = [[] for _ in range(V)] # adjacent list
        for _ in range(E):
            src, dst = map(int, input().split())
            W[src-1].append(dst-1)
            W[dst-1].append(src-1)

        main(V,E,W)
