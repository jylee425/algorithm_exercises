dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, board, count):
    global answer
    answer = max(answer, count)

    for i in range(4):

        nx = dx[i] + x
        ny = dy[i] + y

        if nx <= -1 or nx >= r or ny <= -1 or ny >= c:
            continue

        if visited[ord(board[nx][ny]) - 65] == 0:
            visited[ord(board[nx][ny]) - 65] = 1
            dfs(nx, ny, board, count + 1)
            visited[ord(board[nx][ny]) - 65] = 0


if __name__ == "__main__":

    r, c = map(int, input().split())
    board = []
    for _ in range(r):
        board.append(list(map(str, input())))

    visited = [0] * 26
    visited[ord(board[0][0]) - 65] = 1

    answer = 1

    dfs(0, 0, board, 1)

    print(answer)
