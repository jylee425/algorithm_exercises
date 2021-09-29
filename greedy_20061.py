N = int(input())
green = [ [ 0 for _ in range(4) ] for _ in range(6) ]
blue =  [ [ 0 for _ in range(6) ] for _ in range(4) ]


def move(t, x, y):
    xxx, yyy = 5, 5
    if t == 1:
        # green
        for xx in range(5, -1, -1):
            if ( green[xx][y] == 1 ):
                xxx = xx - 1
        green[xxx][y] = 1

        # blue
        for yy in range(5, -1, -1):
            if ( blue[x][yy] == 1 ):
                yyy = yy - 1
        blue[x][yyy] = 1

    elif t == 2: # (x,y) (x,y+1)
        # green
        for xx in range(5, -1, -1):
            if( green[xx][y] == 1 or green[xx][y+1] == 1 ):
                xxx = xx - 1
        green[xxx][y], green[xxx][y+1] = 1, 1

        # blue
        for yy in range(5, 0, -1):
            if( blue[x][yy] == 1 or blue[x][yy-1] == 1 ):
                yyy = yy - 1
        blue[x][yyy], blue[x][yyy-1] = 1, 1

    elif t == 3:
        # green
        for xx in range(5, 0, -1):
            if( green[xx][y] == 1 or green[xx-1][y] == 1 ):
                xxx = xx - 1
        green[xxx][y], green[xxx-1][y] = 1, 1

        # blue
        for yy in range(5, -1, -1):
            if ( blue[x][yy] == 1 or blue[x+1][yy] == 1 ):
                yyy = yy - 1
        blue[x][yyy], blue[x+1][yyy] = 1, 1

def score():
    # green
    count_green = 0
    for x in range(5, -1, -1):
        flag = True
        for y in range(4):
            flag = flag and green[x][y]
        if flag:
            #print(f"green {count_green}")
            count_green += 1

            for xx in range(x, 0, -1):
                for y in range(4):
                    green[xx][y] = green[xx-1][y]

    # blue
    count_blue = 0
    for y in range(5, -1, -1):
        flag = True
        for x in range(4):
            flag = flag and blue[x][y]
        if flag:
            #print(f"blue {count_blue}")
            count_blue += 1

            for yy in range(y, 0, -1):
                for x in range(4):
                    blue[x][yy] = blue[x][yy-1]

    return count_green + count_blue

def special():
    # green
    special = 0
    for s in range(2):
        flag = False
        for y in range(4):
            flag = flag or green[s][y]
        if flag:
            special += 1
    #print(f"special green {special}")
    for x in range(5, special-1, -1):
        for y in range(4):
            green[x][y] = green[x-special][y]
    for x in range(special-1, -1, -1):
        for y in range(4):
            green[x][y] = 0

    # blue
    special = 0
    for s in range(2):
        flag = False
        for x in range(4):
            flag = flag or blue[x][s]
        if flag:
            special += 1
    #print(f"special blue {special}")
    for y in range(5, special - 1, -1):
        for x in range(4):
            blue[x][y] = blue[x][y-special]
    for y in range(special-1, -1, -1):
        for x in range(4):
            blue[x][y] = 0

answer = 0
for _ in range(N):
    t, x, y = map(int, input().split())
    #print(green, blue)

    move(t, x, y)
    #print(green, blue)

    answer += score()
    #print(green, blue)
    #print(f"answer {answer}")

    special()
    #print(green, blue)
print(answer)

answer = 0
for x in range(len(green)):
    answer += sum(green[x])
for x in range(len(blue)):
    answer += sum(blue[x])
print(answer)
