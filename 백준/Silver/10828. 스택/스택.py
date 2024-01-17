import sys

N = int(sys.stdin.readline())

stk = []

for i in range(N):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        stk.append(int(command[1]))
    elif command[0] == "pop":
        print(stk.pop() if stk else -1)
    elif command[0] == "size":
        print(len(stk))
    elif command[0] == "empty":
        print(0 if stk else 1)
    else: 
        print(stk[-1] if stk else -1)