answers = []
while(True):
    answer = 0

    inputs = list(map(int, input().split()))
    if (inputs[0]) == 0 : break

    stack = []
    for i in range(1, inputs[0]+1):
        right = i-1
        while(len(stack) > 0 and stack[-1][1]>inputs[i]):
            tmp = stack.pop()
            left = tmp[0]
            height = tmp[1]
            answer = max(answer, (right-left+1)*height)
        stack.append([i, inputs[i]])    

    right = len(stack)
    while(len(stack)>0):
        tmp = stack.pop()
        left = tmp[0]
        height= tmp[1]
        answer = max(answer, height * (right - left + 1))

    answers.append(answer)

for a in answers:
    print(a)