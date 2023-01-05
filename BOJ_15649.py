
def dfs(N, M, visited, selected):
    # print('in dfs', now, selected)

    if len(selected) >= M:
        for s in selected:
            print(s, end=' ')
        print()
        return

    for i in range(N):
        if visited[i] == 1: continue

        selected.append(i+1)
        visited[i] = 1
        dfs(N, M, visited, selected)
        selected.pop()
        visited[i] = 0
    return

def main(N, M):
    """
    Args:
        N: N range of numbers
        M: pick M numbers
    """
    visited = [0] * N
    selected = []

    dfs(N, M, visited, selected)
    

if __name__ == "__main__":
    N, M = map(int, input().split())

    main(N, M)

