import sys
from math import sqrt

T = int(input())

for _ in range(T):
    
    x1, y1, r1, x2, y2, r2  = map(int, sys.stdin.readline().split())
    
    d = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    diff = abs(r1-r2)
    
    if d == 0 and r1 == r2:
        print(-1)
    elif (r1+r2) == d or diff == d:
        print(1)
    elif diff < d < (r1+r2):
        print(2)
    else:
        print(0)

