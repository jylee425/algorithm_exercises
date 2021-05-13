def is_one(r, c, s, N, K):
    s = s - 1

    if N%2 == 0: mid = (N-K)//2
    else: mid = (N-K+1)//2

    if s <= 0 :
        res_r = r % N 
        res_c = c % N 

        if( (res_r+1 > mid) and (res_r+1 <= mid+K) ) :
                if( (res_c+1 > mid) and (res_c+1 <= mid+K) ) :       
                    return 1
        return 0
    else :
        res_r = r // (N**s)
        res_c = c // (N**s)

        if( (res_r+1 > mid) and (res_r+1 <= mid+K) ) :
                if( (res_c+1 > mid) and (res_c+1 <= mid+K) ) :       
                    return 1
        return is_one(r % (N**s), c % (N**s), s, N, K)

s, N, K, R1, R2, C1, C2 = map(int, input().split())

for r in range(R1, R2+1):
    for c in range(C1, C2+1):
        i = is_one(r,c,s,N,K)
        print(i, end="")
    print()