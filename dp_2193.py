N = int(input())
D = [[0,0] for _ in range(100)]

D[0] = [1, 1]
for i in range(1,N+1):
    D[i][0] = D[i-1][0] + D[i-1][1]
    D[i][1] = D[i-1][0]
print(D[N-1][1])