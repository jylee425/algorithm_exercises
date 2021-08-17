def solution(clothes):
    map = {}
    for c in clothes:
        if c[1] in map.keys():
            map[c[1]] += 1
        else:
            map[c[1]] = 1

    answer = 1
    for value in map.values():
        answer *= (value+1)
    return (answer - 1)
