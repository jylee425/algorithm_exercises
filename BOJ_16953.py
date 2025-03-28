if __name__ == "__main__":
    A, B = map(int, input().split())

    # bfs
    found = False
    q = [(A, 0)]
    while q:
        curr, step = q.pop(0)
        # print(curr, step)

        if curr == B:
            found = True
            print(step + 1)
            break

        for next in [2 * curr, curr * 10 + 1]:
            if next > B:
                continue

            q.append((next, step + 1))

    if not found:
        print(-1)
