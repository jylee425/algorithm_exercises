from itertools import combinations_with_replacement

if __name__ == "__main__":
    N, M = map(int, input().split())
    nums = set(map(int, input().split()))

    selections = combinations_with_replacement(sorted(nums), M)
    for selection in selections:
        print(" ".join(map(str, selection)))
