N = int(input())
numbers = list(map(int, input().split()))

memo = [1 for _ in range(N)]
src = [-1 for _ in range(N)]
for i, n in enumerate(numbers):
    for j, m in enumerate(numbers[i:]):
        if m > n:
            if memo[i]+1 > memo[i+j]:
                memo[i+j] = memo[i]+1
                src[i+j] = i

res = []
t = max(range(N), key=lambda i: memo[i])
while(src[t] != -1):
    res.append(numbers[t])
    t = src[t]
res.append(numbers[t])

print(max(memo))
for i in res[::-1]:
    print(i, end=" ")
