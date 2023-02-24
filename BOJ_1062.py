ans = 0

def check(words, learn):
    res = 0
    for word in words:
        if (learn & word) == word:
            res += 1
    return res

def dfs(N, K, words, must, idx, learn):
    global ans
    if idx > 26: return

    if bin(learn).count('1') == K:
        ans = max(ans, check(words, learn))
        return

    # print(bin(must), bin(1 << idx))
    if must & (1 << idx):
        dfs(N, K, words, must, idx+1, learn | (1 << idx))
    else:
        dfs(N, K, words, must, idx+1, learn)
        dfs(N, K, words, must, idx+1, learn | (1 << idx))

    return


def main(N, K, vocabs):
    if K < 5:
        print(0)
        return

    global ans

    must = 0
    for alpha in 'acint':
        order = ord(alpha) - ord('a')
        must |= 1 << order

    words = []
    for vocab in vocabs:
        b = 0
        for alpha in vocab:
            order = ord(alpha) - ord('a')
            b |= 1 << order
        words.append(b)

    idx, learn = 0, 0
    dfs(N, K, words, must, idx, learn)
    print(ans)
    return

if __name__ == '__main__':
    N, K = map(int, input().split())
    vocabs = [input() for _ in range(N)]

    main(N, K, vocabs)
