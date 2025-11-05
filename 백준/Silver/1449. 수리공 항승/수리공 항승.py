N, L = map(int, input().split())

pipe = list(map(int, input().split()))

pipe.sort(reverse=True)

cover = L - 1
coverage = 0
count = 0

while pipe:
    hole = pipe.pop()
    if hole > coverage:
        coverage = hole + cover
        count += 1

print(count)