from sys import stdin

grade_point = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0,
}

arr = []
for _ in range(20):
    arr.append(list(stdin.readline().strip().split()))

total_score = 0.000000

total_credit = 0.000000

for i in range(20):
    subject, credit, grade = arr[i]
    credit = float(credit)
    if grade == "P":
        continue
    total_score += credit * grade_point[grade]
    total_credit += credit

print(total_score / total_credit)



