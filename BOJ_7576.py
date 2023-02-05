from collections import deque

direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def bfs(N, M, box):
    # ripe tomatoes
    d = deque()
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1: 
                d.append((i, j, 1))

    # count days
    while(True):
        if len(d) == 0: break

        (x, y, c) = d.popleft()
        # print(x, y, c)


        for dd in direction:
            xx, yy, cc = x + dd[0], y +dd[1], c+1

            if xx < 0 or xx >= N or yy < 0 or yy >= M: continue
            if box[xx][yy] == -1 or box[xx][yy] >= 1: continue

            box[xx][yy] = max(box[xx][yy], cc)
            d.append((xx, yy, cc))


    # check all tomamtoes are riped
    count = 0
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                print(-1)
                return
            else:
                count = max(count, box[i][j])

    print(count-1)
    return

if __name__ == '__main__':
    M, N = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]
    bfs(N, M, box)
