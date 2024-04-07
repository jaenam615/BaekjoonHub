N = int(input())
str = input() + " "
ans = 0
temp = []
temp2 = 0

for i in range(N):
    if str[i].isdigit():
        temp.append(str[i])
        
        if str[i+1].isdigit():
            continue
            
        temp2 = "".join(temp)
        ans += int(temp2)
        
        temp = []
        temp2 = 0

print(ans)
