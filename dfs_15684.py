N, M, H = map(int, input().split())
board = [[0 for _ in range(N + 1)] for _ in range(H + 1)]

def check():
    for i in range(1, N + 1):
        temp = i
        for j in range(1, H + 1):
            if board[j][temp] == 1:
                temp += 1
            elif board[j][temp - 1] == 1:
                temp -= 1
        if temp != i:
            return False
    return True

def simulate(num, cnt):
    global result
    if result != inf:
        return

    if num == cnt:
        if check():
            result = cnt
        return
    else:
        for j in range(1, N):
            for i in range(1, H + 1):
                if board[i][j - 1] == 0 and board[i][j] == 0 and board[i][j + 1] == 0:
                    board[i][j] = 1
                    simulate(num, cnt + 1)
                    board[i][j] = 0

                    while i < H:
                        if board[i][j - 1] or board[i][j + 1]:
                            break
                        i += 1

inf = 4
result = inf
for i in range(M):
    a, b = map(int, input().split())
    board[a][b] = 1
for i in range(4):
    simulate(i, 0)
    if result != inf:
        print(result)
        break
if result == inf:
    print(-1)
