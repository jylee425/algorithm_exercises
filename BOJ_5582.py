import sys
input = sys.stdin.readline


def dp(S1, S2):
    res = 0
    memo = [[0] * (len(S2) + 1) for _ in range(len(S1) + 1)]

    for i in range(1, len(S1)):
        for j in range(1, len(S2)):
            # print(i, j, i-1, j-1, S1[i-1], S2[j-1])
            if S1[i-1] == S2[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
                res = max(res, memo[i][j]) 
                # print('**', memo[i][j])
    return res 


def main(S1, S2):
    print(dp(S1, S2))
    return

if __name__ == '__main__':
    S1 = input()
    S2 = input()
    main(S1, S2)
