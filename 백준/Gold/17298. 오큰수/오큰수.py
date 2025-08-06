import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
answer = [-1] * N
stack = []

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        index = stack.pop()
        answer[index] = A[i]
    stack.append(i)

print(*answer)