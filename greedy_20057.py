N = int(input())
matrix = []

total = 0
for _ in range(N):
    row = list(map(int, input().split()))
    total += sum(row)
    matrix.append(row)

# direction
dir_lst = [0, 1, 2, 3] # left, down, right, up
dir_idx = -1

s_target = 0
m_target, m_flag = 0, True
def get_dir(step):
    global s_target, m_target, m_flag, dir_lst, dir_idx 

    if step >= s_target:
        if m_flag:
            m_target += 1
        m_flag = not m_flag
        s_target += m_target

        dir_idx += 1
        dir_idx %= 4

    return dir_lst[dir_idx]

# step
dir_alpha = [[[-2, 0, 2], [-1, -1, 10], [-1, 0, 7], [-1, +1, 1], [0, -2, 5], [1, -1, 10], [+1, 0, +7], [1, +1, 1], [2, 0, 2]],
            [[-1, -1, 1], [-1, +1, 1], [0, -2, 2], [+0, -1, 7], [0, +1, 7], [0, +2, +2], [1, -1, 10], [1, +1, 10], [2, 0, 5]],
            [[-2, 0, 2], [-1, -1, 1], [-1, 0, 7], [-1, 1, 10], [0, 2, 5], [1, -1, 1] ,[1, 0, 7], [1, 1, 10], [+2, 0, 2]],
            [[-2, 0, 5], [-1, -1, 10], [-1, +1, 10], [0, -2, 2], [0, -1, 7], [0, +1, 7], [0, 2, 2], [+1, -1, 1], [+1, +1, 1]]]
pos_alpha = [[0, -1], [1, 0], [0,1], [-1, 0]]
def step_ahead(dir, x, y):
    global matrix, dir_alpha, pos_alpha
    res = 0
    
    blown_total = 0
    if dir == 0:
        tx, ty = x, y-1
    if dir == 1:
        tx, ty = x+1, y
    if dir == 2 :
        tx, ty = x, y+1
    if dir == 3 :
        tx, ty = x-1, y

    sand = matrix[tx][ty]
    matrix[tx][ty] = 0

    blown_total = 0
    for i in range(len(dir_alpha[dir])):
        ttx, tty, alpha = tx + dir_alpha[dir][i][0], ty + dir_alpha[dir][i][1], dir_alpha[dir][i][2]
        blown_tmp = int( alpha * sand / 100 )
        if ttx >=0 and ttx < N and tty >= 0 and tty < N:
            matrix[ttx][tty] += blown_tmp
        else:
            res += blown_tmp
        blown_total += blown_tmp
    ttx, tty = tx + pos_alpha[dir][0], ty + pos_alpha[dir][1]
    if ttx >= 0 and ttx < N and tty >= 0 and tty < N:
        matrix[ttx][tty] += sand - blown_total
    else:
        res += sand - blown_total

    return res, tx, ty


step, answer = 0, 0
x, y = N//2, N//2
while True:
    dir = get_dir(step)
    
    tmp, x, y = step_ahead(dir, x, y)

    step += 1
    answer += tmp

    if step >= N*N: break
print(answer)
