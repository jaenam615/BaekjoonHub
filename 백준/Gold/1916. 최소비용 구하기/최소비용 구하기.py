import sys
import heapq

N = int(input())
M = int(input())

# 인접 리스트로 변경
adj = [[] for _ in range(N + 1)]

for i in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    adj[start].append((end, cost))

S, E = map(int, input().split())

INF = float('inf')
distance = [INF] * (N + 1)

def dijkstra():
    pq = [(0, S)]  # 우선순위 큐를 이용하여 최소 거리를 먼저 선택
    distance[S] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for nxt, nxt_cost in adj[now]:
            new_cost = dist + nxt_cost
            if new_cost < distance[nxt]:
                distance[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))

dijkstra()
print(distance[E])
