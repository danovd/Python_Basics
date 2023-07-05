bad_grades_qty = int(input())

grades_sum = 0
tasks_sum = 0
last_task_name = ''
bad_grades_count = 0

while True:
    task_name = input()
    if task_name == 'Enough':
        average_grade = grades_sum / tasks_sum
        print(f'Average score: {average_grade:.2f}')
        print(f'Number of problems: {tasks_sum}')
        print(f'Last problem: {last_task_name}')
        break
    last_task_name = task_name
    grade = int(input())
    if grade <= 4:
        bad_grades_count += 1
        if bad_grades_count == bad_grades_qty:
            print(f'You need a break, {bad_grades_count} poor grades.')
            break
    tasks_sum += 1
    grades_sum += grade
