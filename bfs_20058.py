import sys
sys.setrecursionlimit(10000)

N, Q = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(2**N) ]
query = list(map(int, input().split()))

def rotate(b, L):
    res = [[-1 for _ in range(2**N)] for _ in range(2**N)]
    for i in range(0, len(b), 2**L):
        for j in range(0, len(b), 2**L):
            for r in range(0, 2**L):
                for c in range(0, 2**L):
                    res[i+r][j+c] = board[i+(-1-c)%2**L][j+r]
    return res

def melt(b):
    res = [[-1 for _ in range(2**N)] for _ in range(2**N)]

    for x in range(len(b)):
        for y in range(len(b)):
            count = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                tx, ty= x + dx, y + dy
                if tx < 0 or tx >= len(b) or ty < 0 or ty >= len(b): continue
                if b[tx][ty] > 0: count += 1

            if count < 3:
                res[x][y] = max(b[x][y] - 1, 0)
            else:
                res[x][y] = b[x][y]
    return res

# bfs
visited = [[0 for _ in range(2**N)] for _ in range(2**N)]
def count(b, x, y, c):
    global visited

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        tx, ty, tc = x + dx, y + dy, c+1
        if tx < 0 or tx >= len(b) or ty < 0 or ty >= len(b): continue
        if visited[tx][ty]: continue
        visited[tx][ty] = 1
        if b[tx][ty] > 0:
            c = max(c, count(b, tx, ty, tc))
    return c


for q in query:
    board = rotate(board, q)
    board = melt(board)

answer1, answer2 = 0, 0
for i in range(2**N):
    answer1 += sum(board[i])
    for j in range(2**N):
        answer2 = max(answer2, count(board, i, j, 0))
print(answer1)
print(answer2)
