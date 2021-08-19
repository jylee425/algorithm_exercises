num = int(input())

stack = []
curr = 0
answer, flag = [], True
while num > 0:
  num -= 1

  now = int(input())
  if curr < now:
    for n in range(curr, now):
      stack.append(n+1)
      answer.append("+")
    curr = now
    stack.pop()
    answer.append("-")
  else:
    answer.append("-")
    n = stack.pop()
    if n != now:
      print("NO")
      flag = False
      break

if flag == True:
  for a in answer:
    print(a)
