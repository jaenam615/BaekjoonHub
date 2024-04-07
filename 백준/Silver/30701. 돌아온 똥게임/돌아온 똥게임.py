import heapq
import sys

input = sys.stdin.readline
N, D = map(int, input().rstrip().split())

monster = []
equip = []
for _ in range(N):
    a, b = map(int, input().rstrip().split())
    if a == 1:
        heapq.heappush(monster, b)
    else:
        heapq.heappush(equip, b)
        
counter = 0 




while monster:
    now = heapq.heappop(monster)
    if D > now:
        counter += 1
        D += now       
    elif not equip:
        continue
    else:
        heapq.heappush(monster, now)
        jangbi = heapq.heappop(equip)
        counter += 1
        D *= jangbi

if equip:
    counter += len(equip)
    
print(counter)  
    