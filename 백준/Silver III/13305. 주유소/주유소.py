import sys

N = int(input())

# dist = [0,]
# buffer = list(map(int, sys.stdin.readline().split()))
# for i in range(len(buffer)):
#     dist.append(buffer[i])


dist = list(map(int, sys.stdin.readline().split()))
dist.append(0)
price = list(map(int, sys.stdin.readline().split()))
cost = 0
start = 0
least = price[0]

for i in range(1, len(price)):
    if least == min(price):
        cost = cost + least*sum(dist[start:])
        break
    
    if price[i] <= least:
        cost = cost + least*sum(dist[start:i])
        start = i
        least = price[i]



print(cost)