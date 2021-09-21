N, M = map(int, input().split())
Ns = range(1, N+1)
visited = [0] * N

answers = []
def simulate(cnt, selected):
    if cnt == M:
        answer = ""
        for s in selected:
            answer += str(s) + " "
        answers.append(answer)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            selected.append(Ns[i])
            simulate(cnt+1, selected)
            selected.pop()
            visited[i] = 0
simulate(0, [])

answers = sorted(list(set(answers)))
for a in answers:
    print(a)
