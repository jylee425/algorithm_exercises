
def check(res):
    for i in range(10):
        if i not in res:
            return 0
    return 1

def dfs(N, res, answer):
    print(res)

    if len(res) == N:
        answer += check(res)

    if len(res) == 0: 
        for i in range(1, 10):
            res.append(i)
            dfs(N, res, answer)
            res.pop()
    else:
        tmp = res[-1]
        if 1 <= tmp <= 8:
            res.append(tmp+1)
            dfs(N, res, answer)
            res.pop()

            res.append(tmp-1)
            dfs(N, res, answer)
            res.pop()
        elif tmp == 0:
            res.append(tmp+1)
            dfs(N, res, answer)
            res.pop()
        elif tmp == 9:
            res.append(tmp-1)
            dfs(N, res, answer)
            res.pop()
    return

def main(N):
    answer = 0
    res = []

    dfs(N, res, answer)
    return 

if __name__ == '__main__':
    N = int(input())
    main(N)
