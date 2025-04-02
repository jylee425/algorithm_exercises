import heapq
from collections import defaultdict


def stringfy(x):
    return "INF" if x == 1e9 else str(x)


if __name__ == "__main__":
    V, E = map(int, input().split())
    start = int(input())
    graph = defaultdict(list)
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    # dijsktra
    dists = [1e9] * (V + 1)
    dists[start] = 0

    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)

        if dists[node] < dist:
            continue

        for next_node, next_dist in graph[node]:
            new_dist = dist + next_dist
            if dists[next_node] > new_dist:
                dists[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))

    print("\n".join(map(stringfy, dists[1:])))
