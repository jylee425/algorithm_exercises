from collections import deque

def bfs(N, K):
    """
    find the method of making N from K with following operations:
        1) K - 1
        2) K + 2
        3) K // 2
    """
    dist = [0] * (100000 + 1)
    path = [0] * (100000 + 1)

    q = deque()
    q.append(N)
    while q:
        n = q.popleft()

        if n == K:
            print(dist[n])

            arr = []
            temp = n
            for _ in range(dist[n]+1):
                arr.append(temp)
                temp = path[temp]
            print(' '.join(map(str, arr[::-1])))
            return n
        
        for k in (n-1, n+1, 2*n):
            if k < 0 or k > 100000:
                continue
            if dist[k] != 0:
                continue

            q.append(k)
            dist[k] = dist[n] + 1
            path[k] = n

    return

if __name__ == '__main__':
    N, K = map(int, input().split())
    bfs(N, K)
