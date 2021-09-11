class node:
    def __init__(self, prev=0, next=-1):
        self.prev = prev
        self.next = next

def solution(n, k, cmds):
    answer = []
    
    history = []
    linked_list = []
    for i in range(n):
        prev = (i-1)%n
        next = (i+1)%n
        linked_list.append(node(prev, next))
        answer.append('O')
    
    last = n-1
    selected = k
    for cmd in cmds:
        if cmd[0] == "U":
            x = int(cmd[2:])
            for _ in range(x):
                selected = linked_list[selected].prev
                
        elif cmd[0] == "D":
            x = int(cmd[2:])
            for _ in range(x):
                selected = linked_list[selected].next
                
        elif cmd[0] == "C":
            answer[selected] = 'X'
            linked_list[ linked_list[selected].prev ].next = linked_list[selected].next 
            linked_list[ linked_list[selected].next ].prev = linked_list[selected].prev 
            history.append(selected)
            
            if selected == last :
                selected = linked_list[selected].prev 
                last -= 1
            else:
                selected = linked_list[selected].next
                
        elif cmd[0] == "Z":
            target = history.pop()
            answer[target] = 'O'
            linked_list[ linked_list[target].prev ].next = target
            linked_list[ linked_list[target].next ].prev = target 
            
            if target == last+1:
                last += 1
    result = ''.join(c for c in answer)
    return result
