
def dfs(N, edges, visited, now, cnt):
    if cnt == 4:
        print(1)
        exit()
    
    for j in edges[now]:
        if visited[j]: continue
        # print(now, edges[now], j)

        visited[j] = 1
        dfs(N, edges, visited, j, cnt+1)
        visited[j] = 0

    return
    

def main(N, edges):
    cnt = 0
    visited = [0] * (N+1)

    for i in range(N):
        visited[i] = 1
        dfs(N, edges, visited, i, cnt)
        visited[i] = 0

    print(0)
    return


if __name__ == '__main__':
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(M):
        src, dst = map(int, input().split())
        edges[src].append(dst)
        edges[dst].append(src)

    main(N, edges)

