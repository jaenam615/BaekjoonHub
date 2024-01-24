import sys
import heapq
from collections import deque

N, M = map(int, sys.stdin.readline().split())

q = deque()

# 인접 리스트
adj = [[] for _ in range(N + 1)]
# going_in = [[] for _ in range(N + 1)]

# 진입차수
amount = [0 for _ in range(N + 1)]
amount[0] = 999
# 방문확인

# 방문여부 확인

chk = [0 for _ in range(N + 1)]

# 위상정렬된 순서
ans = []

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[b].append(a)
    amount[a] += 1
    # going_in[a].append(b)

# for i in range(N):
#     amount[i + 1] = len(going_in[i])

for i in range(1, N + 1):
    if amount[i] == 0:
        q.append(i)


def bfs():
    while q:
        now = q.popleft()
        ans.append(now)
        for nxt in adj[now]:
            if amount[nxt] != 0:
                amount[nxt] -= 1
                if amount[nxt] == 0:
                    q.append(nxt)


bfs()
ans.reverse()
print(*ans)


# for i in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     b
