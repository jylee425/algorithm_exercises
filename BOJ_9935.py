import sys

input = sys.stdin.readline

if __name__ == "__main__":
    arr = input().rstrip()
    bomb = input().rstrip()

    # use stack
    stack = []
    for s in arr:
        stack.append(s)
        if len(stack) >= len(bomb):
            if "".join(stack[-len(bomb) :]) == bomb:
                del stack[-len(bomb) :]

    if stack:
        print("".join(stack))
    else:
        print("FRULA")
