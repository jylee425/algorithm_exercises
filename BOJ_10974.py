
def dfs(N, selected):
    if len(selected) == N:
        print(' '.join(map(str, selected)))
        return

    for i in range(1, N+1):
        if i in selected: continue

        selected.append(i)
        dfs(N, selected)
        selected.pop()

    return


def main(N):
    selected = []

    dfs(N, selected)


if __name__ == '__main__':
    N = int(input())

    main(N)
