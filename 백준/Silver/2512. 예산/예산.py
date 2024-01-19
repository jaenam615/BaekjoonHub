import sys

N = int(input())
area = list(map(int, sys.stdin.readline().split())) 
M = int(input())

low = 0
high = max(area)
mid = (low + high)//2

ans = 0 

def is_possible(mid):
    return sum(min(a, mid) for a in area) <= M

while low <= high:
    if is_possible(mid):
        low = mid + 1
        ans = mid
    else:
        high = mid - 1

    mid = (low + high)//2


print(ans)