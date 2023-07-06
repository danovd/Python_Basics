begin = int(input())
end = int(input())
magic_number = int(input())

counter_combination = 0

for x in range(begin, end+1):
    for y in range(begin, end+1):
        counter_combination += 1
        if x+y == magic_number:
            print(f'Combination N:{counter_combination} ({x} + {y} = {magic_number})')
            break
    if x+y == magic_number:
        break

if x+y != magic_number:
    print(f'{counter_combination} combinations - neither equals {magic_number}')
