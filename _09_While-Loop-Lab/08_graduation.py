name = input()

count = 0
sum_grades = 0

while count != 12:
    grade = float(input())
    if grade < 4:
        continue
    else:
        count += 1
        sum_grades += grade

average_grades = sum_grades / count

print(f'{name} graduated. Average grade: {average_grades:.2f}')
