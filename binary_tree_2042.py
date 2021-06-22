def build_tree(tree, node, start, end, arr):
    if start == end:
        tree[node] = arr[start]
    else:
        node_left = build_tree(tree, node*2, start, (start+end)//2, arr)
        node_right = build_tree(tree, node*2+1, (start+end)//2+1, end, arr)
        tree[node] = node_left + node_right
    return tree[node]

        
def update_tree(tree, node, start, end, index, val):
    if index < start or index > end:
        return

    tree[node] += val

    flag_leaf = start != end
    if flag_leaf:
        update_tree(tree, node*2, start, (start+end)//2, index, val)
        update_tree(tree, node*2+1, (start+end)//2+1, end, index, val)
    
def sum_subtree(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right :
        return tree[node]
    
    sum_left = sum_subtree(tree, node*2, start, (start+end)//2, left, right) 
    sum_right = sum_subtree(tree, node*2+1, (start+end)//2+1, end, left, right)
    return sum_left + sum_right 

n, m, k = map(int, input().split())

arr = []
for _ in range(n) :
    arr.append(int(input()))

tree = [0] * (1000000 * 3)
build_tree(tree, 1, 0, n-1, arr)

for _ in range(m+k) :
    a, b, c = map(int, input().split())
 
    if a == 1 :
        diff = c - arr[b-1]
        arr[b-1] += diff
        update_tree(tree, 1, 0, n-1, b-1, diff)

    if a == 2 :                
        print(sum_subtree(tree, 1, 0, n-1, b-1, c-1))