import sys
from itertools import combinations

heights = [int(sys.stdin.readline()) for _ in range(9)]

for combination in combinations(heights, 7):
    if sum(combination) == 100:
        for height in sorted(combination):
            print(height)
        break