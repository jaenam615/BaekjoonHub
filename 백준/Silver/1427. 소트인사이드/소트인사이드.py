N = input()
number = []

for i in range(len(N)):
    number.append(int(N[i]))

number.sort(reverse=True)

print(*number, sep="")