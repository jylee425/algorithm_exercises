N = int(input())
Ns = list(map(int, input().split()))
Os = list(map(int, input().split())) # [p, m, x, d]
on = sum(Os)
assert (on == N-1)

op = []
for i, o in enumerate(Os):
    op = op + [ i for _ in range(o) ]

def compute(n1, o, n2):
    if o == 0:
        return n1 + n2
    elif o == 1:
        return n1 - n2
    elif o == 2:
        return n1 * n2
    elif o == 3:
        return int(n1 / n2)

def run(selected):
    answer = Ns[0]
    for i in range(N-1):
        answer = compute(answer, selected[i], Ns[i+1])
    return answer

mi, ma = float("inf"), -float("inf")
selected = []
visited = [ 0 for _ in range(on) ]
def simulate():
    global mi, ma
    if len(selected) == on:
        tmp = run(selected)
        mi = min(mi, tmp)
        ma = max(ma, tmp)
        return
    else:
        for i in range(on):
            if visited[i] == 0:
                visited[i] = 1
                selected.append(op[i])
                simulate()
                selected.pop()
                visited[i] = 0
simulate()
print(ma, mi, sep="\n")
