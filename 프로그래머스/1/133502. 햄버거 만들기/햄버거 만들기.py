def solution(ingredient):
    answer = 0
    stack = []
    order = [1, 2, 3, 1] 
    
    for ing in ingredient:
        stack.append(ing)  
        
        if stack[-4:] == order:
            answer += 1
            for i in range(4):
                stack.pop()
    
    return answer
