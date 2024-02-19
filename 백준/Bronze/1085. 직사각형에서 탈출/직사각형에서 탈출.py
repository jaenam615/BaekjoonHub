x, y, w, h = map(int, input().split())

least_dist = min(w-x, h-y, x, y)

print(least_dist)