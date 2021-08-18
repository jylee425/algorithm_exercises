import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    if K == 0:
        return answer
    
    while len(scoville) > 1:
        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville)
        heapq.heappush(scoville, food1 + food2*2)
        answer += 1

        if scoville[0] >= K:
            return answer
    return -1
