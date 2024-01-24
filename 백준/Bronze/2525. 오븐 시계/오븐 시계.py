H, M = input().split()
t = int(input())
h = int(H)
m = int(M)

a = (t + m) // 60 

h = h + a
if h >= 24:
    h = h - 24
print (h, t+m-(60*a))