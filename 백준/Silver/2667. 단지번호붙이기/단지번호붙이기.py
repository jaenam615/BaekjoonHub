import sys

sys.setrecursionlimit(10**6)

N = int(input())

adj = [0 for _ in range(N)]

for i in range(N):
    adj[i] = str(input())

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N


chk = [[False] * N for _ in range(N)]


danji_counter = 0
house_per_danji = []


def dfs(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if is_valid_coord(ny, nx) and adj[ny][nx] == "1" and not chk[ny][nx]:
            chk[ny][nx] = True
            how_many[ny][nx] = True
            dfs(ny, nx)


count = 0
for i in range(N):
    for j in range(N):
        if adj[i][j] == "1" and not chk[i][j]:
            how_many = [[False] * N for _ in range(N)]
            count = 0
            chk[i][j] = True
            how_many[i][j] = True
            dfs(i, j)
            for k in range(N):
                count += how_many[k].count(True)
            danji_counter += 1
            house_per_danji.append(count)


print(danji_counter)
house_per_danji.sort()
for danji in house_per_danji:
    print(danji)
