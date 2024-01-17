import sys
from collections import deque

T = int(sys.stdin.readline())
cards = deque()

for i in range(1,T+1):
    cards.append(i)

while len(cards) > 0:
    if len(cards) == 1:
        print(cards.popleft())
        break
    cards.popleft()
    if len(cards) > 1:
        cards.append(cards.popleft())