
ans = -1

def check(N, arr, selected):
    res = 0

    for s in range(N-1):
        i, j = selected[s], selected[s+1]
        res += abs(arr[i]-arr[j])

    return res

def dfs(N, arr, selected):
    global ans

    if len(selected) == N:
        tmp = check(N, arr, selected)
        ans = max(ans, tmp)
        return
    
    for i in range(N):
        if i in selected: continue

        selected.append(i)
        dfs(N, arr, selected)
        selected.pop()

    return

def main(N, arr):
    global ans
    selected = []

    dfs(N, arr, selected)
    print(ans)
    return

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))

    main(N, arr)
