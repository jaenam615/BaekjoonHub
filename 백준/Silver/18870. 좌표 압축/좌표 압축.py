N = int(input())

Xn = list(enumerate(map(int, input().split())))
Xn.sort(key = lambda x : x[1])
final = [-1 for _ in range(N)]


final[Xn[0][0]] = 0

curvalue = 1

for i in range(1,len(Xn)):
    if Xn[i][1] != Xn[i-1][1]:  
        final[Xn[i][0]] = curvalue
        curvalue += 1
    else:
        final[Xn[i][0]] = final[Xn[i-1][0]]
        
print(*final)
        