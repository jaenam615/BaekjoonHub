def prune(states):
    best = {}
    for a, b in states:
        if b not in best or a < best[b]:
            best[b] = a
    return [(a, b) for b, a in best.items()]

def solution(info, n, m):
    trace = [[] for _ in range(len(info)+1)]
    trace[0].append((0,0))
    for idx, val in enumerate(info):
        for prev in trace[idx]:
            if prev[1] + val[1] < m:
                trace[idx+1].append((prev[0], prev[1]+val[1]))
            
            if prev[0] + val[0] < n:
                trace[idx+1].append((prev[0]+val[0], prev[1]))
    
        trace[idx+1] = prune(trace[idx+1])        
        
    if len(trace[-1]) == 0:
        return -1
    
    trace[-1].sort()
    answer = trace[-1][0][0]
    return answer