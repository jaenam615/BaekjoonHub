n = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x +10):
        for j in range(y, y + 10):
            arr[j][i] = 1

result = sum(sum(row) for row in arr)

print(result)