
def dfs(N, edges, src, visited):
    visited[src]
    for dst, link in enumerate(edges[src]):
        if visited[dst]: continue
        if link != 1: continue

        visited[dst] = 1
        dfs(N, edges, dst, visited)

def main(N, edges, plan):
    visited = [0 for _ in range(N+1)]
    now = plan[0]-1
    dfs(N, edges, now, visited)

    if 0 not in visited:
        print('YES')
        return

    for city in plan:
        if not visited[city-1]:
            print('NO')
            return

    print('YES')
    return

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    edges = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        edges[i][i] = 1

    plan = list(map(int, input().split()))
    if len(plan) <= 1:
        print('YES')
    else:
        main(N, edges, plan)
