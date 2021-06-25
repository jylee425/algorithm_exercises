N = int(input())

words = []
for _ in range(N):
    words.append(input())

answer = []
for i, w in enumerate(words[0]):
    flag = True
    for j in range(1, N):
        if w != words[j][i] :
            answer.append('?')
            flag = False
            break
    if flag:
        answer.append(w)
for a in answer:
    print(a, end='')