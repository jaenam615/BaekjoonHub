arr = [list(map(int, input().split())) for _ in range(9)]
maxi = [0 for _ in range(9)]



for i in range(9):
    maxi[i] = (max(arr[i]), arr[i].index(max(arr[i])))
     
print(max(maxi)[0])
print(maxi.index(max(maxi))+1, max(maxi)[1]+1)
