def binary_search(arr, left, right, target):
    while(left <= right):
        mid = (left+right)//2
        if arr[mid] == target:
            return 1
        else:
            if arr[mid] > target:
                right = mid-1
            else:
                left = mid+1
    return 0

N = int(input())
Ns = map(int, input().split())
M = int(input())
Ms = map(int, input().split())

Ns = sorted(Ns)
for m in Ms:
    print(binary_search(Ns, 0, N-1, m))
