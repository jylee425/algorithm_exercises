N = int( int(input()))
board = [[-1 for _ in range(N)] for _ in range(N)]
prefer = [[] for _ in range(N**2 + 1)]

def seat(st, prefer):
    global board

    st_cand = []
    st_prefer, st_empty = 0, 0
    for x in range(N):
        for y in range(N):
            if board[x][y] > 0: continue

            n_prefer, n_empty = 0, 0
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                tx, ty = x+dx, y+dy
                if tx<0 or tx >= N or ty < 0 or ty >= N: continue
                if board[tx][ty] in prefer: n_prefer += 1
                if board[tx][ty] == -1: n_empty += 1
            if st_prefer < n_prefer:
                st_cand = [(x, y, n_empty, n_prefer)]
                st_prefer = n_prefer
            elif st_prefer == n_prefer:
                st_cand.append((x, y, n_empty, n_prefer))
    st_cand = sorted(st_cand, key= lambda x: x[2], reverse=True)
    board[st_cand[0][0]][st_cand[0][1]] = st

for _ in range(N**2):
    query = list(map(int, input().split()))
    st = query[0]
    prefer[st] = query[1:]

    seat(st, prefer[st])

result = 0
for x in range(N):
    for y in range(N):
        st = board[x][y]

        n_prefer = 0
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            tx, ty = x + dx, y + dy
            if tx < 0 or tx >= N or ty < 0 or ty >= N: continue
            if board[tx][ty] in prefer[st]: n_prefer += 1

        if n_prefer > 0 :
            result += 10 ** (n_prefer-1)

print(result)

