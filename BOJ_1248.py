
def check(idx, res):
    total_sum = 0
    for i in range(idx, -1, -1):
        total_sum += res[i]

        if total_sum == 0 and S[i][idx] != 0:
            return False
        elif total_sum < 0 and S[i][idx] >= 0:
            return False
        elif total_sum > 0 and S[i][idx] <= 0:
            return False
    return True

def dfs(N, S, idx, res):
    if idx == N:
        return True

    if S[idx][idx] == 0:
        res[idx] = 0
        return dfs(N, S, idx+1, res)
    for i in range(1, 10+1):
        res[idx] = i * S[idx][idx]
        
        if check(idx, res) and dfs(N, S, idx+1, res):
            return True
    return False


def main(N, S):
    idx = 0
    res = [0] * N

    dfs(N, S, idx, res)
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    N = int(input())
    
    arr = list(input())
    S = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i, N):
            sign = arr.pop(0)
            if sign == '+': S[i][j] = 1
            elif sign == '-': S[i][j] = -1

    main(N, S)
