
def dfs(arr, M, visited, selected):
    if len(selected) >= M:
        for s in selected:
            print(s, end=' ')
        print()
        return

    for i, n in enumerate(arr):
        if visited[i] == 1: continue

        selected.append(n)
        visited[i] = 1
        dfs(arr, M, visited, selected)
        selected.pop()
        visited[i] = 0


def main(N, M, arr):
    arr = sorted(arr)
    visited = [0] * N
    selected = []

    dfs(arr, M, visited, selected)
    
    return

if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    main(N, M, arr)
