import sys

N = int(sys.stdin.readline())

mp = dict()

for _ in range(N):
    name = sys.stdin.readline().strip()
    if name in mp:
       mp[name] += 1
    else:
        mp[name] = 1

sorted_mp = sorted(mp.items(), key=lambda x: (-x[1], x[0]))
print(sorted_mp[0][0])