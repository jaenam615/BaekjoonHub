import sys
import random

dwarves=[]
portion = []

for i in range(9):
    height = int(sys.stdin.readline())
    dwarves.append(height)

while True: 
    if sum(portion) != 100:
        random.shuffle(dwarves)
        portion = dwarves[0:7]
    else:
        break

portion.sort()
for i in portion:
    print(i)

