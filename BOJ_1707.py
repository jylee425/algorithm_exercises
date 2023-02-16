import sys
from collections import deque
input = sys.stdin.readline

def bfs(V, E, W, now):
    zeros, ones = [], []
    deq = deque()
    visited = [0] * V

    deq.append((now, 0))
    visited[now] = 1

    while(True):
        if len(deq) <= 0: break

        src, group = deq.popleft()
        # print(src, group)
        if group == 0: 
            zeros.append(src)
            other = 1
        elif group == 1: 
            ones.append(src)
            other = 0

        for dst in W[src]:
            if visited[dst]: continue

            visited[dst] = 1
            deq.append((dst, other))

    return zeros, ones

def main(V, E, W):
    zeros, ones = bfs(V, E, W, 0)
    # print(zeros, ones)

    while(True):
        if len(zeros) + len(ones) == V: break

        for i in range(V):
            if (i in zeros) or (i in ones): continue

            tmp_0, tmp_1 = bfs(V, E, W, i)
            zeros = zeros + tmp_0
            ones = ones + tmp_1

    for src in zeros:
        for dst in W[src]:
            if dst in zeros:
                print('NO')
                return
    for src in ones:
        for dst in W[src]:
            if dst in ones:
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
