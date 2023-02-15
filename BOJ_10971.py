
ans = 1e9

def dfs(N, W, start, now, value, visited):
    global ans

    if sum(visited) >= N:
        last_path = W[now][start]
        if last_path != 0: # should be able to return
            value += last_path
            ans = min(ans, value)

    for i in range(N):
        if visited[i]: continue

        i_path = W[now][i]
        if i_path == 0: continue

        visited[i] = 1
        dfs(N, W, start, i, value+i_path, visited)
        visited[i] = 0 

    return

def main(N, W):
    global ans
    visited = [0] * N

    for i in range(N):
        visited[i] = 1

        start = i
        now = i
        value = 0
        dfs(N, W, start, now, value, visited)
        
        visited[i] = 0

    print(ans)
    return

if __name__ == '__main__':
    N = int(input())
    W = [list(map(int, input().split())) for _ in range(N)]
    main(N, W)
