answers = []
while(True):
    answer = 0

    inputs = list(map(int, input().split()))
    if (inputs[0]) == 0 : break

    stack = []
    for i in range(1, inputs[0]+1):
        right = i-1
        while(len(stack) > 0 and inputs[stack[-1]]>inputs[i]):
            tmp = stack.pop()
            left = 1 if len(stack) == 0 else stack[-1] + 1
            answer = max(answer, inputs[tmp]*(right-left+1))
        stack.append(i)    

    right = inputs[0]
    while(len(stack)>0):
        tmp = stack.pop()
        left = 1 if len(stack) == 0 else stack[-1] + 1
        answer = max(answer, inputs[tmp]*(right-left+1))

    answers.append(answer)

for a in answers:
    print(a)