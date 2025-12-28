def solution(n, computers):
    visited = [0 for _ in range(n)]
    
    def dfs(i):
        visited[i] = True
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                dfs(j)

    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1

    return count