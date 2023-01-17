
def vowel(c):
    return c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' 

def check(res):
    v, c = 0, 0
    for r in res:
        if vowel(r): v += 1
        else: c += 1

    return v >= 1 and c >= 2


def dfs(L, letters, cnt, now, res):
    if cnt >= L:
        if check(res):
            print(''.join(map(str, res)))
        return

    for i, c in enumerate(letters):
        if i <= now:
            continue
        
        res.append(c)
        dfs(L, letters, cnt+1, i, res)
        res.pop()

    return

def main(L, letters):
    cnt = 0
    now = -1
    res = []

    dfs(L, letters, cnt, now, res)

if __name__ == '__main__':
    L, C = map(int, input().split())
    letters = sorted(list(input().split(' ')))
    # print(letters)

    main(L, letters)
    
