import sys

N = int(sys.stdin.readline())
towers= []

towers = list(map(int, sys.stdin.readline().split( )))
ans = [0] * N
stk = []

for i in range(N):
    while stk:
        if towers[stk[-1][0]] < towers[i]:
            stk.pop()
        else:
            ans[i] = stk [-1][0] + 1
            break
    stk.append((i, towers[i])) ##처음에 0, towers[0]을 삽입 

print(*ans)