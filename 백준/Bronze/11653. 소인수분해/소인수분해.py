def factors(n):
    arr = []
    i = 2
    while True:
        if n == 1:
            break
        if n%i == 0:
            arr.append(i)
            n /= i
            i = 1
        i += 1
    return arr

ans = factors(int(input()))

for i in range(len(ans)):
    print(ans[i])