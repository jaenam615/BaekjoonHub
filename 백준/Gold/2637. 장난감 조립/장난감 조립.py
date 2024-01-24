import sys
from collections import deque

N = int(input())
M = int(input())

adj = [[] for _ in range(N + 1)]
seolmyungseo = [[0] * (N + 1) for _ in range(N + 1)]
dq = deque()
degree = [0 for _ in range(N + 1)]

for i in range(M):
    made, part, amount = map(int, sys.stdin.readline().split())
    adj[part].append((made, amount))
    degree[made] += 1

for i in range(1, N + 1):
    if not degree[i]:
        dq.append(i)

def bfs():
    while dq:
        now = dq.popleft()
        for nxt, nxt_need in adj[now]:
            if seolmyungseo[now].count(0) == N + 1:
                seolmyungseo[nxt][now] += nxt_need
            else:
                for i in range(1, N + 1):
                    seolmyungseo[nxt][i] += seolmyungseo[now][i] * nxt_need
            degree[nxt] -= 1
            if degree[nxt] == 0:
                dq.append(nxt)


bfs()
for x in enumerate(seolmyungseo[N]):
    if x[1] > 0:
        print(*x)
