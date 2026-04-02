def quick_sort(nums, depth=0):
    print(depth, nums)

    # base case
    if len(nums) <= 1:
        return nums

    # divide
    pivot = nums[-1]
    left_list, right_list = [], []
    for n in nums[:-1]:
        if n < pivot:
            left_list.append(n)
        else:
            right_list.append(n)

    # recursive
    new_left_list = quick_sort(left_list, depth + 1)
    new_right_list = quick_sort(right_list, depth + 1)

    # merge
    return new_left_list + [pivot] + new_right_list


arr = [5, 3, -1, 4, 3, 3, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)
