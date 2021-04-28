userinput = 1000-int(input())
result = [0, 0, 0, 0, 0, 0]

if(userinput // 500 != 0):
    result[0] += userinput//500
    userinput %= 500
if(userinput // 100 != 0):
    result[1] += userinput//100
    userinput %= 100
if(userinput // 50 != 0):
    result[2] += userinput//50
    userinput %= 50
if(userinput // 10 != 0):
    result[3] += userinput//10
    userinput %= 10
if(userinput // 5 != 0):
    result[4] += userinput//5
    userinput %= 5
if(userinput // 1 != 0):
    result[5] += userinput//1
    userinput %= 1

print(sum(result))