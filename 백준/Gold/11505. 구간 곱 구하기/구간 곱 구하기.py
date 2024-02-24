import sys
import math
MOD = 1000000007

input = sys.stdin.readline

def make_tree(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    
    mid = (start+end)//2

    tree[node] = (make_tree(node*2, start, mid)*make_tree(node*2+1, mid+1, end)) % 1000000007
    return tree[node]

def update_tree(node, start, end, newIndex, newValue):
    if newIndex < start or newIndex > end:
        return
    if start == end:
        tree[node] = newValue
        return
    mid = (start+end)//2
    
    if start <= newIndex and newIndex<=mid:
        update_tree(node*2, start, mid, newIndex, newValue)
    elif mid <= newIndex and newIndex<=end:
        update_tree(node*2+1, mid+1, end, newIndex, newValue)
        
    tree[node] = (tree[node*2] * tree[node*2+1]) % 1000000007
    return


def get_product(node, start, end, prodStart, prodEnd):
    if prodEnd < start or prodStart > end: #구하려는 구간이 트리의 시작보다 전이거나, 트리의 끝보다 뒤면 넘어가야함
        return 1
    
    if (prodStart<=start) and prodEnd>=end: 
        return tree[node]
    
    mid = (start + end)//2

    return (get_product(node*2, start, mid, prodStart, prodEnd) * get_product(node*2+1, mid+1, end, prodStart, prodEnd)) % 1000000007



N, M, K = map(int, input().rstrip().split())
arr = []

arr = [int(input().rstrip()) for _ in range(N)]

tree = [0] * (1 << (int(math.ceil(math.log2(N))) + 1))

make_tree(1,0,N-1)

for _ in range(M+K):
    a, b, c = map(int, input().rstrip().split())
    if a == 1:
        update_tree(1,0,N-1,b-1,c)
    else:
        print(get_product(1,0,N-1,b-1,c-1))