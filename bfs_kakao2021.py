def solution(places):
    answer = []

    dir = [[-1, 0], [0, -1], [+1, 0], [0, +1]]
    for place in places:
        flag = False
        
        for x in range(5):
            for y in range(5):
                if place[x][y] == "P":
                    for d in dir:
                        tx, ty = x + d[0], y + d[1]
                        if (tx>=0 and tx<=4 and ty>=0 and ty<=4):
                    
                            if place[tx][ty] == "O":
                                for dd in dir:
                                    ttx, tty = tx + dd[0], ty + dd[1]
                                    if (ttx>=0 and ttx<=4 and tty>=0 and tty<=4):
                            
                                        if place[ttx][tty] == "P":
                                            if (ttx != x or tty != y) :
                                                flag = True
                            elif place[tx][ty] == "P":
                                flag = True
                                break
        
        if flag:
            answer.append(0)
        else:
            answer.append(1)  
    return answer
