def heappush(heap, x):
    heap.append(x)

    current = len(heap) - 1
    while True:
        if current == 0:
            break

        parent = (current - 1) // 2

        # compare with parent
        if heap[current] < heap[parent]:
            heap[current], heap[parent] = heap[parent], heap[current]
            current = parent
        else:
            break

    return


def heappop(heap):
    if len(heap) == 0:
        return 0
    if len(heap) == 1:
        return heap.pop()

    # pop the toppest data
    data, heap[0] = heap[0], heap.pop()

    current, child = 0, 1
    while True:

        if child >= len(heap):
            break

        sibling = child + 1

        if sibling < len(heap) and heap[sibling] < heap[child]:
            child = sibling

        if heap[current] > heap[child]:
            heap[current], heap[child] = heap[child], heap[current]
            current = child
            child = current * 2 + 1  # left child
        else:
            break

    return data


if __name__ == "__main__":
    N = int(input())

    heap = []

    for _ in range(N):
        x = int(input())

        if x == 0:
            print(heappop(heap))

        else:
            heappush(heap, x)
