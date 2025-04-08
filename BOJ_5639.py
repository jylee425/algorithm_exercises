import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def convert(preorder, postorder, start, end):
    if start > end:
        return

    root = preorder[start]
    mid = end + 1

    # Find the first element greater than root
    for i in range(start + 1, end + 1):
        if preorder[i] > root:
            mid = i
            break

    # Recursively convert left and right subtrees
    convert(preorder, postorder, start + 1, mid - 1)
    convert(preorder, postorder, mid, end)

    # Append the root to the postorder list
    postorder.append(root)

    return postorder


if __name__ == "__main__":
    preorder = []
    while True:
        try:
            preorder.append(int(input()))
        except:
            break

    postorder = []
    convert(preorder, postorder, 0, len(preorder) - 1)
    print("\n".join(map(str, postorder)))
