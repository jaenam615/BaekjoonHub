import sys
input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())
l = []
tree = [0] * 3000000

def make_tree(node, start, end):
    if start == end:
        tree[node] = l[end]
        return tree[node]
    mid = (start + end)//2
    
    tree[node] = make_tree(node*2,start,mid) + make_tree(node*2+1,mid+1,end)
    return tree[node]

def update_tree(node, start, end, newIndex, newValue):
    if start == end:
        tree[node] = newValue
        return
    mid = (start+end)//2
    
    if start <= newIndex and newIndex <= mid:
        update_tree(node*2, start, mid, newIndex, newValue)
    elif mid <= newIndex and newIndex <= end:
        update_tree(node*2+1, mid+1, end, newIndex, newValue)
    
    tree[node] = tree[node*2] + tree[node*2+1]
    return

def get_sum(node, start, end, sumStart, sumEnd):
    if sumEnd < start or sumStart > end:
        return 0
    
    if (sumStart <= start and sumEnd >= end):
        return tree[node]
    mid = (start+end)//2
    return (get_sum(node*2, start, mid, sumStart, sumEnd) + get_sum(node*2+1, mid+1, end, sumStart, sumEnd))

for _ in range(N):
    l.append(int(input().rstrip()))
    
make_tree(1,0,N-1)

for _ in range(M+K):
    a, b, c = map(int, input().rstrip().split()) 
    if a == 1:
        update_tree(1,0,N-1,b-1,c)
    elif a == 2:
        print(get_sum(1,0,N-1,b-1,c-1))
        