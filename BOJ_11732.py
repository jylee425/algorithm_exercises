import sys

input = sys.stdin.readline

if __name__ == '__main__':
    M = int(input())

    bit = 0
    for _ in range(M):
        cmd = input().split()

        if cmd[0] == "all":
            bit = (1 << 20) - 1
        elif cmd[0] == "empty":
            bit = 0
        else:
            op = cmd[0]
            num = int(cmd[1]) - 1

            if op == "add":
                bit |= (1 << num)
            elif op == "remove":
                bit &= ~(1 << num)
            elif op == "check":
                if bit & (1 << num) == 0:
                    print(0)
                else:
                    print(1)
            elif op == "toggle":
                bit = bit ^ (1 << num)

