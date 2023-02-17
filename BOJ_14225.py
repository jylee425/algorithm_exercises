
def dfs(N, S, now, memo, selected):
    memo[sum(selected)] = 1

    for i in range(N):
        if i <= now: continue

        selected.append(S[i])
        dfs(N, S, i, memo, selected)
        selected.pop()

    return

def main(N, S):
    memo = [0] * (100001 * 20)
    selected = []
    now = -1
    
    dfs(N, S, now, memo, selected)

    for i, v in enumerate(memo):
        if v == 0: 
            print(i)
            break
    return

if __name__ == '__main__':
    N = int(input())
    S = list(map(int, input().split()))
    main(N, S)
