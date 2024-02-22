import sys

input = sys.stdin.readline

while True:
    stk = [0]
    status = 1
    sentence = input()
    if sentence.rstrip() == ".":
        break
    
    for i in range(len(sentence)):
        if sentence[i] == "(" or sentence[i] == "[":
            stk.append(sentence[i])
            continue
        elif sentence[i] == ")":
            if stk.pop() == "(":
                continue
            status = 0 
            stk.append("X")
            break
        elif sentence[i] == "]":    
            if stk.pop() == "[":
                continue
            status = 0
            stk.append("X")
            break
    if stk == [0]:
        status = 1
    elif stk:
        status = 0
        
    if status == 1:
        print("yes")
    elif status == 0:
        print("no")
            
                
        
