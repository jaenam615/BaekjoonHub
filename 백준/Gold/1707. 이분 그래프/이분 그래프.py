import sys

sys.setrecursionlimit(10**6)


def bitgraph():
    V, E = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(V + 1)]
    chk = [0] * (V + 1)
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)

    for i in range(1, V + 1):
        if chk[i] == 0:
            result = dfs(adj, chk, i, 1)
            if not result:
                break
    if result:
        print("YES")
    else:
        print("NO")


def dfs(arr, visit, now, bit):
    visit[now] = bit
    
    for nxt in arr[now]:
        if visit[nxt] == 0:
            result = dfs(arr, visit, nxt, -bit)
            if not result:
                return False
        else:
            if visit[nxt] == bit:
                return False
    return True


N = int(input())

for _ in range(N):
    bitgraph()
