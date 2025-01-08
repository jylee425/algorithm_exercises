if __name__ == "__main__":
    N, M = map(int, input().split())
    array = list(map(int, input().split()))

    S = [0]
    acc_sum = 0
    for i in range(N):
        acc_sum += array[i]
        S.append(acc_sum)

    # print(S)
    for _ in range(M):
        src, dst = map(int, input().split())
        print(S[dst] - S[src - 1])
