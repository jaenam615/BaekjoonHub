from collections import deque

def solution(s):
    answer = True
    
    if s[0] == ')' or s[-1] == '(':
        return False
    
    stk = []
    for i in range(len(s)):
        if stk:
            topmost = stk.pop()
            if topmost == "(" and s[i] == ")":
                continue
            else: 
                stk.append(topmost)
        stk.append(s[i])
    
    if stk:
        answer = False
    
    return answer