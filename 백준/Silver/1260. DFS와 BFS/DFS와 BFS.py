import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

adj = [[0] * N for _ in range(N)]
edges = []
for i in range(M):
    A,B = map(int, sys.stdin.readline().split())
    edges.append((A,B))


for edge in edges:
    adj[edge[0]-1][edge[1]-1] = 1
    adj[edge[1]-1][edge[0]-1] = 1

dfs_chk = [False] * (N+1)
bfs_chk = [False] * (N+1)
dfs_chk[0] = True
bfs_chk[0] = True

def dfs(now, arr):
    for nxt in range(len(arr)):
        if arr[now-1][nxt] and not (dfs_chk[nxt+1]):
            dfs_chk[nxt+1] = 1
            print(nxt+1, end=" ")
            dfs(nxt+1, arr)

def bfs(now, arr):
    dq = deque()
    dq.append(now-1)
    bfs_chk[now] = True
    print(now, end=" ")
    while dq:
        now = dq.popleft()
        for nxt in range(len(arr)):
            if arr[now][nxt] and not (bfs_chk[nxt+1]):           
                bfs_chk[nxt+1] = True
                print(nxt+1,end=" ")     
                dq.append(nxt)
        
dfs_chk[V] = True
print(V, end=" ")
dfs(V,adj)
print()
bfs(V, adj)