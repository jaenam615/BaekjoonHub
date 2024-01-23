# 시간초과

import sys

sys.setrecursionlimit(10**6)

N = int(input())

adj_list = [[] for _ in range(N + 1)]

for i in range(N - 1):
    A, B = map(int, sys.stdin.readline().split())
    adj_list[A].append(B)
    adj_list[B].append(A)

chk = [0] * (N+1)


def dfs(now):
    for i in adj_list[now]:
        if not chk[i]:
            chk[i] = now
            dfs(i)


chk[1] = 1
dfs(1)
for i in range(2, N + 1):
    print(chk[i])
