class Node:
  def __init__(self, d, p, n):
    self.data = d
    self.prev = p
    self.next = n

n = int(input())
ms = list(map(int, input().split()))

refs = {}
linked_list = {}

head = Node(0, None, id(1))
tail = Node(n+1, id(n), None)
linked_list[id(0)] = head
linked_list[id(n+1)] = tail
for nn in range(n):
    refs[nn+1] = id(nn+1)
    linked_list[id(nn+1)] = Node(nn+1, id(nn), id(nn+2))
#print(refs)

for m in ms:
  res = ""

  m_ = linked_list[refs[m]]
  
  h = linked_list[head.next]
  head.next = m_.next
  if h == m_:
    tail.prev = id(m_.data)
    m_.next = id(tail.data)
    linked_list[head.next].prev = id(head.data)
  else:
    h.prev = id(m_.data)
    m_.next = id(h.data)

  t = linked_list[tail.prev]
  tail.prev = m_.prev
  if t == m_ :
    head.next = id(m_.data)
    m_.prev = id(head.data)
    linked_list[tail.prev].next = id(tail.data)
  else :
    t.next = id(m_.data)
    m_.prev = id(t.data)


  k = linked_list[id(0)]
  for i in range(n):
    k = linked_list[k.next]
    res += f"{k.data} "
  
  print(res)