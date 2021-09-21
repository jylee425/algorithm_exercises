N = int(input())
board = [0 for i in range(16)]

result = 0
def possible(x):
    for i in range(1, x):
        if board[x] == board[i] or abs(board[x] - board[i]) == x - i:
            return False
    return True

def simulate(cnt):
    global result
    if cnt > N:
        result += 1
        return
    for i in range(1, N + 1):
        board[cnt] = i
        if possible(cnt): simulate(cnt + 1)

simulate(1)
print(result)
