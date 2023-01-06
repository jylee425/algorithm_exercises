
ans = -int(1e10)

def helper(selected, i, j):
    direction = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

    for d in direction:
        ii, jj = i + d[0], j + d[1]
        
        if (ii, jj) in selected:
            return False
    return True

def dfs(x, y, N, M, K, board, selected, cur):
    global ans
    # print('in dfs', selected, cur)

    if len(selected) >= K:
        ans = max(ans, cur)
        # print(ans)
        return 

    for i in range(x, N):
        for j in range(y if i == x else 0, M):
            if helper(selected, i, j):
                selected.append((i, j))
                dfs(i, j, N, M, K, board, selected, cur+board[i][j])
                selected.pop()
    return 
            


def main(N, M, K, board):
    global ans

    selected = []
   
    dfs(0, 0, N, M, K, board, selected, 0)
    print(ans)
    return

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    main(N, M, K, board)
