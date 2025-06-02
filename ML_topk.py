import numpy as np
import heapq


# naive
def topK(arr, K=3):
    sorted_arr = sorted(arr, reverse=True)
    return sorted_arr[:K]


def topK(arr, K):
    heap = arr[:K]
    heapq.heapify(heap)

    for num in arr[K:]:
        if num > heap[0]:
            _ = heapq.heappop(heap)
            heapq.heappush(heap, num)

    return sorted(heap, reverse=True)
