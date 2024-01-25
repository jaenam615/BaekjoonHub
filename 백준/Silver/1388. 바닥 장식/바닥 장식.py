import sys

N, M = map(int, sys.stdin.readline().split())

adj = [0 for _ in range(N)]

for i in range(N):
    a = input()
    adj[i] = str(a)

dy = (1, -1)
dx = (1, -1)


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M


chk = [[False] * M for _ in range(N)]
counter = 0


def dfs(y, x):
    if adj[y][x] == "|":
        chk[y][x] = True
        for i in range(2):
            ny = y + dy[i]
            if is_valid_coord(ny, x) and not chk[ny][x]:
                if adj[ny][x] == "|":
                    dfs(ny, x)
                    return
                else:
                    return

    if adj[y][x] == "-":
        chk[y][x] = True
        for i in range(2):
            nx = x + dx[i]
            if is_valid_coord(y, nx) and not chk[y][nx]:
                if adj[y][nx] == "-":
                    dfs(y, nx)
                    return
                else:
                    return


for i in range(N):
    for j in range(M):
        if chk[i][j] == False:
            dfs(i, j)
            counter += 1

print(counter)
