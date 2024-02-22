import sys 

input = sys.stdin.readline

def apply(n, stack):
    if n[0] == '1':
        stack.append(n[1])
        return -2
    elif n[0] == '2':
        if stack:
            return(stack.pop())
        else: 
            return -1
    elif n[0] == '3':
        return len(stack)
    elif n[0] == '4':
        if stack:
            return 0
        else:
            return 1
    else:
        if not stack:
            return -1
        this = stack.pop()
        stack.append(this)
        return this
        

N = int(input())
stk = []
for _ in range(N):
    val = 0
    cmd = input().split()
    ans = apply(cmd, stk)
    if ans != -2:
        print(ans)