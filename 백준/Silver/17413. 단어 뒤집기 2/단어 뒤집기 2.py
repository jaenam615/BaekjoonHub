import sys

string = sys.stdin.readline().rstrip()

final = []
reverse = 1
stk = []

for i in range(len(string)):
    if string[i] == " ":
        while stk:    
            final.append(stk.pop())
        final.append(" ")
        continue

    if string[i] == "<":
        if stk:
            while stk:
                final.append(stk.pop())
        final.append(string[i])
        reverse = 0
        continue
    elif string[i] == ">":
        final.append(string[i])
        reverse = 1
        continue
    
    if reverse == 1:
        stk.append(string[i])
    else:
        final.append(string[i])


if stk:
    while stk:
        final.append(stk.pop())

print(*final, sep="")
            
        
    
    

