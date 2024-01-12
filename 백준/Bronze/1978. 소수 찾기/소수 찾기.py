import sys
N = int(input())
i = 0 
counter = 0
a = list(map(int, sys.stdin.readline().split()))

while i < N:
    x = 2
    if a[i] == 1:
        counter += 1
        i += 1 
    while x < a[i]:
        if a[i]%x == 0:
            counter += 1
            break
        x += 1
    i += 1
print(N - counter)