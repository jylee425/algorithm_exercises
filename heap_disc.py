import heapq

def solution(jobs):
    answer = 0
    n = len(jobs)

    now = 0
    while len(jobs) > 0:
        heapq.heapify(jobs)
        (init, take) = heapq.heappop(jobs)

        answer += take
        now = init + take
        for idx, (init, take) in enumerate(jobs):
            if init < now: 
                jobs[idx] = [now, take]
                answer += now - init
    return answer // n
