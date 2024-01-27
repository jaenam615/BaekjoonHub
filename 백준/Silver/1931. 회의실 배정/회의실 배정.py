N = int(input())

conf = []

for i in range(N):
    a, b = map(int, input().split())
    conf.append((b, a))

conf.sort()

happen = []

happen.append(conf[0])

for i in range(1, len(conf)):
    if conf[i][1] >= happen[-1][0]:
        happen.append(conf[i])

print(len(happen))
