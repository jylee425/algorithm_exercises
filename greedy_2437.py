chooNum = int(input())
choos = list(map(int,input().split()))
choos = sorted(choos)

target = 1
for i in choos:
  if target<i:
    break
  target+=i

print(target)