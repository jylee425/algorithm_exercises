N = int(input())
board = [ list(map(int, input().split())) for _ in range(N) ]

def next(x, y, s):
    result = []

    if s == 0:
        result.append((x  , y+1, 0))
        result.append((x+1, y+1, 2))
    elif s == 1:
        result.append((x+1, y  , 1))
        result.append((x+1, y+1, 2))
    elif s == 2:
        result.append((x  , y+1, 0))
        result.append((x+1, y  , 1))
        result.append((x+1, y+1, 2))

    return result

def check(x, y, s):
    if s == 0 or s == 1:
        if board[x][y] == 1:
            return True
    elif s == 2:
        if board[x-1][y  ] == 1 or \
           board[x  ][y  ] == 1 or \
           board[x  ][y-1] == 1:
            return True
    return False


answer = 0
def dfs():
    global answer 
    #visited = [ [0 for _ in range(N)] for _ in range(N) ]

    queue = [(0,1,0,0)] # initial (x,y,state) = (0,1,0)
    while(queue):
        x, y, s, d = queue.pop()
        #print(f"now: {(x,y,s)}, depth {d}")

        if x == N-1 and y == N-1:
            answer += 1
            continue

        #print(f"next: {next(x,y,s)}")
        for tx, ty, ts in next(x, y, s):
            if tx < 0 or tx >= N or ty < 0 or ty >= N: continue
            if check(tx, ty, ts): continue
            #if visited[tx][ty] == 1: continue

            queue.append((tx, ty, ts, d+1))
            #visited[tx][ty] = 1
    return

dfs()
print(answer)

