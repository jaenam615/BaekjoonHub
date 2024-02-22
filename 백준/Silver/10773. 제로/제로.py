K = int(input())
numlist = []

for _ in range(K):
    val = int(input())
    if val == 0:
        numlist.pop()
        continue
    numlist.append(val)
    
print(sum(numlist))