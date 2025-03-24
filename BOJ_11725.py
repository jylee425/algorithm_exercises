from collections import defaultdict

if __name__ == "__main__":
    N = int(input())

    # connections
    connections = defaultdict(list)
    for _ in range(N - 1):
        i, j = map(int, input().split())

        connections[i].append(j)
        connections[j].append(i)

    # get parents
    parent = defaultdict(lambda: 0)

    visited = [0 for _ in range(N)]
    targets = [1]
    while True:
        if len(targets) == 0:
            break

        t = targets.pop(0)

        if visited[t - 1]:
            continue
        else:
            visited[t - 1] = 1

        connection_t = connections[t]

        for c in connection_t:
            if parent[c] == 0:
                parent[c] = t

        targets += connection_t

    # print
    for k in sorted(parent.keys())[1:]:
        print(parent[k])
