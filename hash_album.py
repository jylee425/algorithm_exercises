def solution(genres, plays):
    total = {}
    map = {}

    for i, g in enumerate(genres):
        if g in map: 
            map[g].append((i, plays[i]))
            total[g] += plays[i]
        else:
            map[g] = [(i, plays[i])] 
            total[g] = plays[i]

    answer = []
    order = sorted(total.items(), key=lambda item: item[1], reverse=True)
    for o in order:
        musics = sorted(map[o[0]], key=lambda item: item[1], reverse=True)
        album = [ m[0] for m in musics[:2] ]
        answer += album
    return answer
