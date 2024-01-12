T = int(input())
x = 0
y = 0

while x < T:
    R, S = input().split()
    r = int(R)
    while y < len(S):
        result = ((S[y]) * r)
        print(result,end="")
        y += 1
    print()
    x += 1
    y = 0