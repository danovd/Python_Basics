judges_qty = int(input())

total_sum_average_evaluation = 0
count = 0

while True:
    presentation_name = input()
    if presentation_name == 'Finish':
        break
    sum_evaluation = 0
    for i in range(judges_qty):
        evaluation = float(input())
        count += 1
        sum_evaluation += evaluation
        total_sum_average_evaluation += evaluation
    average_evaluation = sum_evaluation / judges_qty
    print(f'{presentation_name} - {average_evaluation:.2f}.')

total_average_evaluation = total_sum_average_evaluation / count
print(f'Student\'s final assessment is {total_average_evaluation:.2f}.')
