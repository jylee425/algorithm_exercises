from itertools import permutations

if __name__ == "__main__":
    N, M = map(int, input().split())
    nums = sorted(list(map(int, input().split())))

    for comb in sorted(set(permutations(nums, M))):
        print(" ".join(map(str, comb)))
