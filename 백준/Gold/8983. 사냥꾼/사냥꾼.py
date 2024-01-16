import sys

M, N, L = map(int, sys.stdin.readline().split( ))

sadaes = list(map(int, sys.stdin.readline().split( )))
sadaes.sort()

def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right: 
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target: 
            left = mid+1
        else:
            right = mid-1
    return right 

count = 0 
for _ in range (N):
    x, y = map(int, sys.stdin.readline().split())

    idx = binary_search(sadaes, x)

    dist = abs(x - sadaes[idx]) + y
    dist_right = abs(x - sadaes[idx+1]) + y if idx < M - 1 else float('inf')

    dist = min(dist, dist_right)

    if dist <= L:
            count += 1

print(count)