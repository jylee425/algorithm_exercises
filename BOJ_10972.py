
def bruteforce(N, seq):

    # step 1
    for i in range(N-1, 0, -1):
        if seq[i-1] < seq[i]:
            k = i-1

            # step 2
            for m in range(N-1, 0, -1):
                if seq[k] < seq[m]:
                    seq[k], seq[m] = seq[m], seq[k]

                    # step 3
                    seq = seq[:k+1] + sorted(seq[k+1:])
                    print(*seq)
                    return

    print(-1)
    return

if __name__ == '__main__':
    N = int(input())
    seq = list(map(int, input().split()))
    
    if N <= 1:
        print(-1)
    else:
        bruteforce(N, seq)

