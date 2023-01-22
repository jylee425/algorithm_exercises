
T = -1
ans = 1e10

def check(selected, Sij):
    global ans, T

    res = 0
    for i in selected:
        for j in selected:
            res += Sij[i][j]

    ans = min(abs(T - res - res), ans)
    print('**', ans)
    return

def dfs(N, Sij, selected):
    print(selected)
    check(selected, Sij)
    
    for i in range(N):
        if i in selected: continue

        selected.append(i)
        dfs(N, Sij, selected)
        selected.pop()

    return

def main(N, Sij):
    selected = []
    dfs(N, Sij, selected) 

    print(ans)
    return


if __name__ == '__main__':
    N = int(input())

    Sij = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        Sij.append(tmp)
        T += sum(tmp)

    main(N, Sij)
