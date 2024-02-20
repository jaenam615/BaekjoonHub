import sys
from math import ceil
N, M = map(int, sys.stdin.readline().split())

minsix = 1000
minone = 1000 
val = 0 
for _ in range(M):
    six, one = map(int, sys.stdin.readline().split())
    if minsix >= six:
        minsix = six
    if minone >= one:
        minone = one

variety = []

if minsix*(N/6) < minone*N:
    variety.append(minsix*((N//6)+1))
if minsix/6 <= minone:
    val += minsix*(N//6)
    val += minone*(N - 6*(N//6)) 
    variety.append(val)
variety.append(minone*N)        

print(min(variety))