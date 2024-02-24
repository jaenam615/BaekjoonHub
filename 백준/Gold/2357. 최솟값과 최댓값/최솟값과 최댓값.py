import sys
import math
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

def make_tree(node, start, end):
    if start == end:
        tree[node] = (l[start],l[start])
        return tree[node]
    
    mid = (start+end)//2
    
    left = make_tree((node*2),start,mid)
    right = make_tree((node*2)+1,mid+1, end)
    
    tree[node] = (min(left[0], right[0]), max(left[1], right[1]))
    return tree[node]


def find_max(node, start, end):
    if a > end or b < start:
        return (1000000000,0)

    mid = (start+end)//2

    if a <= start and end <= b:
        return tree[node]
    
    else:
        left = find_max(node*2, start, mid)
        right = find_max((node*2)+1, mid+1, end)
        return (min(left[0], right[0]), max(left[1], right[1]))





N, M = map(int, input().split())
l = []
for _ in range(N):
    l.append(int(input().rstrip()))
    
b = math.ceil(math.log2(N)) + 1
node_n = 1 << b

tree = [0 for _ in range(node_n)]
make_tree(1,0,N-1)

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    a = a-1
    b = b-1
    ans = find_max(1,0,N-1)
    print(ans[0], ans[1])
