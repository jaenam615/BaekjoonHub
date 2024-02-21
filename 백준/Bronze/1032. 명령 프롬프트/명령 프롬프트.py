N = int(input())

incoming = []
for i in range(N):
    incoming.append(input())

a = [0 for _ in range(len(incoming[0]))]

if N == 1:
    print(incoming[0])
    exit()

for i in range(len(incoming[0])):
    for j in range(N-1):
        if incoming[j][i] == incoming[j+1][i]:
            a[i] = incoming[j][i]
        else:
            a[i] = "?"
            break
        

print(*a, sep="")
        