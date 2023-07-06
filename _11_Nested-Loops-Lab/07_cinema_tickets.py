ticket_counter = 0
student_counter = 0
standard_counter = 0
kid_counter = 0

while True:
    film_name = input()
    if film_name == 'Finish':
        break
    free_places = int(input())
    taken_places = 0
    while free_places > taken_places:
        ticket_type = input()
        if ticket_type == 'End':
            break
        ticket_counter += 1
        taken_places += 1
        if ticket_type == 'student':
            student_counter +=1
        elif ticket_type == 'standard':
            standard_counter +=1
        elif ticket_type == 'kid':
            kid_counter += 1
    result1 = taken_places / free_places * 100
    print(f'{film_name} - {result1:.2f}% full.')

result2 = student_counter / ticket_counter * 100
result3 = standard_counter / ticket_counter * 100
result4 = kid_counter / ticket_counter * 100

print(f'Total tickets: {ticket_counter}\n{result2:.2f}% student tickets.\n{result3:.2f}% standard tickets.\n'
      f'{result4:.2f}% kids tickets.')
