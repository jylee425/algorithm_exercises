def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left, equal, right = [], [], []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            equal.append(num)
        else:
            right.append(num)

    return quick_sort(left) + equal + quick_sort(right)

N = int(input())
ns = []
for i in range(N):
    ns.append(int(input()))

ns_ = quick_sort(ns)
for n in ns_:
    print(n)
