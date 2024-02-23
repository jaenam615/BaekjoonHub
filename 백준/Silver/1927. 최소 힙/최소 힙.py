import heapq
import sys

N = int(input())

hq = []

for _ in range(N):
    a = int(sys.stdin.readline())
    if a > 0:
        heapq.heappush(hq, a)
    elif a == 0:
        if not hq:
            print(0)
            continue
        print(heapq.heappop(hq))
        
    