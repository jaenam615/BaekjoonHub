N, M = map(int, input().split())

items = []
items.append((0, 0))

for i in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

items.sort()

cache = [[0] * (M + 1) for _ in range(N + 1)]


for i in range(1, N + 1):
    for j in range(1, M + 1):
        if items[i][0] > j:
            cache[i][j] = cache[i - 1][j]
        else:
            cache[i][j] = max(
                (cache[i - 1][j]), (cache[i - 1][j - items[i][0]] + items[i][1])
            )

print(max(max(cache)))
