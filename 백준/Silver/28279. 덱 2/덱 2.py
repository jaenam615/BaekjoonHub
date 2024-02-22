import sys
from collections import deque

input = sys.stdin.readline

def apply(n, queue):
    if n[0] == '1':
        queue.appendleft(n[1])
        return -2
    elif n[0] == '2':
        queue.append(n[1])
        return -2
    elif n[0] == '3':
        if queue:
            return(queue.popleft())
        else: 
            return -1
    elif n[0] == '4':
        if queue:
            return(queue.pop())
        else: 
            return -1
    elif n[0] == '5':
        return len(queue)
    elif n[0] == '6':
        if queue:
            return 0
        else:
            return 1
    elif n[0] == '7':
        if queue:
            a = queue.popleft()
            queue.appendleft(a)
            return a
        else:
            return -1
    else:
        if not queue:
            return -1
        this = queue.pop()
        queue.append(this)
        return this
        

N = int(input())
dq = deque()
for _ in range(N):
    val = 0
    cmd = input().split()
    ans = apply(cmd, dq)
    if ans != -2:
        print(ans)