class Node:
  def __init__(self, h, t):
    self.head = h
    self.tail = t

n, k = map(int, input().split(' '))
c = k-1

seq = []
for i in range(n):
    seq.append(Node((i-1) % n, (i+1) % n))

res = "<"
left = n
for nn in range(n):
    res += f"{c+1}"
    if (nn != n-1):
        res += ", "

    seq[seq[c].head].tail = seq[c].tail
    seq[seq[c].tail].head = seq[c].head

    for kk in range(k):
        c = seq[c].tail
res += ">"
print(res)