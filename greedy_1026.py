N = int(input())
A = map(int, input().split())
B = map(int, input().split())

A = sorted(A, reverse=False)
B = sorted(B, reverse=True)

S = 0 
for (i,j) in zip(A, B):
    S += i*j
print(S)