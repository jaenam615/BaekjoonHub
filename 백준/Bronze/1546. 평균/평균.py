N = int(input())

grade = list(map(int, input().split()))

M = max(grade)
average = 0

for i in range(len(grade)):
    average += grade[i]/M * 100
    
print(average/N)