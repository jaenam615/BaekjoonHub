H , M = input().split()
h = int(H)
m = int(M)

if m - 45 >= 0:
    print(h, m-45)
else:
    if h != 0:
        print(h-1, 15+m)
    else: 
        print(23, 15+m)