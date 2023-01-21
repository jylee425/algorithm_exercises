import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())

    queue = []
    for i in range(N):
        cmd = input().split()

        if cmd[0] == 'push':
            queue.insert(0, cmd[1])

        elif cmd[0] == 'pop':
            if len(queue) != 0: print(queue.pop())
            else: print(-1)

        elif cmd[0] == 'size':
            print(len(queue))

        elif cmd[0] == 'empty':
            if len(queue) == 0: print(1)
            else : print(0)

        elif cmd[0] == 'front':
            if len(queue) == 0: print(-1)
            else: print(queue[len(queue) -1])

        elif cmd[0] == 'back':
            if len(queue) == 0: print(-1)
            else: print(queue[0])
