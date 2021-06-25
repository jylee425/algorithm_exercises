N = int(input())
d = map(int, input().split())
d = sorted(d, reverse=False)
print(d[0]*d[-1])