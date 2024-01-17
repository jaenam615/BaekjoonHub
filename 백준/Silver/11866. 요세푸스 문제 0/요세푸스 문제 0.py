import sys
from collections import deque

N, K  = map(int, sys.stdin.readline().split())
people = deque()
counter = 0 
perm = []
for i in range(N):
    people.append(i+1)

while people:
    if counter == K-1:
        perm.append(people.popleft())
        counter = 0
    else:    
        people.append(people.popleft())
        counter +=1

print('<', end="")
print(', '.join(map(str, perm)), end='')
print('>')