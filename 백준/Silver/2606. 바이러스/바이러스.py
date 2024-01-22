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

def same_parent(arr, a, b):
    return find_parent(arr, a) == find_parent(arr, b)

# for edge in edges:
#     for a, b in edge:
#         if not same_parent(virus, a, b):
#             union_parent(virus, a, b)

for i in range(2):
    for a,b in edges:
        union_parent(virus,a,b)


print(virus.count(1)-1)
