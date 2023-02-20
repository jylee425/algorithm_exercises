
max_ans = -1

def bruteforce(N, W, answer):
    global max_ans
    # print(W)

    if len(W) == 2:
        max_ans = max(max_ans, answer)
        return

    for i in range(1, len(W)-1):
        tmp = W[i-1] * W[i+1]

        cur = W.pop(i)
        bruteforce(N, W, answer+tmp)
        W.insert(i, cur)

    return


def main(N, W):
    answer = 0

    bruteforce(N, W, answer)
    print(max_ans)
    return

if __name__ == '__main__':
    N = int(input())
    W = list(map(int, input().split()))

    main(N, W)
