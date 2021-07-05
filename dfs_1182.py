N, S = map(int, input().split())
ns = list(map(int, input().split()))
cnt = 0

def dfs(idx, sum):
    global cnt
    if idx >= N:
        return

    sum += ns[idx]
    if sum == S:
        cnt += 1
    dfs(idx + 1, sum - ns[idx]) # 넣은것
    dfs(idx + 1, sum) # 안넣은것

dfs(0, 0)
print(cnt)
