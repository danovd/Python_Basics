name = input()

count = 1
excluded = 0
sum_grades = 0

while count <= 12:
    grade = float(input())
    if grade < 4:
        excluded += 1
        if excluded == 2:
            break
        continue
    count += 1
    sum_grades += grade

if count == 13:
    average_grades = sum_grades / 12
    print(f'{name} graduated. Average grade: {average_grades:.2f}')
else:
    print(f'{name} has been excluded at {count} grade')
