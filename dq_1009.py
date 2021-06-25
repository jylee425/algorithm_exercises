import sys
sys.setrecursionlimit(10000)

def pow(a, b, m) :
    if (b == 1):
        return (a % m)

    tmp = pow(a, b // 2, m)
    
    if (b % 2 == 0):
        return tmp*tmp % m
    else:
        return tmp*tmp * a % m

test_num = int(input())

def conv(n):
    return 10 if n == 0 else n

for _ in range(test_num):
    a, b = map(int, input().split())
    print(conv(pow(a, b, 10)))