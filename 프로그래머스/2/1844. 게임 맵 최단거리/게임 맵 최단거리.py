from collections import deque

def solution(maps):    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    
    dq = deque([(0,0,1)])
    
    m = len(maps)
    n = len(maps[-1])

    visited = [[False] * n for _ in range(m)]
    visited[0][0] = True
    
    while dq:
        y, x, count = dq.popleft()
        
        if y == m-1 and x == n-1:
            return count
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
        
            if (ny < 0 or ny >= m) or (nx < 0 or nx >= n) or (visited[ny][nx] == True):
                continue
        
            if (maps[ny][nx] == 0):
                continue
        
            visited[ny][nx] = True
            dq.append((ny, nx, count+1))
    
    return -1