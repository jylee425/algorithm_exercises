N = int(input())

dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
def build(x, y, d, g):
    tx, ty = x+dir[d][1], y+dir[d][0]
    curve = [(ty, tx, d)]
    for i in range(g):
        for (_, _, d) in reversed(curve):
            td = (d+1)%4
            tx, ty = tx+dir[td][1], ty+dir[td][0]
            curve.append((ty, tx, td))
    curve.append((y, x, -1))
    return curve

def find(curve):
    res = 0

    for (x, y) in curve:
        if (x-1, y-1) in curve and (x, y-1) in curve and (x-1, y) in curve:
            res += 1
        if (x-1, y) in curve and (x-1, y+1) in curve and (x, y+1) in curve:
            res += 1
        if (x+1, y) in curve and (x+1, y-1) in curve and (x, y-1) in curve:
            res += 1
        if (x+1, y) in curve and (x+1, y+1) in curve and (x, y+1) in curve:
            res += 1
    return res

board = []
for i in range(N):
    x, y, d, g = map(int, input().split())
    board += build(x, y, d, g)

board_ = []
for (x, y, _) in board:
    board_.append((x, y))
board = list(set(board_))

board = sorted(board, key=lambda x: (x[0], x[1]))
print(find(board)//4)
