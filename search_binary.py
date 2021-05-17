def binarySearch(array, target, left, right):
    while left <= right:
        mid = (left+right)//2
        if array[mid] == target:
            return mid
        elif array[mid]>target:
            right = mid-1
        else :
            left = mid+1
    return -1

def binarySearchBound(array, target):
    lowerBound, upperBound = -1, -1
    
    # Lower Bound
    left = 0
    right = len(array)
    while left < right:
        mid = (left+right)//2
        if array[mid]>=target:
            right = mid
        else:
            left = mid + 1
    lowerBound = left

    # Upper Bound
    left = 0
    right = len(array)
    while left < right:
        mid = (left+right)//2
        if array[mid]<=target:
            left = mid+1
        else :
            right = mid
    upperBound = right

    return lowerBound, upperBound

if __name__ == "__main__":
    # https://www.acmicpc.net/problem/10815
    '''
    repoNum = int(input())
    repo = list(map(int, input().split()))
    targetNum = int(input())
    target = list(map(int, input().split()))
    repo.sort()

    for tt in target:
        if binarySearch(repo, tt, 0, repoNum-1) < 0 :
            print(0, end=" ")
        else:
            print(1, end=" ")
    '''

    # https://www.acmicpc.net/problem/10816
    repoNum = int(input())
    repo = list(map(int, input().split()))
    targetNum = int(input())
    target = list(map(int, input().split()))
    repo.sort()

    for tt in target:
        start, end = binarySearchBound(repo, tt)
        print(end-start, end=" ")