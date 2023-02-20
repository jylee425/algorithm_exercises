
max_ans, min_ans = -1000000000, 1000000000

def dfs(N, Ans, Ops, now, answer):
    global max_ans, min_ans

    if now == N:
        max_ans = max(max_ans, answer)
        min_ans = min(min_ans, answer)
        return
    
    if Ops[0] > 0:
        Ops[0] -= 1
        dfs(N, Ans, Ops, now+1, answer+Ans[now])
        Ops[0] += 1
    if Ops[1] > 0:
        Ops[1] -= 1
        dfs(N, Ans, Ops, now+1, answer-Ans[now])
        Ops[1] += 1
    if Ops[2] > 0:
        Ops[2] -= 1
        dfs(N, Ans, Ops, now+1, answer*Ans[now])
        Ops[2] += 1
    if Ops[3] > 0:
        Ops[3] -= 1
        dfs(N, Ans, Ops, now+1, int(answer/Ans[now]))
        Ops[3] += 1

    return

def main(N, Ans, Ops):
    global max_ans, min_ans
    now = 1
    answer = Ans[0]

    dfs(N, Ans, Ops, now, answer)

    print(max_ans)
    print(min_ans)
    return

if __name__ == '__main__':
    N = int(input())
    Ans = list(map(int, input().split()))
    Ops = list(map(int, input().split()))

    main(N, Ans, Ops)
