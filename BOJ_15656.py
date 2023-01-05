
def dfs(arr, M, selected):
    if len(selected) >= M:
        for s in selected:
            print(s, end=' ')
        print()
        return

    for i, n in enumerate(arr):
        selected.append(n)
        dfs(arr, M, selected)
        selected.pop()


def main(N, M, arr):
    arr = sorted(arr)
    selected = []

    dfs(arr, M, selected)
    
    return

if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    main(N, M, arr)
