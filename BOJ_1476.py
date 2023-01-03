
def brute_force(E,S,M):
    for i in range(1, 99999999):
        if i % 15 == E % 15 and i % 28 == S % 28 and i % 19 == M % 19:
            print(i)
            return

if __name__ == '__main__':
    E, S, M = map(int, input().split())

    brute_force(E,S,M)
