import sys
import heapq
pq = []

N = int(sys.stdin.readline())
val = 0
for _ in range(N):
    x = int(sys.stdin.readline()) 
    if x< 0:
        heapq.heappush(pq, (abs(x), -1))        
    elif x>0:
        heapq.heappush(pq, (x, 1))
    else:
        if any(pq) :
            val = heapq.heappop(pq)
            print(val[0]*val[1]) 
        else:
            print(0)