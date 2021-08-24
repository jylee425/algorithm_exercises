total = int(input())
numbers = list(map(int, input().split(" ")))
answer = [-1 for _ in range(total)]

stack = []
for i, n in enumerate(numbers):
  if len(stack) == 0 or stack[-1][0] > n:
    stack.append((n,i))
  else:
    while stack[-1][0] < n:
      m, j = stack.pop()
      answer[j] = n
      if len(stack) == 0: break
    stack.append((n,i))

for a in answer:
  print(a, end=" ")
