while(True):
    line = input()

    if line == '.':
        break
    
    stack = []
    flag = 1
    for c in line:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 or stack[-1] != '(':
                flag = 0
                break
            else:
                stack.pop()
        elif c == '[':
            stack.append(c)
        elif c == ']':
            if len(stack) == 0 or stack[-1] != '[':
                flag = 0
                break
            else:
                stack.pop()

    print("yes" if flag and len(stack) == 0 else "no")