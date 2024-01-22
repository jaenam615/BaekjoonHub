import sys

V, E = map(int, sys.stdin.readline().split())

edges = [0] * E

for i in range(E):
    edges[i] = tuple(map(int, sys.stdin.readline().split()))

#가중치 오름차순으로 정렬
edges.sort(key=lambda arr: arr[2])



parent = [i for i in range(V+1)]

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

weight = 0

for a, b, cost in edges:
    # if parent[a] != parent[b]:
    if not same_parent(parent, a,b):
        union_parent(parent, a, b)
        weight += cost

print(weight)
