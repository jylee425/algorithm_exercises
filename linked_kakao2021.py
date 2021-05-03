class Node:
  def __init__(self, d, p, n):
    self.data = d
    self.prev = p
    self.next = n

n = int(input())
ms = list(map(int, input().split()))

refs = {} # value -> address
linked_list = {} # address -> Node (value)

# build linked list
head = Node(0, None, id(1))
tail = Node(n+1, id(n), None)
linked_list[id(0)] = head
linked_list[id(n+1)] = tail
for nn in range(n):
    refs[nn+1] = id(nn+1)
    linked_list[id(nn+1)] = Node(nn+1, id(nn), id(nn+2))

for m in ms:
  res = ""

  m_ = linked_list[refs[m]]
  n_ = linked_list[m_.prev]
  o_ = linked_list[m_.next]
  head_ = linked_list[head.next]
  tail_ = linked_list[tail.prev]
  
  # swapping right and left with linked list
  if n_ == head:
    m_.next = id(tail.data)
    tail.prev = id(m_.data)
  else:
    m_.next = id(head_.data)
    head_.prev = id(m_.data)

    tail.prev = id(n_.data)
    n_.next = id(tail.data)

  if o_ == tail :
    m_.prev = id(head.data)
    head.next = id(m_.data)
  else :
    m_.prev = id(tail_.data)
    tail_.next = id(m_.data)
    
    head.next = id(o_.data)
    o_.prev = id(head.data)

  k = linked_list[id(0)]
  for i in range(n):
    k = linked_list[k.next]
    print(k.data)
    res += f"{k.data} "
  
  print(res)