
# Online Python - IDE, Editor, Compiler, Interpreter


def binary_search(arr, total):
    start = 0
    end = max(arr)
    target = 0
    
    while start <= end:
        mid = (start + end) // 2
        current = 0 
        for i in range(len(arr)):
            current += min(mid, arr[i])
        
        if current <= total:
            target = mid
            start = mid + 1 
        else:
            end = mid - 1
    return target

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

if sum(arr) <= m:
    print(max(arr))
else:
    print(binary_search(arr , m))
    
