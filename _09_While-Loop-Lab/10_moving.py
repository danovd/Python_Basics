free_space_weight = int(input())
free_space_length = int(input())
free_space_high = int(input())

free_area = free_space_high * free_space_weight * free_space_length
taken_area = 0

while taken_area <= free_area:
    command = input()
    if command == 'Done':
        left_area = free_area-taken_area
        print(f'{left_area} Cubic meters left.')
        break
    else:
        box_qty = int(command)
        taken_area += box_qty

if taken_area > free_area:
    needed_area = taken_area-free_area
    print(f'No more free space! You need {needed_area} Cubic meters more.')
