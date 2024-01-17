import sys
from collections import deque

N = int(sys.stdin.readline())

q = deque()

for i in range(N):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        q.append(int(command[1]))
    elif command[0] == "pop":
        print(q.popleft() if q else -1)
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        print(0 if q else 1)
    elif command[0] == "front":
        print(q[0] if q else -1)
    else: 
        print(q[-1] if q else -1)