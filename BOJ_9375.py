from collections import defaultdict

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        N = int(input())

        tools = defaultdict(list)
        for _ in range(N):
            name, slot = map(str, input().split())
            tools[slot].append(name)

        combinations = 1
        for k, v in tools.items():
            combinations *= len(v) + 1
        print(combinations - 1)
