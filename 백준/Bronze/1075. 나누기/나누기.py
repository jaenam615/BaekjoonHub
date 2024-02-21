N = (input())
F = int(input())

number = int(N)
first2 = number // 100
last2 = N[-2:]

for i in range(100):
    if (first2 * 100 + i) % F == 0:
        print(str(i).zfill(2))
        break