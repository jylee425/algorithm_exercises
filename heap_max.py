import heapq

def heappopmax(nums):
    res = []
    for n in nums:
        heapq.heappush(res, -n)
    heapq.heappop(res)

    return [-n for n in res]

def solution(operations):
    answer = []

    for op in operations:
        heapq.heapify(answer)
        ops = op.split(" ")
        if ops[0] == "I":
            heapq.heappush(answer, int(ops[1]))

        elif ops[0] == "D" and len(answer) > 0:
            if ops[1] == "1":
                answer = heappopmax(answer)

            else:
                heapq.heappop(answer)

    if len(answer) == 0:
        return [0,0]
    else:
        return [max(answer), answer[0]]
    return answer
