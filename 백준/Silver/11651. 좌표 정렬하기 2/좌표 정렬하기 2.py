import heapq
N = int(input())

coordinates = []

for _ in range(N):
    x, y = map(int, input().split())
    heapq.heappush(coordinates,(y,x))
    
# coordinates.sort(key=lambda x: x[1])

for i in range(len(coordinates)):
    y, x = heapq.heappop(coordinates)
    print(x, y)