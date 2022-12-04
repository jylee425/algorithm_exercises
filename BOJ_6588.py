MAX = 1000000

def dp():
    """
    sieve of era
    """
    global memo
    memo = [1] * (MAX + 1)

    max_iter = int(MAX ** 0.5) + 1
    for i in range(2, max_iter):
        if memo[i]:
            for j in range(i*2, MAX, i) : 
                if memo[j]: memo[j] = 0


if __name__ == '__main__':
    dp()

    while(True):
        n = int(input())
        if n == 0: break

        for i in range(3, MAX):
            if memo[i]:
                if memo[n-i]:
                    print(f"{n} = {i} + {n-i}")
                    break
