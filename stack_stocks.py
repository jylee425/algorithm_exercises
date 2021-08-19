def solution(prices):
    answer = [-1 for _ in range(len(prices))]
    stack = []

    stack.append((0, prices[0]))
    for time in range(1, len(prices)):
        while stack and stack[-1][1] > prices[time]:
            (prev, value) = stack.pop()
            answer[prev] = (time - prev)
        stack.append((time, prices[time]))

    for time, price in enumerate(answer):
        if price == -1: 
            answer[time] += len(prices) - time
    return answer
