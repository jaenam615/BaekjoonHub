numbers = []
i = 1 

while i < 10:
    a = int(input())
    numbers.append(a)
    i += 1

print(max(numbers))
print(numbers.index(max(numbers))+1)