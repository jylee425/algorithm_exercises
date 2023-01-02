
def get_coeffs(arr):
    """
    arr[i] = arr[i-1] * a + b

    Return:
        a, b
    """
    a = int((arr[2] - arr[1]) / (arr[1] - arr[0]))
    b = arr[1] - (a * arr[0])
    return a, b

def is_same_nums(arr):
    """
    Return:
        whether is the given array is composed of consecutive numbers or not 
    """
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            pass
        else:
            return False
    return True

def brute_force(arr):
    """
    arr[i] = arr[i-1] * a + b

    Return:
        a, b
    """
    N = len(arr)

    if N == 1:
        return 'A'
    elif N == 2:
        if arr[0] == arr[1]:
            return arr[1]
        else:
            return 'A'
    else:
        if arr[0] == arr[1]:
            if is_same_nums(arr):
                return arr[-1]
            else:
                return 'B'
            
    
        # match with the prediction
        pred = [arr[0]]
        a, b = get_coeffs(arr)
        for i in range(1, N):
            pred.append(a*arr[i-1]+b)
            
        if pred == arr:
            return a*arr[-1]+b
        else:
            return 'B'

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))

    print(brute_force(arr))
