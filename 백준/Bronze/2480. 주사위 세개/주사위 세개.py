A, B, C  = input().split()
a = int(A)
b = int(B)
c = int(C)

if a == b == c:
    print(10000 + a*1000 )
elif a == b or b == c: 
    print(1000+ b*100)
elif a == c:
    print(1000 + a*100)
else: 
    d =  max(a, b, c)
    print (d*100)