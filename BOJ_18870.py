if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    arr_set = sorted(list(set(arr)))
    arr_dict = {arr_set[i]: i for i in range(len(arr_set))}
    result = [arr_dict[arr[i]] for i in range(N)]
    print(*result)
