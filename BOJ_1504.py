import heapq
from collections import defaultdict


def dijkstra(start, connections, N):
    distances = [1e9 for _ in range(N + 1)]

    q = []
    heapq.heappush(q, (start, 0))
    distances[start] = 0
    while q:
        curr, dist_to_curr = heapq.heappop(q)

        if distances[curr] < dist_to_curr:
            continue

        for target, dist_to_target in connections[curr]:
            dist_new = dist_to_curr + dist_to_target
            if distances[target] < dist_new:
                continue

            distances[target] = dist_new
            heapq.heappush(q, (target, dist_new))

    return distances


if __name__ == "__main__":
    N, M = map(int, input().split())
    connections = defaultdict(list)
    for _ in range(M):
        src, dst, cost = map(int, input().split())
        connections[src].append([dst, cost])
        connections[dst].append([src, cost])
    v1, v2 = map(int, input().split())

    # get answer
    a = dijkstra(1, connections, N)
    b = dijkstra(v1, connections, N)
    c = dijkstra(v2, connections, N)

    answer = min(a[v1] + b[v2] + c[N], a[v2] + c[v1] + b[N])

    if answer >= 1e9:
        print(-1)
    else:
        print(answer)
