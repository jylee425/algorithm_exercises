import sys
input = sys.stdin.readline


def bruteforce(N, seq):
    """
    1. from reverse, find where k it is not descending order
    2. from there, find where m it is less than there (starting from the back again) - and swap k & m
    3. rearrange seq = seq[:k+1] + reversed(seq[k+1:]) 
    """
    
    # step 1
    k = -1
    for i in range(N-1, 0, -1):
        if seq[i-1] > seq[i]:
            k = i-1

            # step 2
            for j in range(N-1, k, -1):
                if seq[j] < seq[k]:
                    seq[j], seq[k] = seq[k], seq[j]
                    break

            # step 3
            seq = seq[:k+1] + sorted(seq[k+1:], reverse = True)
            
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
