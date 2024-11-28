
# Online Python - IDE, Editor, Compiler, Interpreter


def binary_search(newArr, total):
    start = 0
    end = max(newArr)
    target = 0
    
    while start <= end:
        mid = (start + end) // 2

        current = 0 
        for i in range(len(newArr)):
            current += min(mid, newArr[i])
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
    newArr = list(filter(lambda x: x > m//n, arr ))
    if len(newArr) == 0:
        print(max(arr))
    else:
        remainingPrice = m - (sum(arr) - sum(newArr))
        print(binary_search(newArr, remainingPrice))
    
