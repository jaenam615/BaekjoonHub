import sys

V = int(input())
E = int(input())


edges = [[0,0] for _ in range (E+1)]

for i in range(E):
    A, B = map(int, sys.stdin.readline().split())
    edges[i+1] = [A,B]

virus = [i for i in range(V+1)]


def find_parent(arr, x):
    if arr[x] == x:
        return x 
    arr[x] = find_parent(arr, arr[x])
    return arr[x]

def union_parent(arr, a, b): 
    a = find_parent(arr, a)
    b = find_parent(arr, b)    
    if a < b:
        arr[b] = a
    else:
        arr[a] = b 


# for a, b in edges:
#     union_parent(virus, a, b)
i = 0
while i <2:
    for a,b in edges:
        union_parent(virus,a,b)
    i += 1

print(virus.count(1)-1)
