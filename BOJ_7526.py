from collections import deque

move = [(-1, 2), (1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, 1), (2, -1)]

def bfs(K, src_x, src_y, dst_x, dst_y):
    board = [[0] * K for _ in range(K)]
    deq = deque()

    deq.append((src_x, src_y)) 
    board[src_x][src_y] = 1

    while(True):
        if len(deq) == 0: break

        x, y = deq.popleft()
        c = board[x][y]
        if x == dst_x and y == dst_y:
            print(c-1)
            return

        for (dx, dy) in move:
            xx, yy, cc = x + dx, y + dy, c + 1

            if xx < 0 or xx >= K or yy < 0 or yy >= K: continue
            if board[xx][yy] != 0: continue

            board[xx][yy] = cc 
            deq.append((xx, yy))



def main(N):
    for _ in range(N):
        K = int(input())
        src_x, src_y = map(int, input().split())
        dst_x, dst_y = map(int, input().split())

        bfs(K, src_x, src_y, dst_x, dst_y)

    return

if __name__ == '__main__':
    N = int(input())
    main(N)
