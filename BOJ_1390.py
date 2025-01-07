from collections import defaultdict


def bfs(current, edges, N):
    kevin_bacon_nums = [0 if i == current else -1 for i in range(N)]

    queue = []
    for t in list(edges[current]):
        queue.append((t, 1))

    while True:
        if len(queue) <= 0:
            break

        if not (-1 in kevin_bacon_nums):
            break

        (target, target_num) = queue.pop(0)
        if kevin_bacon_nums[target] == -1:
            kevin_bacon_nums[target] = target_num

            for t in list(edges[target]):
                queue.append((t, target_num + 1))

    return sum(kevin_bacon_nums)


if __name__ == "__main__":
    N, M = map(int, input().split())

    edges = defaultdict(list)

    for _ in range(M):
        src, dst = map(int, input().split())

        edges[src - 1].append(dst - 1)
        edges[dst - 1].append(src - 1)

    for k, v in edges.items():
        edges[k] = set(v)

    answer, lowest_kevin_bacon_num = -1, 999999999999
    for n in range(N):
        kevin_bacon_num = bfs(n, edges, N)
        if lowest_kevin_bacon_num > kevin_bacon_num:
            answer = n
            lowest_kevin_bacon_num = kevin_bacon_num
    print(answer + 1)
