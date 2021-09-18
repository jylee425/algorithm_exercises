N, M = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N) ]

home, chicken = [], []
for x in range(N):
    for y in range(N):
        if board[x][y] == 1: home.append((x,y))
        elif board[x][y] == 2: chicken.append((x,y))


def calculate(chicken):
    res = 0
    for h in home:
        res += min([ abs(h[0] - c[0]) + abs(h[1] - c[1]) for c in chicken])
    return res


def simulate(count, cur):
    global answer, visited

    if count == M:
        selected = [ chicken[i] for i in range(len(chicken)) if visited[i]]
        answer = min(answer, calculate(selected))
        return
    else:
        for i in range(cur, len(chicken)):
            if visited[i] == 0:
                visited[i] = 1
                simulate(count+1, i+1)
                visited[i] = 0


answer = float("inf")
visited = [0] * len(chicken)
simulate(0, 0)
print(answer)
