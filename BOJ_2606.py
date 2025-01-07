def dfs(current, v, e, visited):
    for target in range(len(v)):
        if e[current][target] == 1 and visited[target] == 0:
            visited[target] = 1
            dfs(target, v, e, visited)

    return


if __name__ == "__main__":
    N = int(input())

    v = [i for i in range(N)]
    visited = [0 for _ in range(N)]
    e = [[0 for _ in range(N)] for _ in range(N)]

    for _ in range(int(input())):
        src, dst = map(int, input().split())

        e[src - 1][dst - 1] = 1
        e[dst - 1][src - 1] = 1

    current = 0
    v[current] = 1
    visited[current] = 1
    dfs(current, v, e, visited)

    print(sum(visited) - 1)
