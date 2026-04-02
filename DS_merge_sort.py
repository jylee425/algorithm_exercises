from typing import List


def merge_sort(nums: List[int], depth=0):
    print(depth, nums)

    # base case
    if len(nums) <= 1:
        return nums

    # recursive
    left, right = 0, len(nums) - 1
    mid = (left + right) // 2
    print("\t", depth, mid)
    left_sorted = merge_sort(nums[left : mid + 1], depth + 1)
    right_sorted = merge_sort(nums[mid + 1 : right + 1], depth + 1)

    # merge
    merge_sorted = []

    i, j = 0, 0
    while i < len(left_sorted) and j < len(right_sorted):
        left_elt = left_sorted[i]
        right_elt = right_sorted[j]
        if left_elt <= right_elt:
            merge_sorted.append(left_elt)
            i += 1
        else:
            merge_sorted.append(right_elt)
            j += 1

    if i < len(left_sorted):
        merge_sorted += left_sorted[i:]
    if j < len(right_sorted):
        merge_sorted += right_sorted[j:]

    return merge_sorted


arr = [1, 2, -1, 2, 5, 3, 4, 5, 3, 3, 4]
sorted_arr = merge_sort(arr)
print(sorted_arr)
