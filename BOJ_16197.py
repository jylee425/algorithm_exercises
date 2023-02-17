from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(n, m, board, coin):
    while coin:
        x1, y1, x2, y2, cnt = coin.popleft()

        if cnt >= 10:
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]

            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                if board[nx1][ny1] == "#": nx1, ny1 = x1, y1
                if board[nx2][ny2] == "#": nx2, ny2 = x2, y2
                coin.append((nx1, ny1, nx2, ny2, cnt + 1))
            elif 0 <= nx1 < n and 0 <= ny1 < m: 
                return cnt + 1
            elif 0 <= nx2 < n and 0 <= ny2 < m: 
                return cnt + 1
            else:  # 둘 다 빠진 경우
                continue

    return -1

def main(N, M, board):
    coin = deque()

    temp = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == "o":
                temp.append((i, j))

    coin.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0))
    print(bfs(N, M, board, coin))
    return

if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [ list(input()) for _ in range(N) ]
    # print(board)

    main(N, M, board)
