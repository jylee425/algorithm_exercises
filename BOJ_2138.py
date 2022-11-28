import copy

def toggle(arr, idx):
    """
    Return:
        switch the idx-th light
    """
    if idx == 0:
        arr[idx], arr[idx+1] = int(not arr[idx]), int(not arr[idx+1])
    elif 0 < idx < N-1:
        arr[idx-1], arr[idx], arr[idx+1] \
                             = int(not arr[idx-1]), int(not arr[idx]), int(not arr[idx+1])
    elif idx == N-1:
        arr[idx-1], arr[idx] = int(not arr[idx-1]), int(not arr[idx])
    
    return arr

def greedy(sta, end):
    """
    Args:
        sta: current state of the lights
        end: target end state of the lights
    Return:
        number of transitions needed
    """
    N = len(sta)

    # first off
    cur = copy.deepcopy(sta)
    off_can = False

    off_cnt = 0
    for i in range(1, N):
        if cur[i-1] != end[i-1]:
            cur = toggle(cur, i)
            off_cnt += 1
    if cur == end:
        off_can = True

    # first on
    cur = copy.deepcopy(sta)
    on_can = False

    on_cnt = 1
    toggle(cur, 0)
    for i in range(1, N):
        if cur[i-1] != end[i-1]:
            cur = toggle(cur, i)
            on_cnt += 1
    if cur == end:
        on_can = True

    if off_can:
        if on_can: res = min(off_cnt, on_cnt)
        else:      res = off_cnt
    else:
        if on_can: res = on_cnt
        else:      res = -1
    return res

if __name__ == "__main__":
    N = int(input())
    cur = list(map(int, list(input())))
    end = list(map(int, list(input())))

    print(greedy(cur, end))
