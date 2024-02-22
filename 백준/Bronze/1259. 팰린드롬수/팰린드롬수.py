import math

while True:
    next = 0
    a = input().lstrip("0")
    if not a:
        break
    for i in range(math.floor((len(a)/2))):
        if a[i] != a[-(i+1)]:
            next = 1    
            print("no")
            break
    if next == 1:
        continue
    print("yes")        
