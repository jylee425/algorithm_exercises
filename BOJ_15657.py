
def dfs(arr, M, visited, selected):
    # print('in dfs ', selected)

    if len(selected) >= M:
        for s in selected:
            print(s, end=' ')
        print()
        return

    for i, n in enumerate(arr):
        if i < visited: continue

        selected.append(n)
        dfs(arr, M, i, selected)
        selected.pop()


def main(N, M, arr):
    arr = sorted(arr)
    visited = -1
    selected = []

    dfs(arr, M, visited, selected)
    
    return

if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    main(N, M, arr)
