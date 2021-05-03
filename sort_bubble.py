N, K = map(int, input().split(' '))
numbers = list(map(int, input().split(' ')))

for i in range(N):
    ii = N-1-i
    for j in range(ii):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        else:
            continue

for n in numbers:
    print(n, end=" ")