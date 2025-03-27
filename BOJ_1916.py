import heapq
from collections import defaultdict

if __name__ == "__main__":
    N = int(input())
    M = int(input())

    # get connections
    connections = defaultdict(list)
    for _ in range(M):
        src, dst, cost = map(int, input().split())
        connections[src].append([dst, cost])
    start, end = map(int, input().split())

    # dijstrak's algorithm
    distances = [1e9 for _ in range(N + 1)]

    q = []
    heapq.heappush(q, (0, start))

    while q:
        distance, curr = heapq.heappop(q)

        # visited
        if distances[curr] < distance:
            continue

        # update
        for target, cost in connections[curr]:
            distance_new = distance + cost
            if distance_new >= distances[target]:
                continue

            distances[target] = distance_new
            heapq.heappush(q, (distance_new, target))

    # print
    print(distances[end])
