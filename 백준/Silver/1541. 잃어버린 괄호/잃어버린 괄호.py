Numbers = input().split("-")

for i in range(len(Numbers)):
    if "+" in Numbers[i]:
        Numbers[i] = sum(list(map(int, Numbers[i].split("+"))))
    else:
        Numbers[i] = int(Numbers[i])

if len(Numbers) == 1:
    print(Numbers[0])
else:
    for i in range(1, len(Numbers)):
        Numbers[0] -= Numbers[i]
    print(Numbers[0])
