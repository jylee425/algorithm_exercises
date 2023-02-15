import sys
input = sys.stdin.readline

MAX = 1000000
memo = [1] * (MAX + 1)

def dp():
    """
    sieve of era
    """
    global memo

    max_iter = int(MAX ** 0.5) + 1
    for i in range(2, max_iter):
        if memo[i]:
            for k in range(2*i, MAX, i):
                memo[k] = 0


if __name__ == '__main__':
    dp()

    while(True):
        n = int(input())
        if n == 0: break

        for i in range(3, MAX):
            if memo[i] and memo[n-i]:
                print(f"{n} = {i} + {n-i}")
                break
