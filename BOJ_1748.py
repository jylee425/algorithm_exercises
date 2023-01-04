
def greedy(N):
    L = len(N) - 1

    c, i = 0, 0
    while True:
        if i >= L: break

        digits = 9 * (10 ** i)
        c += digits * (i + 1)

        i += 1
    remainder = (int(N) - 10 ** L) + 1
    c += remainder * (L + 1)

    return c

if __name__ == '__main__':
    N = input()

    print(greedy(N))
