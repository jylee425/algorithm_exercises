INF = 1e+12

def dp(W, memo, cur, mask):
    """
    tsp problem
        dp[cur][mask] = min(dp[cur][mask | 1 << dst] + W[i][j] for dst)   
    """
    if memo[cur][mask] != 0:
        return memo[cur][mask]

    # all visited, go back to 0
    if mask == (1 << (N-1)) - 1:
        if W[cur][0] != 0:
            return W[cur][0]
        else:
            return INF
    
    result = INF
    for dst in range(1, N):
        if mask & (1 << (dst-1)) != 0:
            continue
        if W[cur][dst] == 0:
            continue
        mask_   = mask | (1 << (dst-1))
        result_ = dp(W, memo, dst, mask_) + W[cur][dst]
        result  = min(result, result_)
    memo[cur][mask] = result
    return memo[cur][mask]

if __name__ == "__main__":
    N = int(input())
    W = [list(map(int, input().split())) for _ in range(N)]
    memo = [[0] * (1 << (N-1)) for _ in range(N)] # dp[pos][visited]

    print(dp(W,memo,0,0)) 

