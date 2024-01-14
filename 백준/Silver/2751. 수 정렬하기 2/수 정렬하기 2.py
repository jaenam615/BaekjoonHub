import sys

N = int(sys.stdin.readline())
numbers = []
numbers2 = []
i = 0


while i < N:
    numbers.append(int(sys.stdin.readline()))
    i += 1

numbers.sort()

for number in numbers:
    print(number)