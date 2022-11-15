

def compute(N, R, C, depth=0):
    if N == 1:
        return R * 2 + C  

    thres = 2 ** (N-1)
    if R < thres and C < thres:
        return 4 ** (N-1) * 0 + compute(N-1, R, C, depth+1)
    if R < thres and C >= thres:
        return 4 ** (N-1) * 1 + compute(N-1, R, C - thres, depth+1)
    if R >= thres and C < thres:
        return 4 ** (N-1) * 2 + compute(N-1, R - thres, C, depth+1)
    if R >= thres and C >= thres:
        return 4 ** (N-1) * 3 + compute(N-1, R - thres, C - thres, depth+1)

if __name__ == "__main__":
    N, R, C = map(int, input().split())

    if N == 0:
        print(1)
    else:
        print(compute(N, R, C))


