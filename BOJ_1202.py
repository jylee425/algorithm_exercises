import heapq
MAX_VALUE = 1000000 + 1

def greedy(Cs):
    """
    Args:
        Js: (mass, value)'s of jewerly + (storage of bags, max_value+1)

    Return:
        Maximum value of total jewerly
    """
    value = 0
    # print(Js)

    tmp = []
    for (_, V) in Cs:
        if V != MAX_VALUE:
            heapq.heappush(tmp, -V)
        elif V == MAX_VALUE:
            # print(tmp)
            if len(tmp) > 0:
                value -= heapq.heappop(tmp)

    return value

if __name__ == "__main__":
    N, K = map(int, input().split())
    Js = [tuple(map(int, input().split())) for _ in range(N)]
    Cs = [tuple((int(input()), MAX_VALUE)) for _ in range(K)]

    Js += Cs
    Js = sorted(Js, key = lambda J: J[0])
    print(greedy(Js))

