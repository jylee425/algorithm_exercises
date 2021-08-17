def solution(participant, completion):
    dict = {}
    
    target = 0
    for p in participant:
        dict[hash(p)] = p
        target += hash(p)
        
    for c in completion:
        target -= hash(c)
        
    return dict[target]
