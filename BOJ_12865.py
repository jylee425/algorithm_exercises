import sys

sys.setrecursionlimit(1e6)

answer = -1


def dfs(K, weights, values, curr, packed):
    global answer

    if curr >= len(weights):
        return

    # check
    sum_of_packed_weights, sum_of_packed_values = 0, 0
    for p in packed:
        sum_of_packed_weights += weights[p]
        sum_of_packed_values += values[p]

    if sum_of_packed_weights <= K:
        if answer == -1 or (answer < sum_of_packed_values):
            answer = sum_of_packed_values
    else:
        return

    # print(curr, packed, answer)

    dfs(K, weights, values, curr + 1, packed + [curr])
    dfs(K, weights, values, curr + 1, packed)
    return


if __name__ == "__main__":
    N, K = map(int, input().split())

    weights, values = [], []
    for _ in range(N):
        W, V = map(int, input().split())
        weights.append(W)
        values.append(V)

    # dfs
    dfs(K, weights, values, curr=0, packed=[])
    print(answer)
