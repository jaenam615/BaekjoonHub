N, K = map(int, input().split())

V = []

for i in range(N):
    V.append(int(input()))

V.reverse()
count = 0

for value in V:
    if value > K:
        continue
    else:
        amount = K // value
        count += amount
        K -= amount * value

print(count)