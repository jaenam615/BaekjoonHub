import sys
from collections import deque


N = int(input())
dq = deque(map(int, sys.stdin.readline().split()))
s = [0]

stackfront = 0 
queuefront = 0 
order = 1


while(dq):

    queuefront = dq.popleft()
    stackfront = s.pop()
        
    if queuefront == order:
        s.append(stackfront)
        order += 1

        continue
    elif stackfront == order:
        dq.appendleft(queuefront)
        order += 1

        continue 
    else: 
        s.append(stackfront)
        s.append(queuefront)

while s:
    if s.pop() == order:
        order += 1
    else: 
        break  
    
if order == N+1:
    print("Nice")
else:
    print("Sad")
             