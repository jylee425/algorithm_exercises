def rotate(c):
    if c == 'U':
        UU, LL, FF, RR, BB = U, L, F, R, B
    if c == 'L':
        UU, LL, FF, RR, BB = L, F, U, B, D
    if c == 'F':
        UU, LL, FF, RR, BB = F, U, L, D, R
    if c == 'R':
        UU, LL, FF, RR, BB = R, D, B, U, F
    if c == 'B':
        UU, LL, FF, RR, BB = B, R, D, L, U
    if c == 'D':
        UU, LL, FF, RR, BB = D, B, R, F, L

    UU[0][0], UU[0][1], UU[0][2], \
    UU[1][0], UU[1][1], UU[1][2], \
    UU[2][0], UU[2][1], UU[2][2]  = UU[2][0], UU[1][0], UU[0][0], \
                                    UU[2][1], UU[1][1], UU[0][1], \
                                    UU[2][2], UU[1][2], UU[0][2]

    LL[2][2], LL[2][1], LL[2][0], \
    FF[2][0], FF[1][0], FF[0][0], \
    RR[0][2], RR[1][2], RR[2][2], \
    BB[0][0], BB[0][1], BB[0][2] = FF[2][0], FF[1][0], FF[0][0], \
                                   RR[0][2], RR[1][2], RR[2][2], \
                                   BB[0][0], BB[0][1], BB[0][2], \
                                   LL[2][2], LL[2][1], LL[2][0]


for _ in range(int(input())):
    U = [['w'] * 3 for _ in range(3)]
    D = [['y'] * 3 for _ in range(3)]
    F = [['r'] * 3 for _ in range(3)]
    B = [['o'] * 3 for _ in range(3)]
    L = [['g'] * 3 for _ in range(3)]
    R = [['b'] * 3 for _ in range(3)]

    _ = int(input())
    query = list(input().split())
    for d in query:
        t, c = d[0], d[1]
        if c == '+':
            for _ in range(1): rotate(t)
        if c == '-':
            for _ in range(3): rotate(t)
    for i in range(3):
        for j in range(3):
            print(U[i][j], end="")
        print()
