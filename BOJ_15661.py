
ans = 1e10

def check(N, visited, Sij):
    global ans

    start, link = 0, 0
    for i in range(N-1):
        for j in range(i+1, N):
            if visited[i] and visited[j]:
                start += Sij[i][j] + Sij[j][i]
            elif not visited[i] and not visited[j]:
                link += Sij[i][j] + Sij[j][i]

    ans = min(ans, abs(start-link))
    return

def dfs(N, Sij, visited, cnt):
    if cnt == N:
        check(N, visited, Sij)
        return
    
    visited[cnt] = True
    dfs(N, Sij, visited, cnt+1)
    visited[cnt] = False
    dfs(N, Sij, visited, cnt+1)

    return

def main(N, Sij):
    cnt = 0
    visited = [False] * N
    dfs(N, Sij, visited, cnt) 

    print(ans)
    return


if __name__ == '__main__':
    N = int(input())
    Sij = [list(map(int, input().split())) for _ in range(N)]

    main(N, Sij)
