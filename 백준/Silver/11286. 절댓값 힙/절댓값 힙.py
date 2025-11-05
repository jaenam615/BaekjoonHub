import heapq
import sys

N = int(sys.stdin.readline())

hq = []

for _ in range(N):
    val = int(sys.stdin.readline())
    if val != 0:
        heapq.heappush(hq, (abs(val), val))
    else:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
