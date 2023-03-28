import sys

sys.setrecursionlimit(int(1e4))

def partition(arr, start, end):
    global K, count

    pivot = arr[end]

    # iteration from [start, end-1] to arrange elements <= pivot
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

            count += 1
            if count >= K:
                if arr[i] <= arr[j]: print(arr[i], arr[j])
                else: print(arr[j], arr[i])
                exit(0)

    # iteration is over, so finally place the pivot in the right place
    i, j = i + 1, end
    if i != j:
        arr[i], arr[j] = arr[j], arr[i]
            
        count += 1
        if count >= K:
            if arr[i] <= arr[j]: print(arr[i], arr[j])
            else: print(arr[j], arr[i])
            exit(0)

    return i

def divide_n_conquer(arr, start, end):
    """
    quick sort
    """
    if start < end:
        middle = partition(arr, start, end)

        divide_n_conquer(arr, start, middle-1)
        divide_n_conquer(arr, middle+1, end)

def main(N, K, arr):
    start, end = 0, N-1
    divide_n_conquer(arr, start, end)

    # print(arr)
    print(-1)
    return

if __name__ == '__main__':
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0

    main(N, K, arr)
