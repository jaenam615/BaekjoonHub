import sys
from collections import deque

# N = Cities(vertex)
# M = Roads(edges)
# X = start city
# K = Minimum to certain city

N, M, K, X = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)

distance = [0 for _ in range(N + 1)]
chk = [False for _ in range(N + 1)]


def bfs(start):
    answers = []
    dq = deque()
    dq.append(start)
    chk[start] = True
    distance[start] = 0
    while dq:
        now = dq.popleft()
        for nxt in adj[now]:
            if not chk[nxt]:
                chk[nxt] = True
                dq.append(nxt)
                distance[nxt] = distance[now] + 1
                if distance[nxt] == K:
                    answers.append(nxt)

    if len(answers) == 0:
        print(-1)
    else:
        answers.sort()
        for answer in answers:
            print(answer)


bfs(X)
