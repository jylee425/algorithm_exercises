from collections import deque

def bfs(N, K):
    deq = deque()
    visited = [0] * 200001

    # Initial point
    deq.append((N, 0))
    visited[N] = 1

    # BFS
    while(True):
        if len(deq) <= 0: break

        (NN, T)  = deq.popleft()

        if NN == K:
            print(T)
            return

        for i, X in enumerate([2*NN, NN-1, NN+1]):
            if X < 0 or X > 200000: continue 
            if visited[X]: continue

            if i == 0:
                deq.append((X, T))
            else:
                deq.append((X, T+1))
            visited[X] = 1

    return

if __name__ == '__main__':
    N, K = map(int, input().split())
    bfs(N, K)
