N = int(input())
factory = list(map(int, input().split()))
for _ in range(3): factory.append(0)

answer = 0
for i in range(N):
    if factory[i+1] > factory[i+2]:
        number = min(factory[i], factory[i+1]-factory[i+2])
        answer += 5 * number
        for ii in range(2):
            factory[i+ii] -= number

        number = min(factory[i], factory[i+1], factory[i+2])
        answer += 7 * number
        for ii in range(3):
            factory[i+ii] -= number
    else:
        number = min(factory[i], factory[i + 1], factory[i + 2])
        answer += 7 * number
        for ii in range(3):
            factory[i+ii] -= number

        number = min(factory[i], factory[i + 1])
        answer += 5 * number
        for ii in range(2):
            factory[i + ii] -= number

    answer += 3 * factory[i]
    factory[i] = 0
print(answer)
