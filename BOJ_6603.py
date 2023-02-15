
def dfs(N, arr, now, selected):
    if len(selected) == 6:
        print(*selected)
        return 

    for i, e in enumerate(arr):
        if i < now: continue
        if e in selected: continue

        selected.append(e)
        dfs(N, arr, i, selected)
        selected.pop()

    return

def main(N, arr):
    now = 0
    selected = []

    dfs(N, arr, now, selected)
    print()
    return

if __name__ == '__main__':
    while(True):
        cmd = input()
        if cmd == '0': break

        cmd = list(map(int, cmd.split()))
        N, arr = cmd[0], cmd[1:]
        main(N, arr)

    exit(0)
