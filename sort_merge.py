def mergeSort(arr):
    size = len(arr)
    if size <= 1:
        pass
    else:
        pivot = size//2
        left, right = mergeSort(arr[:pivot]), mergeSort(arr[pivot:])

        # Merge
        idx, src, dst = 0, 0, 0
        while(src < pivot and dst < size-pivot):
            if left[src] < right[dst]:
                arr[idx] = left[src]
                src += 1
            else:
                arr[idx] = right[dst]
                dst += 1
            idx += 1
        if src == pivot :
            arr[idx:] = right[dst:]
        if dst == size-pivot:
            arr[idx:] = left[src:]
    return arr

if __name__ == "__main__":
    # https://www.acmicpc.net/problem/2750
    arr = list()
    size = int(input())

    for i in range(size):
        arr.append(int(input()))

    res = mergeSort(arr)
    print(*res, sep='\n')