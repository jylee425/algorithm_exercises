import heapq

def solution(n, start, end, roads, traps):
    answer = 0
    
    # graph init
    graph =[[] for _ in range(n+1)]
    for (h, t, c) in roads:
        graph[h].append([t, c, 0]) # normal
        graph[t].append([h, c, 1]) # reverse

    # trap_idx for state computation
    trap_idx = {}
    for idx, trap in enumerate(traps):
        trap_idx[trap] = idx
    
    # dijkstra algorithm
    dist = [[float('inf') for _ in range(n+1)] for _ in range(1<<len(traps))]
    queue = []
    
    state = 0
    dist[state][start] = 0
    heapq.heappush(queue, (start, dist[state][start], state))
    while (queue):
        cur_node, cur_dist, cur_state = heapq.heappop(queue)
        
        if end == cur_node:
            answer = cur_dist
            break
            
        if dist[cur_state][cur_node] < cur_dist:
            continue
            
        for nxt_node, nxt_dist, nxt_state in graph[cur_node]:
            
            # state computation with bit-masking
            if cur_node in traps:
                if nxt_node in traps:
                    cmp_state = ((1&(cur_state>>trap_idx[cur_node])) + (1&(cur_state>>trap_idx[nxt_node])))%2
                    state = cur_state^(1<<trap_idx[nxt_node])
                else:
                    cmp_state = (1&(cur_state>>trap_idx[cur_node]))
                    state = cur_state
            else:
                if nxt_node in traps:
                    cmp_state =  (1&(cur_state>>trap_idx[nxt_node]))
                    state = cur_state^(1<<trap_idx[nxt_node])
                else:
                    cmp_state = 0
                    state = cur_state
            
            if cmp_state == nxt_state:
                if dist[state][nxt_node] > cur_dist + nxt_dist:
                    dist[state][nxt_node] = cur_dist + nxt_dist
                    heapq.heappush(queue, (nxt_node, dist[state][nxt_node], state))

    return answer
