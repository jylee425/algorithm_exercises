
res = 1e10 

def check(Sij, visited):
    global res
    start, link = 0, 0

    for i in range(N-1):
        for j in range(i+1, N):
            if visited[i] and visited[j]:
                start += Sij[i][j] + Sij[j][i]
            elif not visited[i] and not visited[j]:
                link += Sij[i][j] + Sij[j][i]

    res = min(res, abs(start - link))
    return


def dfs(Sij, visited, cnt):
    if(cnt == N):
        if sum(visited) == N//2:
            check(Sij, visited)
        return

    visited[cnt] = True
    dfs(Sij, visited, cnt+1)
    visited[cnt] = False
    dfs(Sij, visited, cnt+1)
    return

def main(N, Sij):
    cnt = 0
    visited = [False] * N

    dfs(Sij, visited, cnt)
    print(res)
    return

if __name__ == '__main__':
    N = int(input())
    Sij = [list(map(int, input().split())) for _ in range(N)]

    main(N, Sij)
