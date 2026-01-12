def solution(tickets):
    tickets.sort()
    used = [False] * len(tickets)
    answer = ["ICN"]
    
    def dfs(curr, depth):
        if depth == len(tickets):
            return True
        
        for i in range(len(tickets)):
            if not used[i] and tickets[i][0] == curr:
                used[i] = True
                answer.append(tickets[i][1])
                
                if dfs(tickets[i][1], depth + 1):
                    return True
                
                # backtrack
                used[i] = False
                answer.pop()
        
        return False
    
    dfs("ICN", 0)
    return answer
